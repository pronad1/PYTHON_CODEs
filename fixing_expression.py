for _ in range(int(input())):
    s=str(input())
    a=int(s[0])
    b=int(s[2])
    if a>b:
        print(f"{str(a)}>{str(b)}")
    elif a<b:
        print(f"{str(a)}<{str(b)}")
    else:
        print(f"{str(a)}={str(b)}")