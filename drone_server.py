from flask import Flask, jsonify, request, render_template
from drone_control import Drone, AutopilotStrategy
from commands import CommandFactory
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)
drone = Drone()


@app.route('/')
def index():
    """Отображает главную страницу интерфейса управления дроном."""
    return render_template('index.html')


@app.route('/control', methods=['POST'])
def control_drone():
    """Обрабатывает команды управления дроном.

    Выполняет команду, переданную через POST-запрос.

    Returns:
        jsonify: Статус выполнения команды.
    """
    command_name = request.json.get('command')
    command = CommandFactory.get_command(command_name, drone)

    missions = {
        'ascend': 'Взлет',
        'descend': 'Посадка',
        'forward': 'Вперед',
        'backward': 'Назад',
        'up': 'Набираем высоту',
        'down': 'Дрон снижается',
    }

    if command:
        drone.execute_command(command)
        logging.info(f'Команда: "{command_name}" выполнена.')
        return jsonify({'status': f'Команда "{missions[command_name]}" отправлена на дрон'})
    else:
        return jsonify({'status': 'Неизвестная команда'}), 400


@app.route('/status')
def get_status():
    """Возвращает текущее состояние дрона.

    Returns:
        jsonify: Состояние дрона (позиция, уровень заряда и текущая команда).
    """
    status = drone.get_status()
    return jsonify(status)


@app.route('/optimize', methods=['POST'])
def optimize():
    """Оптимизирует траекторию полета дроном.

    Returns:
        jsonify: Оптимизированная траектория.
    """
    target = request.json.get('target')
    optimized_trajectory = drone.optimize_trajectory(target)
    return jsonify({'optimized_trajectory': optimized_trajectory.tolist()})


@app.route('/autopilot', methods=['POST'])
def start_autopilot():
    """Запускает режим автопилота для дрона.

    Returns:
        jsonify: Статус запуска автопилота.
    """
    strategy = AutopilotStrategy()
    strategy.execute(drone)
    return jsonify({'status': 'Автопилот запущен'})


@app.route('/save_trajectory', methods=['POST'])
def save_trajectory():
    """Сохраняет выполненную траекторию полета.

    Returns:
        jsonify: Статус сохранения траектории.
    """
    drone.plot_trajectory()
    return jsonify({'status': 'Траектория сохранена'})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
