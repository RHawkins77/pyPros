from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html 
import urllib
#starting firefox
#driver = webdriver.Firefox()
#going to hacktivity disclosed page
#root = etree.Element("https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Apublic&page=1&range=forever")
#finding elements in hacker activity list
#basically finding each disclossure in a list
#print(driver.find_elements_by_class_name("hacktivity hacktivity--voting"))

doc = urllib.request.urlopen("https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Apublic&page=1&range=forever")
    
doc.read()



driver.close()

