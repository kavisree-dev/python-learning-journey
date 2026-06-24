#function -- reusable block of code, with a name(call only by a name())
#def function_name():
#    intended code block
def greet():
    print("welcome")
greet()
greet()   #if again and gain call it works.

def introduce():
    print("Myself kavi sree")
    print("ECE student")
    print("Data science intern")
greet()
introduce()

#arguments:     ---    giving input for function
#single argumment:
def greet(name):
    print("welcome",name)
greet("kavi")
#multiple argument:
def add(a,b):
    print(a+b)
add(3,5)

#practice:
def student_info(name,dept):
    print(name,"from",dept)
student_info("kavi","ECE")
