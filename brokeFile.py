
from __future__ import print_function
from requests import session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from append import appendList
from append import findIfPaid
from order import orderList
from createList import writeList
from createList import writeLastList
import time 
import json

def writeToBrokenFile(bountyPriceList, spot, titleList, linkList):
    with open("bountyPriceList.txt", "a") as saveFile1:
        json.dump(bountyPriceList, saveFile1)
    with open("spot.txt", "a") as saveFile1:
        json.dump(spot, saveFile1)
    with open("titleList.txt", "a") as saveFile1:
        json.dump(titleList, saveFile1)
    with open("linkList.txt", "a") as saveFile1:
        json.dump(linkList, saveFile1)

