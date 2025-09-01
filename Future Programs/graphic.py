# calculator.py

import tkinter as tk

# Define the functions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Define the function to calculate the result
def calculate():
    first = int(num1.get())
    second = int(num2.get())
    operator = operation.get()

    if operator == '+':
        result.set(add(first, second))
    elif operator == '-':
        result.set(subtract(first, second))
    elif operator == '*':
        result.set(multiply(first, second))
    elif operator == '/':
        result.set(divide(first, second))
    elif operator == '//':
        result.set(divmod(first, second)[0])
    elif operator == '%':
        result.set(divmod(first, second)[1])
    else:
        result.set("Invalid operator")

# Create the main window and set its properties
root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")
root.configure(bg="#fff")

# Create the widgets for the calculator
num1_label = tk.Label(root, text="Enter first number:")
num1_label.grid(row=0, column=0, padx=10, pady=10)

num1 = tk.Entry(root)
num1.grid(row=0, column=1, padx=10, pady=10)

num2_label = tk.Label(root, text="Enter second number:")
num2_label.grid(row=1, column=0, padx=10, pady=10)

num2 = tk.Entry(root)
num2.grid(row=1, column=1, padx=10, pady=10)

operation_label = tk.Label(root, text="Select operation:")
operation_label.grid(row=2, column=0, padx=10, pady=10)

operation = tk.StringVar(root)
operation.set("+")

operation_menu = tk.OptionMenu(root, operation, "+", "-", "*", "/", "//", "%")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#007bff", fg="#fff", padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, padx=10, pady=10)

result = tk.StringVar(root)

result_entry = tk.Entry(root, textvariable=result, state="readonly")
result_entry.grid(row=4, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()






'''import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyFirstKivyApp(App):

    def build(self):
        return Label(text='Hello, World!')

if __name__ == '__main__':
    MyFirstKivyApp().run()'''
















