import mysql.connector

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',      # Replace with your MySQL username
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def paginate_users(page_size, offset):
    """Fetch a page of users from user_data table."""
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

def lazy_paginate(page_size):
    """Generator that lazily fetches pages of users."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

# Example usage
if __name__ == "__main__":
    for page in lazy_paginate(5):
        print(f"Page of {len(page)} users:")
        for user in page:
            print(user)
        print("---")
