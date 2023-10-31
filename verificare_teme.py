import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

lista_mare_cazuri = []


def culegere_date_covid(link, id):
    option = webdriver.ChromeOptions()
    option.add_argument('start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(link)
    popup_button = driver.find_element(by=By.CLASS_NAME, value='swal2-close')
    popup_button.click()
    time.sleep(3)
    table = driver.find_element(by=By.XPATH, value=id)
    lista = table.text.split('\n')
    lista_numar = []
    lista_judet = []
    lista_cazuri = []
    lista.pop(0)

    for element in range(43):
        element_listat = lista[element].split()
        lista_numar.append(element_listat[0])
        try:
            element_provizoriu = float(element_listat[2])
            lista_judet.append(element_listat[1])
            lista_cazuri.append(element_listat[2])
        except:
            judet = element_listat[1] + " " + element_listat[2]
            lista_judet.append(judet)
            lista_cazuri.append(element_listat[3])

    rezultat = (lista_numar, lista_judet, lista_cazuri)
    return rezultat


links = ['https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/',
         'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/',
         'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/',
         'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-3/',
         'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/']

ids = ['//*[@id="post-29587"]/div/div/table[1]',
       '//*[@id="post-29627"]/div/div/table[1]',
       '//*[@id="post-29664"]/div/div/table[1]',
       '//*[@id="post-29690"]/div/div/table[1]',
       '//*[@id="post-29726"]/div/div/table[1]']




def get_values_from_link(link: str) -> (list, list, list):
    rezultat = culegere_date_covid(link, ids)
    lista_numar = rezultat[0]
    lista_judete = rezultat[1]
    lista_cazuri = rezultat[2]
    lista_mare_cazuri.append(lista_cazuri)
    return lista_numar, lista_judete, lista_mare_cazuri

for i in range(len(links)):
    get_values_from_link(i)
print(lista_numar)
print(lista_judete)
print(lista_mare_cazuri)


with open('date_covid.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nr.Crt.", "Judet", "01.03", "02.03", "03.03", "04.03", "05.03"])

    for rand in zip(lista_numar, lista_judete, lista_mare_cazuri[0], lista_mare_cazuri[1], lista_mare_cazuri[2], lista_mare_cazuri[3], lista_mare_cazuri[4]):
        writer.writerow(rand)

