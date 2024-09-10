import pandas as pd

#grouping data

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40] 
})

grouped = df.groupby('Category')
print(grouped) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7b447a2ebe10>
summary = grouped.mean()
print(summary)
'''
          Values
Category        
A           20.0
B           30.0
'''
