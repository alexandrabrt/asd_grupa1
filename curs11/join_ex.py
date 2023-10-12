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
                   "order_date DATE,"
                   ")")
except mysql.connector.errors.ProgrammingError:
    pass

try:
    cursor.execute("ALTER TABLE orders MODIFY COLUMN customer_id INT NOT NULL")
except mysql.connector.errors.ProgrammingError:
    pass
try:
    cursor.execute("ALTER TABLE orders ADD CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES customers (id);")
except (mysql.connector.errors.IntegrityError, mysql.connector.errors.ProgrammingError):
    pass

# sql = "INSERT INTO customers (name, address, city, postal_code, country) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     ('ABC SRL', "Mihai Bravu 4", 'Bucuresti', 25, "Romania"),
#     ('XYZ SRL', "Stefan cel Mate 3", 'Craiova', 2334, "Romania"),
#     ('QWE SRL', "Mihai Eminescu 2", 'Bucuresti', 43546, "Romania"),
# ]
# cursor.executemany(sql, val)
# my_db.commit()
# sql = "INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)"
# val = [
#     (1, '2023-10-12'),
#     (1, '2023-10-09'),
#     (2, '2023-10-10'),
#     (2, '2023-10-08'),
#     (3, '2023-10-07'),
#     (3, '2023-10-12'),
# ]
# cursor.executemany(sql, val)
# my_db.commit()

cursor.execute("SELECT * FROM customers c JOIN orders o ON c.id=o.customer_id")
print(cursor.fetchall())
