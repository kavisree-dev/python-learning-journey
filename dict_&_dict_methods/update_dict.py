#update() method:
student={"name":"kavi","age":21,"dept":"ECE","marks":{"english":89,"maths":90,"tamil":78}}
extra={"college":"AAMEC"}
student.update(extra)
print(student)
student.update({"age":22,"college":"AAMEC"})
print(student)

#pandas
#2 config dictionaries merge
default_settings={"delimiter":",","encoding":"utf-8","header":True}
custom_settings={"delimiter":"|","skiprows":3}
default_settings.update(custom_settings)
print(default_settings)

#practice
resume={"name":"Kavi sree A","degree":"ECE"}
new_info={"skills":"python,SQL","internship":"Data Science","degree":"B.E ECE"}
resume.update(new_info)
print(resume)