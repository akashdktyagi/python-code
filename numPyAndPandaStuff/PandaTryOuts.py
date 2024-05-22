
import pandas as pd
import numpy as np

if __name__=="__main__":
    arr = np.array([1,2,3,4,5,6])
    print(arr)

    myseries_no_index = pd.Series(arr)
    print("Panda Series with default index \n",myseries_no_index)

    myseries_withIndexes = pd.Series(arr,index=['a','b','c','d','e','e'])
    print("Panda Series with Character Indexs\n",myseries_withIndexes)
    print("Get Data for a specific key 'e' \n",myseries_withIndexes['e'])


    print("Types of Arguments which you can pass in Panda Series function")

    # 1. List
    seriesWithList = pd.Series([1,2,3,4,5])
    print("Panda Series with List\n",seriesWithList)

    seriesWithDict = pd.Series({'a':1,'b':2,'c':3})
    print("Panda Series with Dictionary\n",seriesWithDict)

    seriesWithNumPyArray = pd.Series(np.array([1,2,3,4,5]))
    print("Panda Series with NumPy Array\n",seriesWithNumPyArray)