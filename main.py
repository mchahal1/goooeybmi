# BMI Calculator
# BMI = mass / (height**2)

import customtkinter as ctk

root = ctk.CTk()  # This creates a root window which is the main window that pops up
root.title("BMI Calculator")
root.geometry("250x250")

# Calculate BMI function
def calculate_bmi():
    weight = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(weight / (height**2), 2)
    label_result.configure(text=f"BMI: {bmi} kg/m\u00B2")

# Create GUI
# Weight
label_kg = ctk.CTkLabel(root, text="Weight (kg): ")  # First step
# Geometry manager to manage the placement of the elements (it is autosized by default)
# label_kg.grid(column=0, row=0)
label_kg.pack(pady=(20, 10))

entry_kg = ctk.CTkEntry(root)  # For text input
# entry_kg.grid(column=1, row=0)
entry_kg.pack()

# Height
label_height = ctk.CTkLabel(root, text="Height (m): ")
# label_height.grid(column=0, row=1)
label_height.pack(pady=(0, 10))

entry_height = ctk.CTkEntry(root)  # For text input
# entry_height.grid(column=1, row=1)
entry_height.pack()

# Button
button_calculate = ctk.CTkButton(
    root, text="Calculate", command=calculate_bmi)
# button_calculate.grid(column=1, row=2)
button_calculate.pack(pady=10)

# Result
label_result = ctk.CTkLabel(root, text="BMI: ")
# label_result.grid(column=0, row=2)
label_result.pack()

# Run the program only if this file is run directly
if __name__ == "__main__":
    root.mainloop()  # Must have to keep the window open at all times