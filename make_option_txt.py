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
import itertools
fhandle = open('bench.txt',mode = 'r')
driver = webdriver.Firefox()
url = 'https://www.itat.gov.in/judicial/tribunalorders'
judicialtribunal = driver.get(url)
bench = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'bench')))
bench = Select(bench)
search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button')))
lines = fhandle.read().split()
fhandle.close()
for s in range(len(lines)):
    fhandle = open('bench.txt',mode = 'r')
    lines = fhandle.read().split()
    a = lines[0]
    bench = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'bench')))
    bench = Select(bench)
    search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button')))
    bench.select_by_visible_text(a)
    time.sleep(0.5)
    search.click()
    try:
        details = WebDriverWait(driver,120).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'Details')))
    except:
        try:
            bench = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'bench')))
            bench = Select(bench)
        except:
            fhandle3 = open('failure.txt',mode = 'w')
            fhandle3.write(a+'\n')
            fhandle3.close()
            driver.back()
        fhandle.close()
        fhandle = open('bench.txt',mode = 'a')
        lines.remove(a)
        for line in lines:
            fhandle.write(line+'\n')
        fhandle.close()
        fhandletemp = open(a+'.txt',mode = 'w')
        fhandletemp.close()
        continue
    details.pop(0)
    fhandletemp = open(a+'.txt',mode = 'w')
    for element in details:
        link = element.get_attribute('href')
        fhandletemp.write(link+'\n')
    fhandletemp.close()
    fhandle.close()
    fhandle = open('bench.txt',mode = 'w')
    lines.remove(a)
    for line in lines:
        fhandle.write(line+'\n')
    fhandle.close()
    time.sleep(10)
    driver.back()
time.sleep(5)
fhandle3.close()
driver.quit()