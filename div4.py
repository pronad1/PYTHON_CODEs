def convert_to_plural(noun):
    return noun[:-2] + "i"

def main():
    t = int(input())
    for _ in range(t):
        singular = input().strip()
        print(convert_to_plural(singular))

if __name__ == "__main__":
    main()
