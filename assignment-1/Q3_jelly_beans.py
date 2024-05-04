# WORKING
def jelly_beans(colours):
    resultDict={}
    strBeans = colours.lower()
    # 1. convert the string in to dict with the count
    for i in range(len(strBeans)):
        if strBeans.char[i] in resultDict:
            resultDict[strBeans[i]] = resultDict[strBeans[i]]  + 1
        else:
            resultDict[strBeans[i]] = 1

    # 2. Get the maximum count
    # 3. add all the remaining count except the max count
    listOfValues = resultDict.values()
    maxValue = max(listOfValues)
    sumOfAll = sum(listOfValues)

    return sumOfAll-maxValue


if __name__=='__main__':
    print(jelly_beans("rbb"))
    print(jelly_beans("oobbby"))
    print(jelly_beans("ooobbbggy"))


