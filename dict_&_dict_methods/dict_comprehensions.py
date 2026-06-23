#normal way ---(4 lines)
#suares={}
#for n in range(1,6):
#    squares[n]=n**2
#print(squares)

#comprehension way ---(2 line)
squares={n:n**2 for n in range(1,6)}    #{key:value for item in iterable}
print(squares)

#condition
marks={"python":78,"java":89}
passed={sub: m for sub, m in marks.items() if m>=60}
print(passed)

#value transform
prices={"laptop":56000,"phone":34000}
discounted={item:price*0.9 for item,price in prices.items()}
print(discounted)

#ds concept
grades={"A+","A","B","B+","C"}
encode={g: i for i, g in enumerate(grades)}
print(encode)    #string --> number

#practice
student={"kavi":92,"priya":45,"ravi":75,"sam":55}
passed_student={name:mark+5 for name,mark in student.items() if mark>=60}
print(passed_student)