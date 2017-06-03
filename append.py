from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
#Appending List of titles
num = 0
needNum = 0

def appendList(textList, browser):
    global num
    count = 0
    ids = browser.find_elements_by_class_name('hacktivity__link')
    #print("ids going in:", ids)
    for ii in ids:
        findIfPaid(ii)
        count = count +1
        num = num + 1
        #append ii.Text_name to our list.
        word = ii.get_attribute('innerHTML')
        #print("about to append")
        textList.append(word)
    #print("textlist before clean:",textList)
    textList = [x for x in textList if x is not None]
    #print("textList going out:",textList)
    return num



def findIfPaid(browser):
    print("wait I should hve gotten a new ii",num)
    time.sleep(2)
    link = browser
    try:
        link.find_element_by_class_name('spec-hacktivity-item-bounty')
        link2 =  link.find_element_by_class_name('spec-hacktivity-item-bounty')
        print(link.get_attribute('outerHTML'))
        print(link2.get_attribute('outerHTML'))
        time.sleep(2)
    except NoSuchElementException:
        print("okay on to the next one")
    #print(link.get_attribute('innerHTML'))
    #link.click()
    #browser.get(previousPage)
    #time.sleep(2)
    #print(link.get_attribute('text'))
