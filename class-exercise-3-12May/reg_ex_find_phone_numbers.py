

import re

if __name__=="__main__":
    myDict={}
    phones = '''LeBroooon James: 123-111-212
    Dd Wade: 391-399-128
    Steve Curry: 188381887
    Kk Durant: 212-212212
    Jon Harden: 371*371&196
    Kiwi Leonard: -192-182-736-
    Power George: 8198-18-817'''

    p = re.compile("(\w+\s\w+):?\s?-?(\d.*)", re.M) # remove the underline and fill in your code

    # print(p.findall(phones))

    list = p.findall(phones)

    # t = "Akash"
    # t.replace()
    for item in list:
        myDict[item[0]]=item[1].replace("-","").replace("*","").replace("&","")

    print(myDict)
