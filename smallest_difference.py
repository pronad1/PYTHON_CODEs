for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    se=set(a)
    v=0
    m=0
    for i in se:
        x=a.count(i)
        if x>m:
            m=x
            v=i
    
    se_list=list(se)
    p=se_list.index(v)

    if se_list[p+1]-v==1 or v-se_list[p-1]==1:
        m+=1
    print(m)