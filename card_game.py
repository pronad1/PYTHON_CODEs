def beats(x, y, n):
    if x == 1 and y == n:
        return True
    if y == 1 and x == n:
        return False
    return x > y

def has_winning_card(candidate_cards, opponent_cards, n):
    for card in candidate_cards:
        all_beaten = True
        for opp in opponent_cards:
            if not beats(card, opp, n):
                all_beaten = False
                break
        if all_beaten:
            return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    alice = []
    bob = []
    for i in range(n):
        if s[i] == 'A':
            alice.append(i + 1)
        else:
            bob.append(i + 1)
    if has_winning_card(alice, bob, n):
        print("Alice")
    elif has_winning_card(bob, alice, n):
        print("Bob")
    else:
        print("Bob")