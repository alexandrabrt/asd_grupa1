import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa1ASD'
)
cursor = my_db.cursor()
try:
    cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
                   'name VARCHAR(255) ,'
                   'address VARCHAR(255),'
                   'project_number INT)')
except mysql.connector.errors.ProgrammingError:
    pass

try:
    # cursor.execute('ALTER TABLE projects ADD COLUMN age INT')
    cursor.execute('ALTER TABLE projects ADD COLUMN varsta INT')
except mysql.connector.errors.ProgrammingError:
    pass
try:
    cursor.execute('ALTER TABLE projects DROP COLUMN age')
except mysql.connector.errors.ProgrammingError:
    pass
# try:
#     cursor.execute('ALTER TABLE projects RENAME COLUMN age TO varsta')
# except mysql.connector.errors.ProgrammingError:
#     pass

# sql = "INSERT INTO projects (name, address, varsta, project_number) VALUES (%s, %s, %s, %s)"
# val = [
#     ('Petre', 'Bucuresti', 25, 123),
#     ('Amalia', 'Ploiesti', 20, 321),
#     ('Mihai', 'Bacau', 35, 224)
# ]
# cursor.executemany(sql, val)
# my_db.commit()

# sql = "UPDATE projects SET address='Bucuresti' where address='Ploiesti' and name='Amalia'"
sql = "UPDATE projects SET address='Bucuresti' where id=2"
cursor.execute(sql)
my_db.commit()
