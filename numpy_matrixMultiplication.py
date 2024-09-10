import numpy as np

#Matrix multiplication

matrixA = [[1,2],[3,4]]
matrixB = [[5,6],[7,8]]

product = np.dot(matrixA, matrixB)
print(product)
'''
[[19 22]
 [43 50]]
'''

#alternatively,
alternateProduct = np.array(matrixA) @ np.array(matrixB)
print(alternateProduct)
'''
[[19 22]
 [43 50]]
'''
