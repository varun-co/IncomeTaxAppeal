from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def scrapper():
    driver = webdriver.Firefox()
    url = 'https://selenium-python.readthedocs.io/getting-started.html'
    driver.get(url)
    time.sleep(5)
    driver.close()
scrapper()
