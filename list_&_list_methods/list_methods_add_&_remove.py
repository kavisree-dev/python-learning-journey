#add elements method
num=[1,3,5,6,9]
num.append(4)               #single element add
print(num)
num.insert(1,67)            #add element in the particular index
print(num)
num.extend([4,9])           #add a list of elements
print(num)


#remove elements method
name=['hi','hello','welcome','thanks','sorry','hey']
name.remove('sorry')
print(name)
name.pop()
print(name)
name.pop(2)
print(name)
name.clear()
print(name)