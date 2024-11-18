import tkinter as tk
from database import setup_database
from gui import add_expense_window, view_summary_window, delete_expense_window

def main():
    setup_database()

    root = tk.Tk()
    root.title('Expense Tracker')

    tk.Button(root, text='Add Expense', width=20, command=lambda: add_expense_window(root)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(root, text='View Summary', width=20, command=lambda: view_summary_window(root)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text='Delete Entry', width=20, command=lambda: delete_expense_window(root)).grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()