import pandas as pd

#Merging the dataframes

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value': [10, 20, 30]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value': [40, 50, 60]
})

mergedDf = pd.merge(df1, df2, on='key')
print(mergedDf)
'''
  key  value_x  value_y
0   B       20       40
1   C       30       50
'''

