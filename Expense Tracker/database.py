import sqlite3

def setup_database():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


def add_expense_to_db(amount, category, description, date):
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
                   (amount, category, description, date))
    
    conn.commit()
    conn.close()


def get_all_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_expense_by_id(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id))
    conn.commit()
    conn.close()