for i in range(int(input())):
    nums=list(map(int,input().split()))

    i=1
    for j in range(1,len(nums)):
        if nums[j] != nums[i-1]:
            nums[i]=nums[j]
            i+=1
        
    print(nums[:i])