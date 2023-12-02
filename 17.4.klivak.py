def check_strings(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("Усі аргументи повинні бути рядками.")
        return func(*args)
    return wrapper

@check_strings
def remove_duplicates(*args):
    return list(set(args))

result = remove_duplicates("a", "c", "b", "a", "b")
print(result)
