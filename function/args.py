#*args----acepting whaterver the count of valuess passed
def total(*args):
    print(args)           #printing just values
    return sum(args)      #printing the sum
print(total(12,43))
print(total(2,4,5,6))