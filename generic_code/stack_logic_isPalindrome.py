
def isPalindrome(myString):
    reverseString=""
    myList = [i for i in myString]
    length = len(myList)
    for i in range(length):
        reverseString = reverseString + myList.pop()

    print("reversed string : " + reverseString)
    print("actual string : " + myString)
    if reverseString == myString:
        return True
    else:
        return False


if __name__=='__main__':
    myString = "NITIN"
    print(isPalindrome(myString))

