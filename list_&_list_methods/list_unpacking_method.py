num=[1,234,5,6]
a,f,k,u=num
print(a,f,k,u)
print(a)

#star unpacking      #* removing outer container and gives you the individual element
first,*rest=[1,2,3,4,5]
print(first)
print(rest)

*start,last=[3,4,5,6,7]
print(start)
print(last)