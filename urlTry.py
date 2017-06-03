from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from append import appendList
import time  

num = 0
sqlCount = 0
XSSCount = 0
XXECount = 0
HTMLCount = 0
HTMLXSSCount = 0
CSRFCount = 0
HTTPCount =0
SSRFCount = 0
XMLCount = 0
COOKIEVULN = 0
OPRED = 0
AUTHVULN = 0
RCEVULN = 0
textList = []

browser = webdriver.Firefox()  
#get hackerone disclosed hacktivity page
browser.get('https://hackerone.com/hacktivity?sort_type=upvotes&filter=type%3Apublic&page=146&range=forever')  
time.sleep(2)
print("Please wait while we look for the Results you have Requested")

def vulnCounter(textList):
    global sqlCount
    global XSSCount
    global XXECount
    global HTMLCount
    global HTMLXSSCount
    global CSRFCount
    global HTTPCount
    global SSRFCount
    global COOKIEVULN
    global OPRED
    global AUTHVULN
    global RCEVULN
    global XMLCount
    textList = [x for x in textList if x is not None]
    length = len(textList)
    i = 0
    for i in range(length):
        if "sql" in textList[i].lower():
            sqlCount = sqlCount + 1
        if "csrf" in textList[i].lower():
            CSRFCount = CSRFCount + 1
        if "xss" in textList[i].lower() or "cross-site scripting" in textList[i].lower() or "cross site scripting" in textList[i].lower():
            if "html" in textList[i].lower() and "xss" in textList[i].lower():
                continue
            else:
                 #print(textList[i])
                 #print(textList[i].lower())
                 XSSCount = XSSCount + 1
        if "xml" in textList[i].lower():
            XMLCount = XMLCount + 1
        if "xxe" in textList[i].lower():
            XXECount = XXECount + 1
        if "html" in textList[i].lower() and "xss" in textList[i].lower():
            HTMLXSSCount = HTMLXSSCount + 1
        if "http" in textList[i].lower():
            HTTPCount = HTTPCount + 1
        if "ssrf" in textList[i].lower():
            SSRFCount = SSRFCount + 1
        if "cookie" in textList[i].lower():
            COOKIEVULN = COOKIEVULN + 1
        if "open redirect" in textList[i].lower() or "open-redirect" in textList[i].lower():
            OPRED = OPRED + 1
        if "auth" in textList[i].lower():
            AUTHVULN = AUTHVULN + 1
        if "rce" in textList[i].lower() or "remote code execution" in textList[i].lower():
            RCEVULN = RCEVULN + 1
        i = i + 1

while True:
    try:
        time.sleep(2)
        #print("fuck this dude")
        myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
        appendList(textList,browser)
        #print("inside 1st try")
        myButton.click()
    except NoSuchElementException:
        #print("im not skipping")
        time.sleep(2)
        #print("im where I should be")
        number = appendList(textList,browser)
        #print(textList)
        break
    #print("I skipped?")
vulnCounter(textList)

with open('Count.txt', 'a+') as f:
    f.write("SQL Count: ")
    f.write(str(sqlCount))
    f.write("\n")
    f.write("CSRF Count: ")
    f.write(str(CSRFCount))
    f.write("\n")
    f.write("xml count: ")
    f.write(str(XMLCount))
    f.write("\n")
    f.write("HTTP Count: ")
    f.write(str(HTTPCount))
    f.write("\n")
    f.write("SSRF Count: ")
    f.write(str(SSRFCount))
    f.write("\n")
    f.write("XXE Count: ")
    f.write(str(XXECount))
    f.write("\n")
    f.write("XSS Count: ")
    f.write(str(XSSCount))
    f.write("\n")
    f.write("HTML and XSS Count: ")
    f.write(str(HTMLXSSCount))
    f.write("\n")
    f.write("HTML Count: ")
    f.write(str(HTMLCount))
    f.write("\n")
    f.write("Cookie Vuln. Counter: ")
    f.write(str(COOKIEVULN))
    f.write("\n")
    f.write("Open Redirect Count: ")
    f.write(str(OPRED))
    f.write("\n")
    f.write("Authorization Vuln. Count: ")
    f.write(str(AUTHVULN))
    f.write("\n")
    f.write("remote code execution count: ")
    f.write(str(RCEVULN))
    f.write("\n")
    f.write("Number of disclosed reports Counted Total:")
    f.write(str(number))
    f.write("\n")


browser.quit() 
