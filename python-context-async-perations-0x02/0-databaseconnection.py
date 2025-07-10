import sqlite3

# Class-based context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        print("[LOG] Database connection opened.")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("[LOG] Database connection closed.")
        if exc_type:
            print(f"[ERROR] {exc_type.__name__}: {exc_val}")
        # Returning False will propagate exceptions if any
        return False

# Using the context manager to run a query
with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("Query Results:")
    for row in results:
        print(row)
