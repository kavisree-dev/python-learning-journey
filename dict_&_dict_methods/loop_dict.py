student={"first_year":"full_stack","second_year":"data science","final_year":"data analytics","third_year":"UI/UX design"}
for key in student.keys():   #work if not including .keys()
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, ":", value)

#contion loop
for year, course in student.items():
    if year == "final_year":
       print("Eligible for the course of", course)
    else:
        print("not eligible")

#if-else condition    
admin={"name":"kavi","year":"final_year","course":"data science"}      
if admin.get("year") == "final_year":
    print("Eligible for the course of", admin.get("course"))
else:
    print("not eligible")
           
#practice
admission={"data science":78000,"fullstack":67000,"UI/UX design":66000}
for dept, fees in admission.items():
    if fees >= 70000:
       print("pay advance amount for ",dept)
    else:
       print("no advance")