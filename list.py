
li=["Apple","Banana","cherry"] ; print(li,' ',"The length of the list is: ",len(li))
isli=list(("Apple","Banana","cherry"))
print(isli) ; print(isli[1:3])
li.append("orange"); print(li)
li.insert(1,"coconat"); print(li)
tropical = ["mango", "pineapple"]
li.extend(tropical); print(li)
li.remove("Apple"); print(li)
li.pop(0); print(li); li.pop();print(li)
del li[3]; print(li)
# li.clear() ; print(li)
for x in li:
    print(x)
for i in range(len(li)):
    print(li[i])
    i=0
while i< len(li):
    print(li[i])
    i=i+1
nli=[]
for x in li:
    if "orange" in x:
        nli.append(x)

print(nli)
li.sort(); print(li)

li=[100, 50, 65, 82, 23]; li.sort(); print(li)
li.sort(reverse=True); print(li)

myli=li.copy(); print(myli) #myli=list(li)  # myli=li[:]
