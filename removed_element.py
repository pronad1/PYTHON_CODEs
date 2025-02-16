nums=list(map(int,input().split()))
val=int(input())

k=0

for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
print(k)