import csv

# masini = [
#     ['Dacia', 'Logan', 2005, 75],
#     ['Renault', 'Clio', 2005, 90]
# ]

# with open('data.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for masina in masini:
#         csv_writer.writerow(masina)

with open('data.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row)
