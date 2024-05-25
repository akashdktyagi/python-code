import pandas as pd
import numpy as np

if __name__=="__main__":
    df = pd.DataFrame(
        {'first name': ['Josh', 'John', 'Jane',"a","b","c"],
         'last name': ['Anderson', 'Doe', 'Doe',"e","f","g"]
         }
    )


    print(df)
    df['last name'].drop([1,2],inplace=True)

    # df['last name'] = df['last name'].apply(str.title)

    # print(df)

    print(df)