#pass whatever number of values in kay value pair.
def profile(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,":",value)
profile(name="kavi",dept="ECE",goal="data analytics")

#practice:
def describe(*args,**kwargs):
    print("skills:",args)
    print("datils:",kwargs)
describe("python","SQL","power BI",name="kavi",college="AAMEC")