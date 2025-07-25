import time
import sqlite3
import functools

query_cache = {}

# Decorator to open and close DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query in query_cache:
            print("[LOG] Returning cached result for query.")
            return query_cache[query]
        else:
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
            print("[LOG] Caching result for query.")
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users_again)
# This script fetches users from the database and caches the results.
# It uses decorators to manage database connections and caching, ensuring that repeated queries return cached results.