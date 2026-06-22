a={2,4}
b={2,4,5,7}
print(a.issubset(b))        #is small?
print(b.issuperset(a))      # is big?
print(a.isdisjoint({5}))    # no common elements