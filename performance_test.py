import timeit
from drone_control import Drone


drone = Drone()


def test_move():
    """Тестировочная функция для перемещения дрона."""
    drone.move('forward')


if __name__ == "__main__":
    # Замер времени выполнения метода move
    move_time = timeit.timeit(test_move, number=1000)
    print(f"Время выполнения move('forward') 1000 раз: {move_time:.5f} секунд")

