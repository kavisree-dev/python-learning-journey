name='sree'
age=21
#f-string
print(f"My name is {name} and my age is {age}")

#format()
print("My name is {} and my age is {}".format(name,age))

#%style(old)
print("My name is %s and my age is %d" % (name,age))

#f-string expressions
print(f"2+2={2+2}")
print(f"PI={3.14159:.2f}")   #f--> f string for writing variable of expression inside{}
                             #PI--variable
                             #{3.14159}--> value that is to print
                             #: -->starting format
                             #.2 -->after decimal two digits
                             # f-->float