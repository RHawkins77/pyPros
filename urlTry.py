from requests import session
from selenium import webdriver  
import time  
#open Web Browser
browser = webdriver.Firefox()  
#get hackerone disclosed hacktivity page
browser.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever')  
#wait for 3 seconds for page to load
time.sleep(3)
#print pages title  
print(browser.title)
 
ids = browser.find_elements_by_class_name('hacktivity__wrapper')
num = 0
myButton = browser.find_element_by_xpath('/html/body/div[3]/span/div/div[2]/div[1]/div[27]/div[1]/div[2]/button[2]')

for ii in ids:
    num = num + 1

while myButton.is_enabled():
    myButton.click()
    time.sleep(3)
    ids2 = browser.find_elements_by_class_name('hacktivity__wrapper')
    for ii in ids2:
        num = num + 1

print(num)
browser.quit() 

#with session() as c:
#    c.post('https://hackerone.com/users/sign_in', data=username)
#    response = c.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever')
#    print(response.headers)
#    print(response.text)
