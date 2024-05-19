
# WORKING SOLUTION
def index_v2(list_of_values, value):
    result=[]

    for i in range(0,len(list_of_values)):
        if list_of_values[i]==value:
            result.append(i)

    return result

if __name__ == '__main__':
    list_of_values = [1, 3, 4, 1, 5, 2]
    print(range(len(list_of_values)))
    value = 1
    print(index_v2(list_of_values, value))

    list_of_values = [1, 3, 4, 1, 'hello', 'a', 5, 5, 6, 9, 'b', 2, 1, 'what', 5, 6, 6, 3, 6, 2]
    value = 'b'
    print(index_v2(list_of_values, value))

    #index_v2(list_of_values, value)  # Expected answer: [10]

    #this was returing [1,1] the actual value but not the index
    # result = [num for num in list_of_values if num==value]
    # print(result)

    # this is correct using lis comprehension
    result = [i for i in range(len(list_of_values)) if list_of_values[i] == value]
    print(result)

    # Using Lambda
    result = list(filter(lambda i: list_of_values[i] == value, range(len(list_of_values))))
    print(result)



# How to do this with list comprehension