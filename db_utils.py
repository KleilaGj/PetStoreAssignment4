import mysql.connector

# Connect to SQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database_name'
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to execute an SQL query
def execute_query(connection, query, data=None):
    try:
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.e
