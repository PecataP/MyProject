import sqlite3


def create_database():
    # Connect to or create the database
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                 id INTEGER PRIMARY KEY,
                 name VARCHAR(20) NOT NULL CHECK(name GLOB '[A-Za-z]*'),
                 surname VARCHAR(20) NOT NULL CHECK(surname GLOB '[A-Za-z]*'),
                 position VARCHAR(40) NOT NULL CHECK(position GLOB '[A-Za-z]*'),
                 phone INTEGER NOT NULL,
                 email VARCHAR(30) NOT NULL
                 )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


def insert_data(name, surname, position, phone, email):
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # Insert a new row into the table
    c.execute('''INSERT INTO employees (name, surname, position, phone, email)
                 VALUES (?, ?, ?, ?, ?)''',
              (name, surname, position, phone, email))

    # Commit changes and close connection
    conn.commit()
    conn.close()


def clear_database():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # Delete all rows from the table
    c.execute('''DELETE FROM employees''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Create the database and table
    create_database()
    print("Database 'employees' and table 'employees' created successfully.")

    clear_database()
    print("Database cleared successfully.")

    # Example data with mandatory fields only
    mandatory_data = {
        "name": "Jack",
        "surname": "Jones",
        "position": "mf",
        "phone": "+31696969690",
        "email": "jack@gmail.com"
    }

    # Insert data into the database
    insert_data(**mandatory_data)
    print("Data inserted successfully.")
