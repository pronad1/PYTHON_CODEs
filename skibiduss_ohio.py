def min_length(s):
    l=len(s)
    p=0
    for i in range(0,l-1):
        if s[i] == s[i+1]:
            p+=1
    return max(l-p*2,1)

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(min_length(s))

if __name__ == "__main__":
    main()
