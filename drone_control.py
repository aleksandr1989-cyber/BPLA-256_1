import logging
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from commands import MoveForwardCommand, MoveBackwardCommand, AscendCommand, DescendCommand, MoveUpCommand, MoveDownCommand

# Настройка логирования
logging.basicConfig(filename='drone_log.txt', filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Drone:
    """Класс для управления дроном."""

    def __init__(self):
        """Инициализирует дрон с начальным уровнем заряда и позицией."""
        self.battery_level = 100
        self.position = [0, 0]
        self.trajectory = []
        self.current_command = "Нет"

    def move(self, direction):
        """Перемещает дрон в указанном направлении и обновляет его состояние.

        Args:
            direction (str): Направление движения ('forward', 'backward', 'ascend', 'descend', 'up', 'down').
        """
        if direction == 'forward':
            self.position[0] += 5
        elif direction == 'backward':
            self.position[0] -= 5
        elif direction == 'ascend':
            self.position[1] += 5
        elif direction == 'descend':
            self.position[1] -= 5
        elif direction == 'up':
            self.position[1] += 5
        elif direction == 'down':
            self.position[1] -= 5

        self.trajectory.append(self.position.copy())
        self.battery_level -= 1  # Снижаем уровень заряда на каждое движение

    def can_execute_command(self, command):
        """Проверяет, можно ли выполнить команду на основании уровня заряда.

        Args:
            command (Command): Команда для проверки.

        Returns:
            bool: True, если команду можно выполнить, False в противном случае.
        """
        # Определяем порог для низкого уровня батареи
        battery_threshold = 20
        # Если заряд ниже порога, ограничиваем команды
        if self.battery_level < battery_threshold:
            if isinstance(command, (AscendCommand, MoveUpCommand)):
                return False
        return True

    def execute_command(self, command):
        """Выполняет данную команду, проверяя уровень заряда.

        Args:
            command (Command): Команда для выполнения.
        """
        if self.can_execute_command(command):
            command.execute()
            self.update_current_command(command)
        else:
            self.current_command = "ВНИМАНИЕ! Низкий заряд батареи!"
            print(f"Ошибка: Низкий уровень заряда батареи. Команда не может быть выполнена.")

    def update_current_command(self, command):
        """Обновляет текущее состояние команды.

        Args:
            command (Command): Зафиксированная команда.
        """
        if isinstance(command, MoveForwardCommand):
            self.current_command = "Вперед"
        elif isinstance(command, MoveBackwardCommand):
            self.current_command = "Назад"
        elif isinstance(command, AscendCommand):
            self.current_command = "Взлет"
        elif isinstance(command, DescendCommand):
            self.current_command = "Посадка"
        elif isinstance(command, MoveUpCommand):
            self.current_command = "Набираем высоту"
        elif isinstance(command, MoveDownCommand):
            self.current_command = "Дрон снижается"

    def optimize_trajectory(self, target):
        def loss_function(trajectory):
            return sum((t - target) ** 2 for t in trajectory)

        result = minimize(loss_function, self.trajectory)
        return result.x

    def get_status(self):
        """Получает текущее состояние дрона.

        Returns:
            dict: Словарь с текущими координатами и уровнем батареи.
        """
        return {
            "battery_level": self.battery_level,
            "altitude": self.position[1],
            "current_command": self.current_command
        }

    def plot_trajectory(self):
        """Строит график маршрута дрона и выводит его в файл.

        Returns:
            trajectory.png.
        """
        if not self.trajectory:
            return

        time_vals = list(range(len(self.trajectory)))
        height_vals = [coord[1] for coord in self.trajectory]

        plt.figure()
        plt.plot(time_vals, height_vals, marker='o')
        plt.title('Траектория полета дрона')
        plt.xlabel('Время (или шаги управления)')
        plt.ylabel('Координата Y (высота)')
        plt.grid()
        plt.savefig('trajectory.png')
        plt.close()


class AutopilotStrategy:
    def execute(self, drone):
        print("Патрулирование выполняется")
        drone.move('forward')
        drone.move('ascend')
        drone.move('backward')
        drone.move('descend')
