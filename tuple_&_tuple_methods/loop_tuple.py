t=('kavi','ECE',89,67,34)

#for loop
for item in t:
    print(item)

#access with index --> use enumerate
for index, item in enumerate(t):
    print(index,item)

subjects=('tamil','english','maths','social','science')
for index, item in enumerate(subjects):
    print("subject",index,item)