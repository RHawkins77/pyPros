from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time  

#open Web Browser
browser = webdriver.Firefox()  
#get hackerone disclosed hacktivity page
browser.get('https://hackerone.com/hacktivity?sort_type=upvotes&filter=type%3Apublic&page=139&range=forever')  
#wait for 3 seconds for page to load
time.sleep(2)
#print pages title  
print(browser.title)

ids = browser.find_elements_by_class_name('hacktivity__link')
textList = []
for ii in ids:
	#print ii.tag_name
	textList.append(ii.get_attribute('text'))
#	print("FUCKYABUDDY")
print(textList.count('SQL'))	
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
