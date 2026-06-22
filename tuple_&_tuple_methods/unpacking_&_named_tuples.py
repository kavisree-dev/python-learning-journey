#t=(7,9,8)
#t=3,5,2 ---> () optional
#t=(90,) --> single element comma mandatory
'''merits: 
          faster
          less memory
          fixed data'''

#packing
student="kavi","priya","kavin"
print(student)
#unpacking
t=(5,7,9)
a,s,d=t
print(a)
#*unpacking
first,*middle,last=t
print(first)
print(middle)
print(last)


#named tuples - readable structured data
from collections import namedtuple
ModelResult=namedtuple('ModelResult',['accuracy','precision','recall'])
result=ModelResult(2.3,44.5,56.5)
print(result.accuracy)
