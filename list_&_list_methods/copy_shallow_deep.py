#copy
a=[4,3,2]
b=a
b[0]=88
print(a)            #changed

#shallow copy
a=[1,2,3,4,4,9,2]
b=a.copy()
b[0]=55
print(a)            #unchanged

#deep copy
import copy
c=[[1,2],[4.5,8],[3,4]]
d=copy.deepcopy(c)
d[0][1]=55
print(c)            #unchanged

#max,min,sum
print(max(a))
print(min(a))
print(sum(a))

#check empty
if not a:
    print("empty")

#list from range
s=list(range(1,8))
print(s)

#flatten nested list
flat=[x for row in c for x in row]
print(flat)

#remove duplicate from list
new_a=list(set(a))
print(new_a)