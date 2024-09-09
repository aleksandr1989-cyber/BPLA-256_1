import unittest
from drone_control import Drone
from commands import CommandFactory


class TestDrone(unittest.TestCase):
    """Тесты для проверки функциональности класса Drone."""

    def setUp(self):
        """Создает экземпляр дрона перед каждым тестом."""
        self.drone = Drone()

    def test_initial_battery(self):
        """Проверяет, что уровень заряда дрона изначально равен 100."""
        self.assertEqual(self.drone.battery_level, 100)

    def test_move_forward(self):
        """Проверяет, что дрон движется вперед и уровень батареи снижается."""
        command = CommandFactory.get_command('forward', self.drone)
        self.drone.execute_command(command)
        self.assertEqual(self.drone.position, [5, 0])
        self.assertEqual(self.drone.battery_level, 99)

    def test_ascend(self):
        """Проверяет, что дрон поднимается и уровень батареи снижается."""
        command = CommandFactory.get_command('ascend', self.drone)
        self.drone.execute_command(command)
        self.assertEqual(self.drone.position, [0, 5])
        self.assertEqual(self.drone.battery_level, 99)


if __name__ == '__main__':
    unittest.main()
