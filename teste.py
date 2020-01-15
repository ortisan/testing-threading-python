from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import random
import time
from datetime import datetime


def execute(x):
    inicio = datetime.now()
    wait = random.randint(0, 10)
    time.sleep(wait)

    fim = datetime.now()
    print(x, wait, inicio, fim-inicio)


xpto = [1, 2, 3, 4, 5, 6, 7]


with ProcessPoolExecutor(max_workers=4) as e:
    e.map(execute, xpto)

urls = ['https://finance.yahoo.com/quote/ITUB?p=ITUB',
        'https://finance.yahoo.com/quote/BAC?p=BAC',
        'https://finance.yahoo.com/quote/NIO?p=NIO',
        'https://finance.yahoo.com/quote/WFC?p=WFC',
        'https://finance.yahoo.com/quote/BYND?p=BYND',
        'https://finance.yahoo.com/quote/GE?p=GE',
        'https://finance.yahoo.com/quote/AAPL?p=AAPL']


def scrap_title(url):
    print('URL: ', url)
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    print('TITLE: ', driver.title)
    driver.close()

# with ThreadPoolExecutor(max_workers=2) as e:
with ProcessPoolExecutor(max_workers=2) as e:
    e.map(scrap_title, urls)
