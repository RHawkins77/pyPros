from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time  
sqlCount = 0
XSSCount = 0
XXECount = 0
HTMLCount = 0
HTMLXSSCount = 0
CSRFCount = 0
HTTPCount =0
SSRFCount = 0
XMLCount = 0

#open Web Browser
browser = webdriver.Firefox()  
#get hackerone disclosed hacktivity page
browser.get('https://hackerone.com/hacktivity?sort_type=upvotes&filter=type%3Apublic&page=1&range=forever')  
#wait for 3 seconds for page to load
time.sleep(2)
#print pages title  
print("We Are on Page :" , browser.title)

ids = browser.find_elements_by_class_name('hacktivity__link')
textList = []
num = 0

def vulnCounter():
	global sqlCount
	global XSSCount
	global XXECount
	global HTMLCount
	global HTMLXSSCount
	global CSRFCount
	global textList
	global HTTPCount
	global SSRFCount
	global XMLCount
	textList = [x for x in textList if x is not None]
	length = len(textList)
	i = 0
	for i in range(length):
		if "sql" in textList[i].lower():
			sqlCount = sqlCount + 1
		if "csrf" in textList[i].lower():
			CSRFCount = CSRFCount + 1
		if "xss" in textList[i].lower():
			if "html" in textList[i].lower() and "XSS" in textList[i].lower():
				continue
			else:
				XSSCount = XSSCount + 1
		if "xml" in textList[i]:
			XMLCount = XMLCount + 1
		if "XXE" in textList[i] or "xxe" in textList[i]:
			XXECount = XXECount + 1
		if "HTML" in textList[i] or "html" in textList[i] and "XSS" in textList[i] or "xss" in textList[i]:
			HTMLXSSCount = HTMLXSSCount + 1
		if "HTTP" in textList[i] or "http" in textList[i]:
			HTTPCount = HTTPCount + 1
        if "SSRF" in textList[i] or "ssrf" in textList[i] or "ssrf" in textList[i]:
			SSRFCount = SSRFCount + 1
			i = i + 1	
	return textList

def appendList():
	global textList
	global num
	global ids
	#print("ids going in:", ids)
	for ii in ids:
		num = num + 1
		#append ii.Text_name to our list.
		word = ii.get_attribute('text')
		#print(word)
		textList.append(word)
	#print("textlist before clean:",textList)
	textList = [x for x in textList if x is not None]
	#print("textList going out:",textList)
	return textList




while True:
	myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
	appendList()
	myButton.click()			
	try:
		#print("i am here")
		myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
		time.sleep(2)
		ids = browser.find_elements_by_xpath('hacktivity__link')
		appendList()
	except NoSuchElementException:
		#print("im where I should be")
		time.sleep(2)
		ids = browser.find_elements_by_class_name('hacktivity__link') 
		appendList()
		#print(textList)
		vulnCounter()
	break
#print(textList)
print("SQL COUNT : " , sqlCount)
print("CSRF COUNT : " , CSRFCount)
print("XML COUNT : " , XMLCount)
print("HTTP COUNT : " , HTTPCount)
print("SSRF COUNT : " , SSRFCount)
print("XXE COUNT : " , XXECount)
print("XSS COUNT : " , XSSCount)
print("HTML and XSS COUNT: " , HTMLXSSCount)
print("HTML COUNT : " , HTMLCount)
print("Number of disclosed reports :", num)
#print(textList.count('SQL'))	
#print(textList)

#num = 0

#while True:
#    myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
#    ids.append(browser.find_elements_by_class_name('hacktivity__wrapper'))
 #   myButton.click()   
  #  time.sleep(2)
   # try:	    
    #    myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')
     #   ids.append(browser.find_elements_by_class_name('hacktivity__wrapper'))
   # except NoSuchElementException:
	#	ids.append(browser.find_elements_by_class_name('hacktivity__wrapper'))
	#	break

#print(ids)
browser.quit() 

#with session() as c:
#    c.post('https://hackerone.com/users/sign_in', data=username)
#    response = c.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever')
#    print(response.headers)
#    print(response.text)
