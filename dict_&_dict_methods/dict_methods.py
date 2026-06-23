student={"name":"kavi","Age":21,"course":"data science","year":"4th year"}

#four most important method
#1---.keys()
print(student.keys())

#2---.values()
print(student.values())

#3---.items()
print(student.items())      #tuples pair return

#4---.get()
print(student.get("college"))              #default - none
print(student.get("college","no key"))     #you can change your default

#practice
employee={"id":121,"name":"kavi","dept":"data science","salary":50000}
print(employee.keys())
print(employee.values())
print(employee.get("bonus","Not Assigned"))
print(employee.items())
