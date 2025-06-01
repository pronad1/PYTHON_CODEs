for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    fl=min(a,b)
    kn=min(c,d)
    if fl<kn:
        ma=max(a,b)
        if ma==a:
            print("Gellyfish")
        else:
            print("Flower")
            
    elif  fl>kn:
        ma=max(c,d)
        if ma==c:
            print("Gellyfish")
            
        else:
            print("Flower")
    else:
        ma=max(a,b)
        if ma==a:
            print("Gellyfish")
        else:
            print("Flower")