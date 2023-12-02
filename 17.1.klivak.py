def ensure_positive_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 0:
            result = 1
        return result
    return wrapper

@ensure_positive_result
def f(x):
    return x - 5

result = f(10)
print(result)

result = f(3)
print(result)
