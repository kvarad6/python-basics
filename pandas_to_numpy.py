import pandas as pd
import numpy as np

#converting pandas dataframe to numpy array
df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
df2npy = df.to_numpy()
print(type(df2npy)) #<class 'numpy.ndarray'>
print(df2npy)
'''
[[1 4]
 [2 5]
 [3 6]]
'''
