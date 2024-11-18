import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Expense Tracker')

add_button = tk.Button(root, text='Add Expense', width=20)
view_button = tk.Button(root, text='View Summary', width=20)
delete_button = tk.Button(root, text='Delete Entry', width=20)

add_button.grid(row=0, column=0, padx=10, pady=10)
view_button.grid(row=0, column=1, padx=10, pady=10)
delete_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
