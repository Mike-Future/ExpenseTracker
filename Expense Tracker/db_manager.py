import sqlite3

class DBManager:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            category TEXT,
            amount REAL,
            date TEXT,
            description TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, expense):
        query = "INSERT INTO expenses (category, amount, date, description) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (expense.category, expense.amount, expense.date, expense.description))
        self.conn.commit()

    def get_expenses(self):
        cursor = self.conn.execute("SELECT * FROM expenses")
        return cursor.fetchall()

    def delete_expense(self, expense_id):
        query = "DELETE FROM expenses WHERE id = ?"
        self.conn.execute(query, (expense_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
