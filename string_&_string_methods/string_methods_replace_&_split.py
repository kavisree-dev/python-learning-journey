kav="I love python"
print(kav.replace("python","coding"))

#string to list
print(kav.split())        #['i', 'love', 'python']

print(kav.split("()"))    #can use |@#$%() etc,.. any character instead of (,)
                          #['i love python']
              
print(",".join(kav))      #i, ,l,o,v,e, ,p,y,t,h,o,n
print("|".join(kav))      #i| |l|o|v|e| |p|y|t|h|o|n

#list to string     
words=['i','love','python']
print(','.join(words))    #i,love,python