students={"kavi":{"python":90,"sql":98,"stats":89},"sree":{"python":89,"sql":78,"stats":77}}
def get_grade(avg):
    if avg>=90:
        return"A+"
    elif avg>=80:
        return"A"
    elif avg>=70:
        return"B+"
    elif avg>=60:
        return"B"
    elif avg>=45:
        return"c"
    else:
        return"fail"
for name,subjects in students.items():
    total=0
    for subject,mark in subjects.items():
        total+=mark
    avg = total/len(subjects)
    grade=get_grade(avg)
    print(f"\n{name}")
    print(f"Average : {avg:.1f}")      #float ----- avg = float(total)/len(subjects) ✅
                                       #rount ----- avg = round(total)/len(subjects) ✅
                                       #            print(f"Average : {avg}")
                                       #print(f"Average : {round(avg,1)}") ✅

    print(f"Grade   : {grade}")