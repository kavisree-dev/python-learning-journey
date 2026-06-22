#title
title="student report card generator"

#stuent detail in tuple
student_detail=("kavi",21,"ECE",(86,90,78,93,99))

#student detail unpacking
name,age,dept,marks=student_detail

#subject detail in tuple
subjects=('networks','signals and systems','communication system','control sytem','calculus')

#for loop --> for zipping subject with their marks

#total
total=sum(marks)

#average
average=sum(marks)/len(marks)

#highest mark which subject
high_mark=max(marks)
high_index=marks.index(high_mark)

#lowest mark which subject
low_mark=min(marks)
low_index=marks.index(low_mark)

#final project
print("="*30)
print(title.upper())
print("="*30)
print("Name      : ",name)
print("Age       : ",age)
print("Department: ",dept)
print("-"*35)
print("Subject wise marks:")
for subject,mark in zip(subjects,marks):
    print(subject,":", mark)
print("-"*35)
print("Total mark: ",total)
print("Average:",average)
print("highest:",subjects[high_index],'-',high_mark)
print("Lowest:",subjects[low_index],"-",low_mark)
print("="*35)