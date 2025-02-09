for i in range(int(input())):
    s=input().strip()
    if len(s)==2:
        if s[0]==s[1]:
            print(1)
        else:
            print(2)
    else:
        l=len(s)
        stack=[]
        if s[0]!=s[1]:
            stack.append(s[0])

        for i in range(1,l-1):
            if s[i]!=s[i+1]:
                # print(s[i])
                stack.append(s[i])
        if s[l-1]!=s[l-2]:
            stack.append(s[l-1])
            
        print(len(stack))
        