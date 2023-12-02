import threading

class CustomThread(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        super().__init__(target=target, args=args, kwargs=kwargs)
        self._exception = None

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **(self._kwargs or {}))
        except Exception as e:
            self._exception = e

    def propagate_exception(self):
        if self._exception:
            raise self._exception


def calculate_factorial(n):
    if not isinstance(n, int):
        raise ValueError("Ввід має бути цілим числом")
    if n < 0:
        raise ValueError("Ввід має бути цілим невід’ємним числом")

    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Факторіал з {n} є {result}")


if __name__ == "__main__":
    try:
        thread = CustomThread(target=calculate_factorial, args=(5,))

        thread.start()

        thread.join()

        thread.propagate_exception()

    except Exception as e:
        print(f"Виняток у головному потоці: {e}")





