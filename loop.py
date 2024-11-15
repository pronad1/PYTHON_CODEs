for x in range(6):
    if x==3: break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,' ',y)

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1