import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=(), db_name='users.db'):
        self.query = query
        self.params = params
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print("[LOG] Executing query:", self.query)
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("[LOG] Connection closed.")
        if exc_type:
            print(f"[ERROR] {exc_type.__name__}: {exc_value}")
        # Don't suppress exceptions
        return False

# Usage of the context manager
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    print("Query Results:")
    for row in results:
        print(row)
# This code defines a context manager for executing SQL queries using SQLite.
# It connects to a database, executes a query with parameters, and fetches results.