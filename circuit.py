t=int(input())
for i in range(t):
    l=int(input())
    z=0;o=0
    for j in range(2*l):
        x=int(input())
        if x==0:
            z+=1
        else:
            o+=1
    if z==o:
        print(1,' ',l,"\n")
    elif z==0 or o==0:
        print(0,' ',0,"\n")
    else:
        print(0,' ',o,"\n")