import tkinter as tk
from tkinter import messagebox
from controller import Controller

class ExpenseTrackerGui:
    def __init__(self, root):
        self.controller = Controller()
        self.root = root
        self.root.title('Expense Tracker')

        # ENtry fields
        self.category_entry = tk.Entry(root)
        self.amount_entry = tk.Entry(root)
        self.date_entry = tk.Entry(root)
        self.description_entry = tk.Entry(root)

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text='Category').grid(row=0, column=0)
        tk.Label(self.root, text='Amount').grid(row=1, column=0)
        tk.Label(self.root, text='Date').grid(row=2, column=0)
        tk.Label(self.root, text='Description').grid(row=3, column=0)

        self.category_entry.grid(row=0, column=1)
        self.amount_entry.grid(row=1, column=1)
        self.date_entry.grid(row=2, column=1)
        self.description_entry.grid(row=3, column=1)

        # Buttons
        add_button = tk.Button(self.root, text='Add Expense', command=self.add_expense)
        add_button.grid(row=4, column=0, columnspan=2)

        view_button = tk.Button(self.root, text='View Expenses', command=self.view_expenses)
        view_button.grid(row=5, column=0, columnspan=2)

    def add_expense(self):
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())
        date = self.date_entry.get()
        description = self.description_entry.get()

        self.controller.add_expense(category, amount, date, description)
        messagebox.showinfo('Success', 'Expense added sucessfully!')

    def view_expenses(self):
        expenses = self.controller.get_all_expenses()
        view_window = tk.Toplevel(self.root)
        view_window.title('View Expenses')

        for i, expense in enumerate(expenses):
            tk.Label(view_window, text=str(expense)).grid(row=i, column=0)
