
def isPalindrome(myString):
    reverseString=""
    myList = [i for i in myString]
    length = len(myList)
    for i in range(length):
        reverseString = reverseString + myList.pop()
    if reverseString == myString:
        return True
    else:
        return False


if __name__=='__main__':
    list=[]
    dict={}
    myString = "SUPERREVIVER"
    maxLength=10000000

    for i in range(len(myString)):
        for j in range(i+1,len(myString)+1):
            str = myString[i:j]
            print(str)
            if isPalindrome(str):
                dict[str]=len(str)

    print(dict)
    print(max(dict.values()))


    # print(isPalindrome(myString))

