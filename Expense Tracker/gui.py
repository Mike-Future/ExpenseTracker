import tkinter as tk
from tkinter import ttk
from database import add_expense_to_db, get_all_expenses, delete_expense_by_id

def add_expense_window(root):
    add_window = tk.Toplevel(root)
    add_window.title('Add Expense')

    tk.Label(add_window, text='Amount:').grid(row=0, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(add_window)
    amount_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Category:').grid(row=1, column=0, padx=10, pady=5)
    category_entry = tk.Entry(add_window)
    category_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Description:').grid(row=2, column=0, padx=10, pady=5)
    description_entry = tk.Entry(add_window)
    description_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text='Date (YYYY-MM-DD):').grid(row=3, column=0, padx=10, pady=5)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=3, column=1, padx=10, pady=5)

    def save_expense():
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        add_expense_to_db(amount, category, description, date)
        add_window.destroy()

    tk.Button(add_window, text='Save', command=save_expense).grid(row=4, column=0, columnspan=2, pady=10)


def view_summary_window(root):
    summary_window = tk.Toplevel(root)
    summary_window.title('Expense Summary')

    columns = ('ID', 'Amount', 'Category', 'Description', 'Date')
    tree = ttk.Treeview(summary_window, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill=tk.Both, expand=True)

    rows = get_all_expenses()
    for row in rows:
        tree.insert('', tk.END, values=row)
    

def delete_expense_window(root):
    delete_window = tk.Toplevel(root)
    delete_window.title('Delete Expense')

    tk.Label(delete_window, text='Enter ID to delete:').grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    def delete_expense():
        expense_id = int(id_entry.get())
        delete_expense_by_id(expense_id)
        delete_window()

    tk.Button(delete_window, text='Delete', command=delete_expense).grid(row=1, column=0, columnspan=2, pady=10)
