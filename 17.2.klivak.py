def limit_result(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result < a:
                result = a
            elif result > b:
                result = b
            return result
        return wrapper
    return decorator

@limit_result(a=0, b=10)
def f(x):
    return x * 2

result = f(15)
print(result)

result = f(-5)
print(result)

result = f(5)
print(result)
