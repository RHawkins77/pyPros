




def writeList(bountyPriceList, spot, titleList,linkList):
    j = 1   
    i = 0
    for ii in spot:
        spotholder = int(ii)
        with open('topList.txt', 'a+') as f:
            f.write("#")
            f.write(str(j))
            f.write("\n")
            f.write("$")
            f.write(bountyPriceList[i].encode('utf-8'))
            f.write("\n")
            f.write("The Title of the Report:")
            f.write(titleList[spotholder].encode('utf-8'))
            f.write("\n")
            f.write("The URL:")
            f.write(linkList[spotholder].encode('utf-8'))
            f.write("\n")
        i = i + 1
        j = j + 1
        if(j>200):
            return 1





def writeLastList(bountyPriceList, spot, titleList,linkList):
    j = 1
    i = len(spot)-1
    while j < 201:
        with open('BottomList.txt', 'a+') as f:
            f.write("#")
            f.write(str(j))
            f.write("\n")
            f.write("$")
            f.write(bountyPriceList[i].encode('utf-8'))
            f.write("\n")
            f.write("The Title of the Report:")
            f.write(titleList[int(i)].encode('utf-8'))
            f.write("\n")
            f.write("The URL:")
            f.write(linkList[int(i)].encode('utf-8'))
            f.write("\n")
        i = i - 1
        j = j + 1
        if j > len(spot) or i < 0:
            return 1
    return 1
