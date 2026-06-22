#nested tuple
t=(8,8,5,(6,9),8)
print(t[3][0])

#conversion via modify
#tuple to list
l=list(t)
print(l)

#modify
l.append(23)
print(l)

#list to tuple
t=tuple(l)
print(t)