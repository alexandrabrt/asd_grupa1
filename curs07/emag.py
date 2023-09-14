from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas

option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver.get('https://www.emag.ro/#opensearch')
get_element = driver.find_element(by=By.ID, value='searchboxTrigger')


def search_product(product):
    get_element.send_keys(product)
    get_element.submit()
    url = requests.get(driver.current_url)
    page = BeautifulSoup(url.text, 'html.parser')
    print(page)
    counter = 1
    data = {}
    for i in page.find_all('div', attrs={'class': 'card-v2-wrapper'}):
        product_name = i.find('a', attrs={'class': 'card-v2-title'}).get_text()
        counter += 1
        data[f"product_{counter}"] = {'product_name': product_name}

    pandas.DataFrame(data).transpose().to_csv(f"{product.title()}.csv", header=['Product name'])
    return data


search_product('telefon')
