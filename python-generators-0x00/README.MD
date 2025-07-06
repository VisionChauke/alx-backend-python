# ALX ProDev MySQL Seeder

This project sets up a MySQL database and populates it with user data from a CSV file using Python.

## Features

Connects to MySQL server and creates a database ALX_prodev if it doesn’t exist.

Creates a table user_data with fields:

- user_id (UUID, Primary Key, Indexed)
- name (VARCHAR, NOT NULL)
- email (VARCHAR, NOT NULL)
- age (DECIMAL, NOT NULL)

Reads user data from user_data.csv and inserts it into the database.

Ensures no duplicate emails are inserted.

## Prerequisites

- Python 3.x
- MySQL Server running locally or accessible remotely
- Python packages:
  - mysql-connector-python
  - pandas

Install the required packages with:

License
MIT License
