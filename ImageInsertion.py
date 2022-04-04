import mysql.connector
import base64
from PIL import Image
import io

my_db = mysql.connector.connect(
    host='localhost',  # HostName goes in this variable.
    user='root',  # UserName goes in this variable.
    password='Chopras1!',  # Password for the MySQL connection.
    port='3306',  # Port number for the database connection.
    database='studentdb'  # Name of the new database created.
)

my_cursor = my_db.cursor()

# Open a file in binary mode
file = open('C:/Users/Harman/OneDrive/Pictures/Screenshots/Screenshot.png', 'rb').read()

# We must encode the file to get base64 string
file = base64.b64encode(file)

# Sample data to be inserted
args = ('200', 'Sample Name', file)

# Prepare a query
query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'    # PROFILE is the table in the new database

# Execute the query and commit the database.
my_cursor.execute(query, args)
my_db.commit()
