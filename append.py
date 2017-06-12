from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import operator
#Appending List of titles
num = 0
needNum = 0
paidReportsList = []
geTenThou = 0
leOneHun = 0
def appendList(hrefList, browser, titleList,count):
    global num
    
    ids = browser.find_elements_by_class_name('hacktivity__link')
    for ii in ids:
        word= ii.get_attribute('href')
        hrefList.append(word)
        count = count +1
        num = num + 1
        title = ii.get_attribute('innerHTML')
        titleList.append(title)
    return hrefList, browser, titleList, count




    #****WHILE LOOP ITTERATING LISTS**********
    #
    #size = len(hrefList)
    #i = 0
    #while i < size:
    #    print(titleList[i])
    #    print(hrefList[i])
    #    i = i +1
    #
    #
    #print(hrefList)
    #print("textlist before clean:",textList)
    #textList = [x for x in textList if x is not None]
    #print("textList going out:",textList)


def findIfPaid(linkList, nonePaidReports,browser,disclosed):
    size = len(linkList)
    i = 0
    
    while i < size:
        #print(titleList[i])
        #print(hrefList[i])
        browser.get(linkList[i])
        time.sleep(3)
        try:
            link =  browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/table[1]/tbody/tr[5]/td[2]').get_attribute('innerHTML')
            bountyNumber = link.replace('$','').replace(',','')
            #print(bountyNumber)
            try:
                int(bountyNumber)
                if operator.ge(int(bountyNumber),10000):
                    #save to equal or above 10000
                    geTenThou = geTenThou + 1
                    i = i + 1
                if operator.le(int(bountyNumber),100):
                    #save to equal or above 100
                    leOneHun = leOneHun + 1
                    i = i + 1
                insertPaidReports(paidReportsList,bountyNumber,linkList)
                i = i + 1
                print(paidReportsList)
            except ValueError:
                print("sorry this wasnt a number, let me check 1 more spot\n")
                try:
                    link =  browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/table[1]/tbody/tr[6]/td[2]').get_attribute('innerHTML')
                    bountyNumber =   link.replace('$','').replace(',','') 
                    if operator.ge(int(bountyNumber),10000):
                        #save to equal or above 10000
                        geTenThou = geTenThou + 1
                        i = i + 1
                    if operator.le(int(bountyNumber),100):
                        #save to equal or above 100
                        leOneHun = leOneHun + 1
                        i = i + 1
                except NoSuchElementException:
                    #TODO:put in unknown.txt file
                    with open('unknown.txt', 'a+') as f:
                        f.write("The URL :")
                        f.write(browser.current_url)
                        f.write("\n")
                    i = i +1
        except NoSuchElementException:
            with open('notPaidReports.txt', 'a+') as f:
                f.write("The URL :")
                f.write(browser.current_url)
                f.write("\n")
            nonePaidReports = nonePaidReports + 1
            i = i + 1
            #TODO: count number of non paid disclosed reports
            #print("okay on to the next one")
    return nonePaidReports, top200
    #print(link.get_attribute('innerHTML'))
    #link.click()
    #browser.get(previousPage)
    #time.sleep(2)
    #print(link.get_attribute('text'))


def insertPaidReports(paidReportsList, bountyNumber,linkList):
    if not paidReportsList:
        paidReportsList = [bountyNumber]
        print(paidReportsList)
    return paidReportsList
