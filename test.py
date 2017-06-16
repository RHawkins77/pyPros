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

browser.get('https://hackerone.com/reports/85201')
try:
    link = browser.find_element_by_class_name('report-heading__report-title spec-report-title').get_attribute('text')
    print(link)
except NoSuchElementException:
    print("oh no!!!")


link = "$"
with open('TESTER.txt', 'a+') as f:
    f.write("hello"+link+"fuckin a")
