from expense import Expense
from db_manager import DBManager

class Controller:
    def __init__(self):
        self.db_manager = DBManager()

    def add_expense(self, category, amount, date, description=''):
        expense = Expense(category, amount, date, description)
        self.db_manager.add_expense(expense)

    def get_all_expenses(self):
        return self.db_manager.get_expenses()
    
    def delete_expense(self, expense_id):
        self.db_manager.delete_expense(expense_id)
