import pandas as pd

#handling missing data

df = pd.DataFrame({'A': [1, 2, None], 'B': [5, None, 7]})
# print(df)
'''
     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
'''
#Removing missing values
dfDropped = df.dropna()
print(dfDropped)
'''
     A    B
0  1.0  5.0
'''

#Filling missing values
dfFilled = df.fillna(0) #filling with '0'
print(dfFilled)
'''
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
'''
