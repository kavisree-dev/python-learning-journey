#search method
num=[57,7,3,2,1,9]
print(num.index(2))
print(num.count(7))
print(3 in num)

#sorting method
num.sort()                  #ascending
print(num)                  
num.sort(reverse=True)      #descending
print(num)
new=sorted(num)             
print(new)
copy=num.copy()
print(copy)
print(num+[2,5])
print(num*2)