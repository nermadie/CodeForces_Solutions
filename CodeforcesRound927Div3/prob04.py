# D. Card Game
def solve(n, trump, cards):
    suits = ["C", "D", "H", "S"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9"]
    dict_cards = {}
    for card in cards:
        suit = card[-1]
        value = card[0:-1]
        dict_cards.setdefault(suit, []).append(value)
    for suit in suits:
        if suit in dict_cards:
            dict_cards[suit].sort()
    remain_not_suit_card = []
    result = []
    for suit in suits:
        if suit != trump and suit in dict_cards:
            for i in range(len(dict_cards[suit]) // 2):
                result.append(
                    dict_cards[suit][i]
                    + suit
                    + " "
                    + dict_cards[suit][len(dict_cards[suit]) - i - 1]
                    + suit
                )

            if len(dict_cards[suit]) % 2 == 1:
                remain_not_suit_card.append(
                    dict_cards[suit][len(dict_cards[suit]) // 2] + suit
                )
    if trump in dict_cards:
        cur_trump = 0
        num_trump_card = len(dict_cards[trump])
        for card in remain_not_suit_card:
            cur_trump += 1
            if cur_trump <= num_trump_card:
                result.append(card + " " + dict_cards[trump][cur_trump - 1] + trump)
            else:
                print("IMPOSSIBLE")
                return
        if (num_trump_card - cur_trump) % 2 == 1:
            print("IMPOSSIBLE")
            return
        else:
            for i in range((num_trump_card - cur_trump) // 2):
                result.append(
                    dict_cards[trump][i + cur_trump]
                    + trump
                    + " "
                    + dict_cards[trump][num_trump_card - i - 1]
                    + trump
                )
    else:
        if len(remain_not_suit_card) > 0:
            print("IMPOSSIBLE")
            return
    for res in result:
        print(res)


t = int(input())
for _ in range(t):
    n = int(input())
    trump = input()
    cards = input().split()
    solve(n, trump, cards)
