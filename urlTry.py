from requests import session
from selenium import webdriver  
import time  
browser = webdriver.Firefox()  
browser.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever')  
time.sleep(3)  
print(browser.title) 
ids = browser.find_elements_by_class_name('hacktivity__wrapper')
num = 0
for ii in ids:

    num = num + 1
print(num)     
browser.quit() 



#username = "<USERNAME>&password=<PASSWORD>"

#with session() as c:
#    c.post('https://hackerone.com/users/sign_in', data=username)
#    response = c.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever')
#    print(response.headers)
#    print(response.text)
