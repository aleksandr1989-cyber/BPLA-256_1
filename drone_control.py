import matplotlib.pyplot as plt

class Drone:
    def __init__(self):
        self.battery_level = 100
        self.position = [0, 0]  # Начальные координаты (x=0, y=0)
        self.trajectory = []  # Список для хранения координат
        self.current_command = None  # Текущая команда

    def move(self, direction):
        if direction == 'forward':
            self.position[0] += 5  # Увеличение по оси X
        elif direction == 'backward':
            self.position[0] -= 5  # Уменьшение по оси X
        elif direction == 'ascend':
            self.position[1] += 5  # Увеличение по оси Y (высота)
        elif direction == 'descend':
            self.position[1] -= 5  # Уменьшение по оси Y (высота)

        # Сохраняем текущую позицию
        self.trajectory.append(self.position.copy())
        self.battery_level -= 1

    def plot_trajectory(self):
        if not self.trajectory:
            return

        # Индексы для временной оси
        time_vals = list(range(len(self.trajectory)))
        height_vals = [coord[1] for coord in self.trajectory]  # Высота из координат

        plt.figure()
        plt.plot(time_vals, height_vals, marker='o')
        plt.title('Траектория полета дрона')
        plt.xlabel('Время (или шаги управления)')
        plt.ylabel('Координата Y (высота)')
        plt.grid()

        # Сохраняем график
        plt.savefig('trajectory.png')
        plt.close()

    def get_status(self):
        return {
            "battery_level": self.battery_level,
            "altitude": self.position[1],  # Возвращает текущую высоту
            "current_command": self.current_command if self.current_command else "Нет"
        }

    def execute_command(self, command):
        command.execute()
        self.current_command = command.__class__.__name__  # Обновляем текущую команду

class AutopilotStrategy:
    def execute(self, drone):
        print("Автопилот активирован")
        drone.move('forward')
        drone.move('ascend')
        drone.move('backward')
        drone.move('descend')
