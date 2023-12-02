import subprocess
import time

def run_student_program(program_path, arguments):
    try:
        start_time = time.time()
        result = subprocess.run(
            ["python", program_path] + list(arguments),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        end_time = time.time()

        return {
            "success": True,
            "output": result.stdout.strip(),
            "error": result.stderr.strip(),
            "execution_time": end_time - start_time
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Timeout expired"}
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": f"Error: {e.stderr.strip()}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

def check_test_case(test_case):
    try:
        parts = test_case.strip().split()
        program_path = parts[0]
        arguments = eval(parts[1])
        expected_output = eval(parts[2])

        print(f"Running test: {test_case}")
        result = run_student_program(program_path, arguments)

        print(f"Output: {result['output']}")
        print(f"Error: {result['error']}")
        print(f"Execution Time: {result['execution_time']} seconds")

        if result["success"]:
            if isinstance(expected_output, int) or isinstance(expected_output, float):
                tolerance = 1e-6
                actual_output = float(result["output"])
                if abs(actual_output - expected_output) < tolerance:
                    print("Test passed!\n")
                else:
                    print(f"Test failed! Expected: {expected_output}, Actual: {actual_output}\n")
            elif isinstance(expected_output, str):
                if result["output"] == expected_output:
                    print("Test passed!\n")
                else:
                    print(f"Test failed! Expected: {expected_output}, Actual: {result['output']}\n")
        else:
            print(f"Test failed! {result['error']}\n")
    except Exception as e:
        print(f"Error processing test case: {str(e)}")

def student_program():
    # Вхідні дані
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")

    result = f"Привіт, {name}! Вам вже цілих {age} років."

    print(result)

if __name__ == "__main__":

    test_cases = [
        "path_to_program.py ('Mark', '25') ('str': 'Привіт, Mark! Вам вже цілих 25 років.')",

    ]

    for test_case in test_cases:
        check_test_case(test_case)

    student_program()

