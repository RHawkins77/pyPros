#Appending List of titles
num = 0
def appendList(textList, browser):
    global num
    ids = browser.find_elements_by_class_name('hacktivity__link')
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




