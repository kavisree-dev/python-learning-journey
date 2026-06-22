three_count=0
five_count=0
both_count=0
for i in range(1,101):
    if(i%3==0):
        three_count+=1
    if(i%5==0):
        five_count+=1
    if(i%3==0 and i%5==0):
        both_count+=1
print("the number of numbers only divide by 3: ",three_count)
print("the number of numbers only divide by 5: ",five_count)
print("the number of numbers divide by both 3 and 5: ",both_count)

#(+)----> string is concatenate with string and list with list.