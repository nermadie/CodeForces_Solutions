# Short Sort
def is_possible(cards):
    temp_cards = [char for char in cards]
    temp_cards.sort()
    sorted_cards = "".join(temp_cards)
    count = 0
    char1 = ""
    char1_ref = ""
    char2 = ""
    char2_ref = ""
    for i in range(len(cards)):
        if cards[i] != sorted_cards[i]:
            count += 1
            if count == 3:
                return "NO"
            if count == 1:
                char1 = cards[i]
                char1_ref = sorted_cards[i]
            if count == 2:
                char2 = cards[i]
                char2_ref = sorted_cards[i]
    if char1 == char2_ref and char2 == char1_ref:
        return "YES"


t = int(input())

for _ in range(t):
    cards = input()
    print(is_possible(cards))
