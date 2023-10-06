import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Entry widget for displaying the input and output
        entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        current_result = self.result_var.get()

        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = str(eval(current_result))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_result + value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
