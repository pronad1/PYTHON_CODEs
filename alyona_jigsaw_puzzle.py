for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    happy=0
    cur_pic=0
    layer=0
    pic_re=1

    for i in range(n):
        cur_pic+=arr[i]

        while cur_pic>=pic_re:
            if cur_pic==pic_re:
                happy+=1
        layer+=1
        pic_re+=8*layer

    print(happy)