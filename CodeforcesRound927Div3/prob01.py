# A. Thorns and Coins
def max_coins(path):
    max_coins = 0
    thorn_check = False
    for cell in path:
        if cell == ".":
            thorn_check = False
        elif cell == "@":
            max_coins += 1
            thorn_check = False
        elif cell == "*" and thorn_check == False:
            thorn_check = True
        elif cell == "*" and thorn_check == True:
            return max_coins
    return max_coins


# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    path = input().strip()
    print(max_coins(path))
