#❌way -- reference copy
#student={"name":"kavi","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}
#new_student=student    ===not copying (same object).
#new_student["name"]="priya"
#print(student)   --->   student={"name":"priya","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}
#print(new_student)   --->student={"name":"priya","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}
#both are changed  --> that is the problem

#copy():✅
student={"name":"kavi","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}
new_student=student.copy()        #real copy
new_student["name"]="priya"
print(student)
print(new_student)

#practice
original_df_config={"rows":1000,"columns":12,"target":"sales"}
exp_config=original_df_config.copy()
print(exp_config)
original_df_config["columns"]=56
print(original_df_config)
print(exp_config)