
def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        cows = []
        card_to_cow = {}
        for cow_idx in range(n):
            cards = list(map(int, input().split()))
            cows.append(cards)
            for card in cards:
                card_to_cow[card] = cow_idx + 1 
        
        all_cards = sorted(card_to_cow.keys())
        cow_pos_mod = {}
        possible = True
        for card in all_cards:
            cow = card_to_cow[card]
            pos = all_cards.index(card)
            mod = pos % n
            if cow in cow_pos_mod:
                if cow_pos_mod[cow] != mod:
                    possible = False
                    break
            else:
                cow_pos_mod[cow] = mod
        if not possible:
            print(-1)
            continue
        
        mod_to_cow = {}
        for cow, mod in cow_pos_mod.items():
            if mod in mod_to_cow:
                possible = False
                break
            mod_to_cow[mod] = cow
        if not possible or len(mod_to_cow) != n:
            print(-1)
            continue
        
        p = [0] * n
        for mod in range(n):
            p[mod] = mod_to_cow[mod]
        print(' '.join(map(str, p)))

solve()