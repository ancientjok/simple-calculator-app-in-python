import tkinter as tk

calculator = tk.Tk()
calculator.title("Calculator")

expression_field = tk.Entry(calculator)
expression_field.grid(row=0, column=0, columnspan=4)

def button_click(button_text):
  current_expression = expression_field.get()

  new_expression = current_expression + button_text

  expression_field.delete(0, tk.END)
  expression_field.insert(0, new_expression)

digit_buttons = [
  tk.Button(calculator, text=str(i), command=lambda i=i: button_click(str(i))) for i in range(10)
]

operator_buttons = [
  tk.Button(calculator, text="+", command=lambda: button_click("+")),
  tk.Button(calculator, text="-", command=lambda: button_click("-")),
  tk.Button(calculator, text="*", command=lambda: button_click("*")),
  tk.Button(calculator, text="/", command=lambda: button_click("/")),
]

for i, digit_button in enumerate(digit_buttons):
  digit_button.grid(row=i // 3 + 1, column=i % 3)

for i, operator_button in enumerate(operator_buttons):
  operator_button.grid(row=i + 1, column=3)

equals_button = tk.Button(calculator, text="=", command=lambda: evaluate_expression())
equals_button.grid(row=4, column=3)

def evaluate_expression():
  try:
    expression = expression_field.get()

    result = eval(expression)

    expression_field.delete(0, tk.END)
    expression_field.insert(0, result)
  except:
    expression_field.delete(0, tk.END)
    expression_field.insert(0, "Error")

calculator.mainloop()
