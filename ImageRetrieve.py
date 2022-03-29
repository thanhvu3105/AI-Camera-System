import mysql.connector
import base64
from PIL import Image
import io

mydb = mysql.connector.connect(
    host='',  # HostName goes in this variable.
    user='',  # UserName goes in this variable.
    password='',  # Password for the MySQL connection.
    port='',  # Port number for the database connection.
    database=''  # Name of the new database created.
)
cursor = mydb.cursor()

# Prepare the query
query = 'SELECT PICTURE FROM PROFILE WHERE ID=100'   # Sample Query

# Execute the query to get the file
cursor.execute(query)

data = cursor.fetchall()

# The returned data will be a list of list
image = data[0][0]

# Decode the string
binary_data = base64.b64decode(image)

# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))

# Display the image
image.show()