from collections import Counter

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    sortedArr=sorted(arr)
    count=Counter(sortedArr)
    print(count)