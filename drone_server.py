from flask import Flask, jsonify, request, render_template
from drone_control import Drone, AutopilotStrategy
from commands import CommandFactory
import logging

# Конфигурация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)
drone = Drone()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control_drone():
    command_name = request.json.get('command')
    command = CommandFactory.get_command(command_name, drone)

    # Обновите названия команд для отображения
    missions = {
        'ascend': 'Взлет',
        'descend': 'Посадка',
        'forward': 'Вперед',
        'backward': 'Назад',
        'left': 'Влево',
        'right': 'Вправо',
        'patrol': 'Патрулирование',
    }

    if command:
        drone.execute_command(command)
        # Логируем выполнение команды
        logging.info(f'Команда: "{command_name}" выполнена.')
        drone.current_command = missions[command_name]  # Обновляем текущую команду с корректным названием
        return jsonify({'status': f'Команда "{missions[command_name]}" отправлена на дрон'})
    else:
        return jsonify({'status': 'Неизвестная команда'}), 400

@app.route('/status')
def get_status():
    status = drone.get_status()
    return jsonify(status)

@app.route('/autopilot', methods=['POST'])
def start_autopilot():
    strategy = AutopilotStrategy()
    strategy.execute(drone)
    return jsonify({'status': 'Автопилот запущен'})

@app.route('/save_trajectory', methods=['POST'])
def save_trajectory():
    drone.plot_trajectory()
    return jsonify({'status': 'Траектория сохранена'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
