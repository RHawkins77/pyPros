# Vulnerability Counter Module


sqlCount = 0
XSSCount = 0
XXECount = 0
HTMLCount = 0
HTMLXSSCount = 0
CSRFCount = 0
HTTPCount =0
SSRFCount = 0
XMLCount = 0
COOKIEVULN = 0
OPRED = 0
AUTHVULN = 0
RCEVULN = 0





def vulnCounter(textList):
    global sqlCount
    global XSSCount
    global XXECount
    global HTMLCount
    global HTMLXSSCount
    global CSRFCount
    global HTTPCount
    global SSRFCount
    global COOKIEVULN
    global OPRED
    global AUTHVULN
    global RCEVULN
    global XMLCount
    textList = [x for x in textList if x is not None]
    length = len(textList)
    i = 0
    for i in range(length):
        if "sql" in textList[i].lower():
            sqlCount = sqlCount + 1
        if "csrf" in textList[i].lower():
            CSRFCount = CSRFCount + 1
        if "xss" in textList[i].lower() or "cross-site scripting" in textList[i].lower() or "cross site scripting" in textList[i].lower():
            if "html" in textList[i].lower() and "xss" in textList[i].lower():
                continue
            else:
                 #print(textList[i])
                 #print(textList[i].lower())
                 XSSCount = XSSCount + 1
        if "xml" in textList[i].lower():
            XMLCount = XMLCount + 1
        if "xxe" in textList[i].lower():
            XXECount = XXECount + 1
        if "html" in textList[i].lower() and "xss" in textList[i].lower():
            HTMLXSSCount = HTMLXSSCount + 1
        if "http" in textList[i].lower():
            HTTPCount = HTTPCount + 1
        if "ssrf" in textList[i].lower():
            SSRFCount = SSRFCount + 1
        if "cookie" in textList[i].lower():
            COOKIEVULN = COOKIEVULN + 1
        if "open redirect" in textList[i].lower() or "open-redirect" in textList[i].lower():
            OPRED = OPRED + 1
        if "auth" in textList[i].lower():
            AUTHVULN = AUTHVULN + 1
        if "rce" in textList[i].lower() or "remote code execution" in textList[i].lower():
            RCEVULN = RCEVULN + 1
        i = i + 1

