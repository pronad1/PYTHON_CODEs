for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            new_arr.append(arr[i])
    arr = [0] + new_arr + [0]
    c = 0
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            c += 1
    print(c)
