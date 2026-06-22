score=int(input("enter your score: "))
if score>=40:
    interview=input("enter your interview result(clear/not clear): ")
    if interview=="clear":
      print("selected")
    else:
      print("rejected")
else:
   print("rejected")