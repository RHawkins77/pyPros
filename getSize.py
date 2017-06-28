from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from append import findIfPaid
from append import appendList
from order import orderList
from createList import writeList
from createList import writeLastList

import time  



def numberOfReports(browser, linkList, titleList, number):
    while True:
        try:
            time.sleep(3)
            #print("fuck this dude")
            myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
            #myButton2 = browser2.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
            #linkList, browser, titleList, number = appendList(linkList,browser,titleList,number)
            #linkList2, browser2, _, _ = appendList(linkList2, browser2, titleList, number)
            #print("inside 1st try")
            #myButton2.click()
            myButton.click()
        except NoSuchElementException:
            #print("im not skipping")
            time.sleep(4)
            link = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[23]/div[1]/div[1]').get_attribute('innerHTML')
            print(link)

            #linkList2, browser2, _, _ = appendList(linkList2, browser2, titleList, number)
            #linkList, browser, titleList, number = appendList(linkList,browser,titleList,number)
            #print(textList)
            break
    return browser, linkList, titleList, number
   
