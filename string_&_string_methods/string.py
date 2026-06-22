#'hi'
print('hi)')
#"hi"
print("hi)")
#'''hi'''
print('''hi''')
#"""hi"""
print("""hi""")
name="kavi"
#immutable --> name[0]="a" (cannot change)
#to create new string --> adding the index to the string
name="K"+name[1:]
print(name)
#string indexing
print(name[0])
print(name[-1])
#string slicing --> name[start:stop:step]
print(name[0:3])
print(name[2:])
print(name[:3])
print(name[:])
print(name[::2])
print(name[::-1])  #reverse print  
                   #can also used to check for palindrome.

#string operations
a="kavi"
b="sree"
print("hi "+a+b)   #concatenation
print(a*5)        #repetition
print(len(a))     #length
print("vi" in a)  #membership (true or false)
