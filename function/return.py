#without return:
def no_return():
    print("hello")

def with_return():
    return"hello"

result_without_return=no_return()
print("without return value is",result_without_return)
result_with_return=with_return()
print("with return value is",result_with_return)

#practice:
def square(n):
    return n*n
val=square(5)
print("square is:",val)

