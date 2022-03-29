import mysql.connector
import base64
from PIL import Image
import io

my_db = mysql.connector.connect(
    host='',  # HostName goes in this variable.
    user='',  # UserName goes in this variable.
    password='',  # Password for the MySQL connection.
    port='',  # Port number for the database connection.
    database=''  # Name of the new database created.
)

my_cursor = my_db.cursor()

# Open a file in binary mode
file = open('Image_Name', 'rb').read()

# We must encode the file to get base64 string
file = base64.b64encode(file)

# Sample data to be inserted
args = ('100', 'Sample Name', file)

# Prepare a query
query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'    # PROFILE is the table in the new database

# Execute the query and commit the database.
my_cursor.execute(query, args)
my_db.commit()
