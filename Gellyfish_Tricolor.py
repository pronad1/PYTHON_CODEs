for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    fl=min(a,c)
    kn=min(b,d)
    
    if fl>kn:
        print("Gellyfish")
        
    elif  fl<kn:
        print("Flower")
        
    else:
        print("Gellyfish")
        
