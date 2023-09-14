from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas


option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('https://www.bnr.ro/files/xml/nbrfxrates2022.htm')
table = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
lista = table.text.split('\n')
# print(lista)
header_len = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
# print(header)
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + j, len(lista), len(header)):
        dictionar[header[j]].append(lista[i])
print(dictionar)
df = pandas.DataFrame(dictionar)
df.to_csv('bnr_all_data.csv')



