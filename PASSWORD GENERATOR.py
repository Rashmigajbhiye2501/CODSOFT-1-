import tkinter as tk
import random
import string

def generate_password():
    username = entry_username.get()
    password_length = entry_length.get()

    if not password_length.isdigit() or int(password_length) <= 0:
        result.set("Invalid password length.")
        return

    password_length = int(password_length)

    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user preferences
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password using random.choice and truncate if longer than specified length
    generated_password = ''.join(random.choice(all_characters) for _ in range(password_length))

    # Truncate the password if longer than specified length
    generated_password = generated_password[:password_length]

    # Display the generated password with username
    result.set(f"{generated_password}")

def reset_fields():
    entry_username.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    result.set("")

def accept_fields():
    entry_username.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    result.set("")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Title label in the middle of the window (above side)
title_label = tk.Label(window, text="Password Generator", font=('Arial', 16, 'bold', 'underline'), fg="navy blue")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entry for username
label_username = tk.Label(window, text="Username:")
label_username.grid(row=1, column=0, padx=10, pady=5)
entry_username = tk.Entry(window)
entry_username.grid(row=1, column=1, padx=10, pady=5)

# Entry for password length
label_length = tk.Label(window, text="Password Length:")
label_length.grid(row=2, column=0, padx=10, pady=5)
entry_length = tk.Entry(window)
entry_length.grid(row=2, column=1, padx=10, pady=5)

# Display the generated password label
label_generated_password = tk.Label(window, text="Generated Password:")
label_generated_password.grid(row=3, column=0, pady=5)

# Display the generated password with username
result = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result, state='readonly', font=('Arial', 14))
result_entry.grid(row=4, column=0, columnspan=2, pady=10)

# Button to generate password (in blue color)
generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="navy blue", fg="white")
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Reset button (white background with black border and blue font color)
reset_button = tk.Button(window, text="Reset", command=reset_fields, bg="white", fg="blue", bd=2, relief="solid")
reset_button.grid(row=6, column=0, columnspan=2, pady=10)

# Accept button (white background with black border and blue font color)
accept_button = tk.Button(window, text="Accept", command=accept_fields, bg="white", fg="blue", bd=2, relief="solid")
accept_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
