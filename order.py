import time
def orderList(bountyPriceList,spot):
    for i in range(len(bountyPriceList)):
        for j in range(len(bountyPriceList) - 1):
            if int(bountyPriceList[j]) < int(bountyPriceList[j+1]):
                spot[j+1], spot[j] = spot[j],spot[j+1]
                bountyPriceList[j+1], bountyPriceList[j] = bountyPriceList[j], bountyPriceList[j+1]
                #print(bountyPriceList)
                #print(spot)
    return bountyPriceList, spot 
