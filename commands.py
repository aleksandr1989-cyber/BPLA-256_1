class Command:
    """Базовый класс для команд управления дроном."""

    def execute(self):
        """Выполняет команду. Это метод заглушка и должен быть переопределен в подклассах."""
        pass


class MoveForwardCommand(Command):
    """Команда для перемещения дрона вперед."""

    def __init__(self, drone):
        """Инициализирует команду перемещения вперед.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду перемещения дрона вперед."""
        self.drone.move('forward')


class MoveBackwardCommand(Command):
    """Команда для перемещения дрона назад."""

    def __init__(self, drone):
        """Инициализирует команду перемещения назад.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду перемещения дрона назад."""
        self.drone.move('backward')


class AscendCommand(Command):
    """Команда для подъема дрона."""

    def __init__(self, drone):
        """Инициализирует команду подъема.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду подъема дрона."""
        self.drone.move('ascend')


class DescendCommand(Command):
    """Команда для спуска дрона."""

    def __init__(self, drone):
        """Инициализирует команду спуска.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду спуска дрона."""
        self.drone.move('descend')


class MoveUpCommand(Command):
    """Команда для набора высоты дрона."""

    def __init__(self, drone):
        """Инициализирует команду набора высоты.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду набора высоты дрона."""
        self.drone.move('up')


class MoveDownCommand(Command):
    """Команда для снижения высоты дрона."""

    def __init__(self, drone):
        """Инициализирует команду снижения.

        Args:
            drone (Drone): Экземпляр дрона, который будет выполнять команду.
        """
        self.drone = drone

    def execute(self):
        """Выполняет команду снижения высоты дрона."""
        self.drone.move('down')


class CommandFactory:
    """Фабрика для создания команд."""

    _commands = {}

    @staticmethod
    def get_command(command_name, drone):
        """Получает команду по её имени, создавая её при необходимости.

        Args:
            command_name (str): Название команды.
            drone (Drone): Экземпляр дрона для выполнения команды.

        Returns:
            Command: Экземпляр соответствующей команды или None, если команда не распознана.
        """
        if command_name not in CommandFactory._commands:
            if command_name == 'forward':
                CommandFactory._commands[command_name] = MoveForwardCommand(drone)
            elif command_name == 'backward':
                CommandFactory._commands[command_name] = MoveBackwardCommand(drone)
            elif command_name == 'ascend':
                CommandFactory._commands[command_name] = AscendCommand(drone)
            elif command_name == 'descend':
                CommandFactory._commands[command_name] = DescendCommand(drone)
            elif command_name == 'up':
                CommandFactory._commands[command_name] = MoveUpCommand(drone)
            elif command_name == 'down':
                CommandFactory._commands[command_name] = MoveDownCommand(drone)

        return CommandFactory._commands.get(command_name)
