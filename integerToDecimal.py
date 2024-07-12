#converting an integer into decimal


#------- Approach 1 ----------#
from decimal import *

integer = 10

print(Decimal(integer)) #--> 10
print(type(Decimal(integer))) #--> <class 'decimal.Decimal'>


#------- Approach 2 ----------#

import decimal

integer = 10

print(decimal.Decimal(integer)) #--> 10

print(type(decimal.Decimal(integer)))  #--> <class 'decimal.Decimal'>
