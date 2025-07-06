import mysql.connector

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',      # Replace with your MySQL username
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_users_in_batches(batch_size):
    """Generator that fetches rows from user_data in batches."""
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)

    offset = 0
    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """Generator that processes batches and yields users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_users = (user for user in batch if user['age'] > 25)
        for user in filtered_users:
            yield user

# Example usage:
if __name__ == "__main__":
    for user in batch_processing(10):
        print(user)
#     conn = connect_to_prodev()