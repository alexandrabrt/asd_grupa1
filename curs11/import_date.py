import pandas
import mysql.connector


df = pandas.read_csv("date_clienti.csv",
                     header=None)
                     # names=["Companie", "Adresa", "Oras", "Cod postal", "Tara"])
data_list = []
for item, row in df.iterrows():
    # print(row.tolist())
    # customer_value = df.iloc[item, 0]
    # address_value = df.iloc[item, 1]
    # city_value = df.iloc[item, 2]
    # postal_code_value = df.iloc[item, 3]
    # country_value = df.iloc[item, 4]
    # data_list.append((customer_value, address_value, city_value, int(postal_code_value), country_value))
    data_list.append(row.tolist())

print(data_list)
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa1ASD'
)
cursor = my_db.cursor()
sql = "INSERT INTO customers (name, address, city, postal_code, country) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(sql, data_list)
my_db.commit()
