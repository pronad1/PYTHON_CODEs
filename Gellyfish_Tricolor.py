for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    flower_knight_hits = (c + d - 1) // d
    gelly_knight_hits = (d + c - 1) // c
    # How many hits does Flower's knight need to kill Gellyfish?
    flower_hits = (a + d - 1) // d
    # How many hits does Gellyfish's knight need to kill Flower?
    gelly_hits = (b + c - 1) // c

    # If Gellyfish's knight can kill Flower's knight before Flower's knight can kill Gellyfish, Gellyfish wins
    if c <= d:
        print("Flower")
    else:
        print("Gellyfish")