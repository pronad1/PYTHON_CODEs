def my_function(country="Bangladesh"):
    print("I am from "+country)


print("Enter 5 country : ")
for _ in range(5):
    my_function(input())

my_function()