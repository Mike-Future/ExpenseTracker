import tkinter as tk
from gui import ExpenseTrackerGui

if __name__ == '__main__':
    root = tk.Tk()
    app = ExpenseTrackerGui(root)
    root.mainloop()