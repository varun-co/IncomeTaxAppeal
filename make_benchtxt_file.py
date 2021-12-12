from os import wait
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
import random
from selenium.webdriver.firefox.options import Options
def get_benches_from_benchtxt():
    try:
        fhandle = open('bench.txt',mode='r')
        bench = fhandle.read().splitlines()
        return bench
    except:
        print('unable to open bench.txt please check if file exists')
def get_benches():
    driver = webdriver.Firefox()
    option = Options()
    option.headless = True
    url = 'https://www.itat.gov.in/judicial/tribunalorders'
    judicialtribunal = driver.get(url)
    try:
        orderdate = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div/section[2]/p/label'))).click()
        bench = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,'bench2')))
    except:
        print('website is currently down or webiste is changed')
        print('trying to fetch from a local file ')
        print('WARNING this file might contain outadated bench information please use it wisely')
        bench = get_benches_from_benchtxt()
        return bench
    bench = Select(bench)
    opt = bench.options
    opt = [i.text  for i in opt]
    opt.pop(0)
    driver.quit()
    return opt

