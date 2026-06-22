a=[]
print("enter 10 numers:")
for i in range(10):
    num=int(input("enter the number: "+str(i+1)))
    a.append(num)
print(a)
sum=0
for i in a:
    sum+=i
print(sum)
print(f"Average: {sum/10}")
