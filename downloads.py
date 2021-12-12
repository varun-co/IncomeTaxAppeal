from os import wait
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import sqlite3
import time
import random
try:
    conn = sqlite3.connect('IncomeTaxAppeal.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS APPEALDETAILS (
        SN0 INTEGER PRIMARY KEY AUTOINCREMENT,
        BENCH TEXT,
        BENCH_ALLOTED TEXT,
        APPEAL_NUMBER TEXT,
        ORDER_TYPE TEXT,
        ORDER_DATE TEXT,
        FILED_ON TEXT,
        ASSESSMENT_YEAR TEXT,
        PRONUCED_DATE TEXT,
        RESULTS TEXT,
        ORDER_LINK TEXT,
        STATUS TEXT
        )
        ''')
    conn.commit()
    fhandle = open('bench.txt',mode = 'r+')
    driver = webdriver.Firefox('/home/varun/geckodriver-v0.29.1-linux32')
    blines = fhandle.read().split()
    bench = blines[0]
    fhandle2 = open(bench + '.txt',mode = 'r+')
    llines = fhandle2.read().split()
    url = llines[1]
    judicialtribunal = driver.get(url)
    date = WebDriverWait(driver,120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[2]'))).text
    ordertype = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[1]').text
    pronouncedon = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[3]').text
    results = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[5]').text
    status = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[7]').text
    appeleant = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[7]/td[1]').text
    respondent = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[7]/td[2]').text
    appealnumber = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[5]/td[1]').text
    filledon = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[5]/td[2]').text
    assesemnt_year = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[5]/td[3]').text
    benchalloted = driver.find_element_by_xpath('/html/body/div/main/div/div/table/tbody/tr[5]/td[4]').text
    try:
        link = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[5]/div/table/tbody/tr[2]/td[6]/a')
        link = link.get_attribute('href')
    except:
        link = ' '
    #print(date,ordertype,pronouncedon,results,status,appeleant,respondent)
    #print(appealnumber,assesemnt_year,benchalloted,link)
    if date >= '2020-03-15':
        ptr = '''INSERT INTO APPEALDETAILS 
        (APPEAL_NUMBER,FILED_ON,ASSESSMENT_YEAR,BENCH,BENCH_ALLOTED
        ,ORDER_TYPE,ORDER_DATE,PRONUCED_DATE,RESULTS,ORDER_LINK,STATUS)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(ptr,[appealnumber,filledon,assesemnt_year,bench,benchalloted,ordertype,date  ,pronouncedon,results,link,status])
        conn.commit()
        conn.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        llines.remove(url)
        fhandle2.seek(0)
        fhandle2.truncate()
        fhandle3 = open('Dounloads.txt',mode='a')
        fhandle3.write(url+'\n')
        fhandle3.close()
        for line in llines:                                                                                                                                                                     
            fhandle2.write(line+'\n')
        fhandle2.close()

    else:
        blines.remove(bench)
        fhandle2.seek(0)
        fhandle2.truncate()
        fhandle.truncate()
        for line in blines:
            fhandle.write(line+'\n')
        fhandle.close()
except:
    print('error')
time.sleep(5)
driver.quit()
