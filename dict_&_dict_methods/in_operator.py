#in operator:
student={"name":"kavi","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}

#key check
print("name" in student)
print("marks" in student)

#❌ way -keyerror
#print(student["marks"])
#✅ way - check before acces 
if "marks" in student:
    print(student["marks"])
else:
    print("marks not found")

#value check
print("kavi" in student.values())
print(21 in student.values())

#practice
profile={"name":"kavi","linkedin":"kavi_dev","github":"kavisree-dev"}
if "twitter" in profile:    #key check
   print(profile["twitter"])
else:
    print("twitter not found")
print("kavisree-dev" in profile.values())
