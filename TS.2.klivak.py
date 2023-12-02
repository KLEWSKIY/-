import tkinter as tk
from threading import Thread

def fibonacci_recursive(n):
    if n <= 0:
        return "Номер повинен бути більше 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def calculate_fibonacci(n, result_label):
    result = fibonacci_recursive(n)
    result_label.config(text=f"Число Фібоначчі для n={n}: {result}")

def on_calculate_button_click(entry, result_label):
    try:
        n = int(entry.get())
        thread = Thread(target=calculate_fibonacci, args=(n, result_label))
        thread.start()
    except ValueError:
        result_label.config(text="Введіть коректне ціле число для n")

root = tk.Tk()
root.title("Обчислення числа Фібоначчі")

label = tk.Label(root, text="Введіть номер n:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Обчислити", command=lambda: on_calculate_button_click(entry, result_label))
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
