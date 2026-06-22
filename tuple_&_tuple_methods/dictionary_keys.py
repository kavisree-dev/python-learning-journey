#d={'name':'kavi'}
#list cannot do this ---> {[1,2]:'something'}--->  dictionay immutable-list mutable
#tuples mutable so,
s={(1,23):'something'}
print(s[(1,23)])

feature_pairs={('age','income'):2.98,('city','price'):5.78}
print(feature_pairs[('age','income')])