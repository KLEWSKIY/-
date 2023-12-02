def check_argument_count(func):
    def wrapper(*args, **kwargs):
        if len(args) != len(kwargs):
            raise ValueError("Кількість позиційних та ключових аргументів не співпадає")
        return func(*args, **kwargs)
    return wrapper

@check_argument_count
def f(*x, **y):
    result = 1
    for xi, yi in zip(x, y.values()):
        result *= (xi + 1/yi)
    return result

result = f(1, 2, 3, y1=4, y2=5, y3=6)
print(result)

try:
    result = f(1, 2, 3, y1=4, y2=5)
except ValueError as e:
    print(e)
