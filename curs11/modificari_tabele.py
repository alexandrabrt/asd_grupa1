import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa1ASD'
)
cursor = my_db.cursor()
# cursor.execute("SHOW TABLES")
# print(cursor.fetchall())
# print(list(cursor))
# cursor.execute('SELECT * FROM projects')
# cursor.execute('SELECT id, name, address FROM projects WHERE address="Bacau" AND project_number=224')
# cursor.execute('SELECT id, name, address, varsta FROM projects WHERE address="Bacau" OR address="Bucuresti" ORDER BY varsta DESC')
# result = cursor.fetchall()
# print(result)
# for i in result:
#     print(i)
# result = []
# for row in cursor.fetchall():
#     dictionary = {}
#     for i, value in enumerate(row):
#         print(cursor.description[i][0])
        # dictionary.update({cursor.description[i][0]: value})
    # result.append(dictionary)
# result = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
# for i in result:
#     print(i['address'])

# cursor.execute("DELETE FROM projects WHERE project_number=224")
cursor.execute('SELECT * FROM projects WHERE project_number IN (123, 321)')
print(cursor.fetchall())
# my_db.commit()
