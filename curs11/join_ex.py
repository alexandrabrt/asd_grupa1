import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa1ASD'
)
cursor = my_db.cursor()
try:
    cursor.execute("CREATE TABLE customers ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "name VARCHAR(200) NOT NULL,"
                   "address VARCHAR(300),"
                   "city VARCHAR(50),"
                   "postal_code INT,"
                   "country varchar(70))")
except mysql.connector.errors.ProgrammingError:
    pass
try:
    cursor.execute("CREATE TABLE orders ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "customer_id INT,"
                   "order_date DATE"
                   ")")
except mysql.connector.errors.ProgrammingError:
    pass


