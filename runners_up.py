n=int(input())
arr=map(int,input().split())
arr=sorted(arr,reverse=True)
for i in arr:
    if i < max(arr):
        print(i)
        break