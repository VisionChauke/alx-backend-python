import mysql.connector
import pandas as pd
import uuid

def connect_db():
    """Connects to the MySQL server (no database selected yet)."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',  # replace with your MySQL username
        password='your_password'  # replace with your MySQL password
    )

def create_database(connection):
    """Creates the ALX_prodev database if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    """Connects specifically to the ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='your_username',  # replace with your MySQL username
        password='your_password',  # replace with your MySQL password
        database='ALX_prodev'
    )

def create_table(connection):
    """Creates the user_data table if it does not exist with the specified schema."""
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL,
        INDEX idx_user_id (user_id)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def insert_data(connection, data):
    """Inserts data into user_data table if the user_id does not exist."""
    cursor = connection.cursor()
    for _, row in data.iterrows():
        user_id = str(uuid.uuid4())
        name = row['name']
        email = row['email']
        age = row['age']

        # Check if email already exists (to avoid duplicates)
        cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (email,))
        (count,) = cursor.fetchone()
        if count == 0:
            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (user_id, name, email, age)
            )
    connection.commit()
    cursor.close()

def main():
    # Step 1: Connect to MySQL server (no DB)
    conn = connect_db()
    create_database(conn)
    conn.close()

    # Step 2: Connect to ALX_prodev database
    conn_prodev = connect_to_prodev()
    create_table(conn_prodev)

    # Step 3: Load CSV data
    data = pd.read_csv('user_data.csv')

    # Step 4: Insert data
    insert_data(conn_prodev, data)
    conn_prodev.close()
    print("Database and table setup complete, data inserted.")

if __name__ == "__main__":
    main()
