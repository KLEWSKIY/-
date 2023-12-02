import re

def read_program(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_program_variables(program_text):
    variables = {}
    assignments = re.findall(r'(\w+)\s*=\s*([^#]+)', program_text)

    for variable, expression in assignments:
        variables[variable] = expression.strip()

    return variables

def check_used_before_defined(variables):
    used_before_defined = set()
    for value in variables.values():
        for variable in variables:
            if variable in value:
                used_before_defined.add(variable)
    return used_before_defined

def main(file_path):
    program_text = read_program(file_path)
    variables = get_program_variables(program_text)
    used_before_defined = check_used_before_defined(variables)

    if used_before_defined:
        print(f"Помилка: Змінні {', '.join(used_before_defined)} використовуються до визначення.")
    else:
        print("Змінні:")
        for name, value in variables.items():
            print(f"{name}: {value}")

if __name__ == "__main__":
    file_path = r"C:\need\kchay\Файли\Файл.py"
    main(file_path)
