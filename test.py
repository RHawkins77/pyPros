from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from append import appendList
from append import findIfPaid
import time  

browser = webdriver.Firefox()

browser.get('https://hackerone.com/reports/124100')

time.sleep(3)
try:
    link = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]')
    link2 =  browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/table[1]/tbody/tr[5]/td[2]').get_attribute('innerHTML')
    print(link)
    print(link2)
except NoSuchElementException:
    print("aint here yo!")
