import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123"
)

# Create a cursor object
my_cursor = mydb.cursor()

# Try to drop the database if it exists
my_cursor.execute("DROP DATABASE IF EXISTS saborealestate")

# Create the database
my_cursor.execute("CREATE DATABASE saborealestate")
print("Database 'saborealestate' created successfully.")

# Close the cursor and connection
my_cursor.close()
mydb.close()
