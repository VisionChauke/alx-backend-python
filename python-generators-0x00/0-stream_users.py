import mysql.connector

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',      # Replace with your MySQL username
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_users():
    """Generator function that streams user_data rows one by one."""
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)  # dictionary=True for dict rows

    cursor.execute("SELECT * FROM user_data")

    # Using a single loop with fetchone() to yield rows one at a time
    row = cursor.fetchone()
    while row:
        yield row
        row = cursor.fetchone()

    cursor.close()
    conn.close()


# Example usage
if __name__ == "__main__":
    for user in stream_users():
        print(user)
