import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
print(my_db)
cursor = my_db.cursor()
try:
    cursor.execute("CREATE DATABASE grupa1ASD")
except mysql.connector.errors.DatabaseError:
    pass
cursor.execute('SHOW DATABASES')
for item in cursor:
    print(item)
