'''name="kavi"
count=0
for c in name:
    if c in "aeiouAEIOU":
       count+=1
print(count)

'''
name="kavi"
count=sum(1 for c in name if c in "aeiouAEIOU")
print(count)


   