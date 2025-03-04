import tkinter as tk  # Import Tkinter

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")  # Title of the window
root.geometry("300x430")  # Set size of the window

# Entry field to display numbers
entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Function to handle button clicks
def on_button_click(value):
    entry.insert(tk.END, value)  # Insert button text into the entry field

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)  # Delete everything in the entry field

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the field
        entry.insert(tk.END, result)  # Display the result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # If error occurs, show "Error"

# Define the button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),  # ✅ Plus sign is now in its correct place!
]

# Create and place buttons in the window
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Move the Clear button to a new row
clear_btn = tk.Button(root, text="C", width=22, height=2, font=("Arial", 14),
                      command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)  # ✅ Now it's in a new row!

# Run the main event loop
root.mainloop()
