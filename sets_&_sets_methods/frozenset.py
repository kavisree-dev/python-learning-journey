fs=frozenset({7,8,9})
fs.add(3)
print(fs)    #attribute error
#immutable - so hashable
#can use for dict key