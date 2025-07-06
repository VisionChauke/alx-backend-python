import mysql.connector

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',      # Replace with your MySQL username
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    row = cursor.fetchone()
    while row:
        yield row['age']
        row = cursor.fetchone()

    cursor.close()
    conn.close()

def calculate_average_age():
    """Calculates average age using the age generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():  # Loop 1: iterate generator
        total_age += age
        count += 1
    average_age = total_age / count if count > 0 else 0
    return average_age

if __name__ == "__main__":
    avg_age = calculate_average_age()
    print(f"Average age of users: {avg_age:.2f}")
# This script connects to the ALX_prodev database, streams user ages from the user_data table,
# and calculates the average age of users. The average is printed with two decimal places.