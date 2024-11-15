def my_function(country="Bangladesh"):
    print("I am from "+country)


print("Enter 5 country : ")
for _ in range(5):
    my_function(input())

my_function()

def myfun(n):
    return lambda a : a*n

mydouble=myfun(2)
mytriple=myfun(3)

print(mydouble(11))
print(mytriple(11))