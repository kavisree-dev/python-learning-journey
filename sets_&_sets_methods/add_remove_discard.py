s={1,3,4,5}
s.add(34)      #added
print(s)
s.add(3)       #no changes

s.remove(4)
print(s)          #remove show error if no element
s.discard(89)     #discard don't show error if no element


popped=s.pop()   #removing random element
print(s)

s.clear()        #empty set