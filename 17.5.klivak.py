def check_types(type_name):
    def decorator(func):
        def wrapper(*args):
            if all(isinstance(arg, type_name) for arg in args):
                return func(*args)
            else:
                raise TypeError(f"Усі аргументи повинні бути {type_name}")
        return wrapper
    return decorator

@check_types(int)
def average(*args):
    return sum(args) / len(args)

try:
    result = average(1, 2, 3, 4, 5)
    print(f"Середнє: {result}")
except TypeError as e:
    print(e)

try:
    result = average(1, 2, '3', 4, 5)
    print(f"Average: {result}")
except TypeError as e:
    print(e)
