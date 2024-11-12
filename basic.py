
g="edd";# global variable
MyVariableName = "John"; #Pascal Case(Each word starts with a capital letter)
print(MyVariableName); 
my_variable_name = "John"; #Snake Case(Each word is separated by an underscore character)
print(my_variable_name);
fruits= "Orange", "Banana", "Cherry"; #Unpack a list:
x, y, z =fruits
print(x,' ',y," ",z,' ',type(fruits));

print(x+y+z,'\n');
print(x,y,z,'\n');
x=4.0
y=5j
print(x+y,' ',type(x+y));

def myf():
    g="fastastic"
    print("Python is "+g)

myf()

print("Python is "+g)

def fun():
    global p
    p="Prosenjit"

fun()
print("By using global keyword "+p)
print(type(p)) #Print datatype

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(5,10))

z=int(4.785)
print(z)
z=float("3.497")
print(z,' ','This is my last semester CGPA','\n',"And now I am trying to do something better: ")

