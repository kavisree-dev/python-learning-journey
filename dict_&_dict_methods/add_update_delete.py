student={"name":"kavi","Age":21,"course":"data science","year":"4th year"}
#add
student["college"]="AAMEC"
print(student)
#update
student["Age"]=22
print(student["Age"])
#delete - method_1
del student["Age"]
print(student)
#delete - method_2
removed=student.pop("college")
print(removed)
print(student)

#practice
profile={"name":"kavi","skills":"python"}
profile["internship"]="data science"
print(profile)
profile["skills"]="python,sql"
print(profile)
del profile["name"]
print(profile)
