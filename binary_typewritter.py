for _ in range(int(input())):
    n = int(input())
    s =input().strip()
    cnt=0
    for i in range(n-1):
        if s[i]!= s[i+1]:
            cnt+=1

    if cnt==0:
        print(n+int(s[0]=="1"))