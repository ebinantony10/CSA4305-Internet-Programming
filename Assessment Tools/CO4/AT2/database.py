import sqlite3

# Connect to database
try:
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    print("Database connected successfully")

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER,
            name TEXT,
            email TEXT
        )
    """)

    # Insert sample records
    cursor.execute("DELETE FROM students")

    cursor.execute(
        "INSERT INTO students VALUES (101, 'John', 'john@gmail.com')"
    )

    cursor.execute(
        "INSERT INTO students VALUES (102, 'David', 'david@gmail.com')"
    )

    conn.commit()

    # Execute SELECT query
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    # Display records
    if len(records) == 0:
        print("No records found")
    else:
        print("\nStudent Records")
        print("----------------")

        for record in records:
            print("ID    :", record[0])
            print("Name  :", record[1])
            print("Email :", record[2])
            print()

    # Close resources
    cursor.close()
    conn.close()

except sqlite3.Error as e:
    print("Database connection failed")
    print(e)