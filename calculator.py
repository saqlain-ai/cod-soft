import customtkinter as ctk

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"

        result_label.configure(text=f"Result: {result}")
    except ValueError:
        result_label.configure(text="Error: Invalid input")

def create_calculator():
    window = ctk.CTk()
    window.title("Simple Calculator")
    window.geometry("250x250")
    window.resizable(False, False)

    main_frame = ctk.CTkFrame(window, corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    global num1_entry, num2_entry, operation_var, result_label
    num1_entry = ctk.CTkEntry(main_frame, width=20)
    num2_entry = ctk.CTkEntry(main_frame, width=20)
    operation_var = ctk.StringVar(value="Addition")
    result_label = ctk.CTkLabel(main_frame, text="")

    num1_label = ctk.CTkLabel(main_frame, text="Number 1:")
    num1_label.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    num1_entry.grid(row=0, column=1, padx=10, pady=10, sticky="news")

    num2_label = ctk.CTkLabel(main_frame, text="Number 2:")
    num2_label.grid(row=1, column=0, padx=10, pady=10, sticky="news")
    num2_entry.grid(row=1, column=1, padx=10, pady=10, sticky="news")

    operation_label = ctk.CTkLabel(main_frame, text="Operation:")
    operation_label.grid(row=2, column=0, padx=10, pady=10, sticky="news")
    operation_option = ctk.CTkOptionMenu(main_frame, variable=operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"])
    operation_option.grid(row=2, column=1, padx=10, pady=10, sticky="news")

    calculate_button = ctk.CTkButton(main_frame, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    return window

if __name__ == "__main__":
    window = create_calculator()
    window.mainloop()