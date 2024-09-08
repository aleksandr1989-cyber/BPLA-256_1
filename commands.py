class Command:
    def execute(self):
        pass

class MoveForwardCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('forward')

class MoveBackwardCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('backward')

class AscendCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('ascend')

class DescendCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('descend')

class RotateLeftCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('rotate_left')

class RotateRightCommand(Command):
    def __init__(self, drone):
        self.drone = drone

    def execute(self):
        self.drone.move('rotate_right')

class CommandFactory:
    _commands = {}

    @staticmethod
    def get_command(command_name, drone):
        if command_name not in CommandFactory._commands:
            if command_name == 'forward':
                CommandFactory._commands[command_name] = MoveForwardCommand(drone)
            elif command_name == 'backward':
                CommandFactory._commands[command_name] = MoveBackwardCommand(drone)
            elif command_name == 'ascend':
                CommandFactory._commands[command_name] = AscendCommand(drone)
            elif command_name == 'descend':
                CommandFactory._commands[command_name] = DescendCommand(drone)
            elif command_name == 'rotate_left':
                CommandFactory._commands[command_name] = RotateLeftCommand(drone)
            elif command_name == 'rotate_right':
                CommandFactory._commands[command_name] = RotateRightCommand(drone)

        return CommandFactory._commands[command_name]
