# Buttons
def determine_winner(a, b, c):
    last_player = "First"
    if c % 2 == 1:
        last_player = "Second"
    if last_player == "First":
        if a > b:
            return "First"
        else:
            return "Second"
    else:
        if b > a:
            return "Second"
        else:
            return "First"


t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print(determine_winner(a, b, c))
