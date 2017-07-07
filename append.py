from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import operator
#Appending List of titles
num = 0
needNum = 0
nonePaidReports = 0

def appendList(hrefList, browser, titleList,count): 
    ids = browser.find_elements_by_class_name('hacktivity__link')
    for ii in ids:
        hrefWord= ii.get_attribute('href')
        titleWords = ii.get_attribute('text')
        hrefList.append(hrefWord)
        count = count + 1
        titleList.append(titleWords)
    #print(len(hrefList))
    return hrefList, browser, titleList, count



def findIfPaid(linkList, titleList, bountyPriceList,disclosed,spot,geTenThou,leOneHun):
    size = len(linkList)
    i =0
    broken = 0
    print(len(linkList))
    global nonePaidReports
        #print(titleList[i])
        #print(hrefList[i])
    while i < size:
        browser = webdriver.Firefox()
        try:
            browser.get(linkList[i])
            j = 1
            time.sleep(3)
            while j < 12:
                try:
                    #print(j)
                    bountyChecker = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/table[1]/tbody/tr[%d]/td[1]' % j).get_attribute('innerHTML')
                    if "bounty" in bountyChecker.lower():
                        try:
                            link =  browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/table[1]/tbody/tr[%d]/td[2]' % j).get_attribute('innerHTML')
                            bountyNumber = link.replace('$','').replace(',','')
                            #print(link)
                            geTenThou, leOneHun = sizeChecker(geTenThou, leOneHun, bountyNumber)
                            bountyPriceList, spot = insertPaidReports(bountyPriceList,bountyNumber,linkList,i,spot)
                            #print("EVERYTHING WENT PERFECT WE ADDED")
                            browser.quit()
                            i = i + 1
                            break
                        except NoSuchElementException:
                            print("DURING THE PROCESS WE FOUND A BOUNTY TAG BUT NO MATCHING PRICE TAG")
                    else:
                        j = j + 1
                except NoSuchElementException:
                    #print("but got back here again")
                    nonePaidReports = nonePaidReports + 1
                    writeToUnpaid(browser, titleList, i)
                    #print("WE HAVE A NONEPAID REPORT HERE")
                    #print(j)
                    browser.quit()
                    i = i + 1
                    break
        except TimeoutException:
            broken = 1
            return broken, bountyPriceList, spot, nonePaidReports, geTenThou, leOneHun 
    return broken, bountyPriceList, spot, nonePaidReports, geTenThou, leOneHun 


def sizeChecker(tenThou, oneHun,bountyNum):
    if operator.ge(float(bountyNum),10000):
        #save to equal or above 10000
        tenThou = tenThou + 1
    if operator.le(float(bountyNum),100):
        #save to equal or above 100
        oneHun = oneHun + 1
    return tenThou, oneHun

def writeToUnpaid(browser, givenTitleList, ourI):
    with open('unpaidReports.txt', 'a+') as f:
        f.write(givenTitleList[ourI].encode('utf-8'))
        f.write("\n")
        f.write("The URL:")
        f.write(browser.current_url)
        f.write("\n")

def insertPaidReports(bountyPriceList, bountyNumber,linkList, listSpot,spot):
    if bountyPriceList:
        #print("I am in the previous paidreportslist")
        i = 0
        size = len(bountyPriceList)
    #if not bountyPriceList:
        #print("I started a new report list")
        #print(bountyPriceList)
    bountyPriceList.append(bountyNumber)
    spot.append(listSpot)
    #print(spot)
    return bountyPriceList, spot
