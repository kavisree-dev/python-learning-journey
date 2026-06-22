title="student grade analyzer"
print(title.upper())

#datas in sets
passed_math={'kavi','priya','sam','ram'}
passed_science={'krish','kalai','sree','kavi'}
passed_english={'priya','sam','tom','kavi'}

#passed in all subject
all_pass=passed_math & passed_science & passed_english
print("All subjets passed: ", all_pass)

#passed in one subject
anyone=passed_english | passed_science | passed_math
print("Passed atleast one: ", anyone)

#passed only in maths remaining fail
only_math=passed_math-passed_science-passed_english
print("Only math: ", only_math)

#total number of unique students
print("Total unique students: ",len(anyone))