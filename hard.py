
for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    s1=min(m,a)
    rs1=m-s1
    cc=min(rs1,c)
    s1+=cc
    cs=c-cc
    s2=min(m,b)
    rs2=m-s2
    s2+=min(rs2,cs)

    print(s1+s2)

