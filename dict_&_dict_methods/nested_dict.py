#neted dictionary
record={"student_1":{"name":"kavi","age":21,"dept":"data science"},"student_2":{"name":"sree","age":21,"dept":"fullstack"}}
#access--(dict_name[key_1][key_2])
print(record["student_1"]["dept"])
#loop
for student,details in record.items():
    print(student,":")
    for key,value in details.items():
        print("   ",key,":",value)

#practice:
companies={"infosys":{"location":"chennai","employee number":21,"domain":"data science"},"tcs":{"location":"coimbatore","employee number":21,"domain":"fullstack"}}
print(companies["tcs"]["location"])
for name,details in companies.items():
    print(name,":")
    for key, value in details.items():
        print("   ",key,":",value)