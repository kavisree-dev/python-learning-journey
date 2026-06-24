#function project:
def student_report(name,*subject,**details):
    print("="*35)
    title="student report generator"
    print(title.upper())
    print("="*35)
    print("Name:",name)
    print("\nSubjects:")
    for i,sub in enumerate(subject,1):
        print(f"{i}. {sub}")
    print("\nExtra details:")
    for key, value in details.items():
        print(f"{key}:{value}")
    print("="*35)

student_report(
        "Kavi Sree","python","SQL","power BI",college="AAMEC",department="ECE"
    )
