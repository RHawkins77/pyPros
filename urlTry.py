from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from vulnCounter import * 
from append import appendList
import time  
#open Web Browser
browser = webdriver.Firefox()  
#get hackerone disclosed hacktivity page
browser.get('https://hackerone.com/hacktivity?sort_type=upvotes&filter=type%3Apublic&page=144&range=forever')  
#wait for 3 seconds for page to load
time.sleep(2)
#print pages title  
print("We Are on Page :" , browser.title)
textList = []
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
        appendList(textList,browser)
        #print(textList)
        vulnCounter(textList)
        break
    #print("I skipped?")
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
    f.write(str(num))
    f.write("\n")

#print(textList)

browser.quit() 
