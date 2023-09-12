from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
link = BeautifulSoup(r.text, 'html.parser')
title = link.find_all('div', attrs={'class': 'contentDiv'})[0]
dataset = []
# header = []
for tr_index in title.find_all('table'):
    for td_index in tr_index.find_all('tr'):
        td_list = []
        if td_index.find_all('th'):
            # for th_index in td_index.find_all('th'):
            #     header.append(th_index.get_text())
            header = [th_index.get_text() for th_index in td_index.find_all('th')]
            dataset.append(header)
        else:
            for index, td_value in enumerate(td_index.find_all('td')):
                print(index, td_value)
                if index == 0:
                    td_list.append(td_value.get_text())
                else:
                    # if td_value.get_text().strip() != '':
                    #     td_list.append(float(td_value.get_text().strip().replace(',', '.')))
                    # else:
                    #     td_list.append('')
                    td_list.append(float(td_value.get_text().strip().replace(',', '.')) if td_value.get_text().strip() != '' else '')
            dataset.append(td_list)
print(dataset)
with open('bnr_data.csv', 'w', newline='') as file:
    variabila = csv.writer(file)
    variabila.writerows(dataset)

