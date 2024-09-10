import pandas as pd
import numpy as np

#converting numpy array to dataframe

numpyArray = np.array([[1,4],
                      [2,5],
                      [3,6]])
 
df = pd.DataFrame(numpyArray)
print(df)
'''
   0  1
0  1  4
1  2  5
2  3  6
'''
