import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result.set(eval(expression))
    except Exception as e:
        result.set("Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for input
entry = tk.Entry(window, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '+', '-',
    '*', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2,
              command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Equal button
tk.Button(window, text='=', width=5, height=2, command=calculate).grid(row=row_val, column=col_val, padx=5, pady=5)

# Clear button
tk.Button(window, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val+1, padx=5, pady=5)

# Display result
result = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result, state='readonly', font=('Arial', 14))
result_entry.grid(row=row_val+1, column=0, columnspan=4, pady=10)

# Run the Tkinter event loop
window.mainloop()
