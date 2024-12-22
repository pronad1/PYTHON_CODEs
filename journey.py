for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    e=a//(b+c+d)*3
    if a%(b+c+d)>b+c:
        e+=3
    elif a%(b+c+d)>b:
        e+=2
    elif a%(b+c+d)>0:
        e+=1
    print(e)