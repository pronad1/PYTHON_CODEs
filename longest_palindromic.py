def expand(s,l,r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        l-=1
        r+=1
    return s[l+1:r]

s=str(input())
m=0
r=''
for i in range(len(s)):
    r=max(r,expand(s,i,i),expand(s,i,i+1),key=len)
print(r)