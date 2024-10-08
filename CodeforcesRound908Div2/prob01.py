# Secret Sport
def determine_game_winner(n, plays):
    for i in range(1, n + 1):
        countAwin = 0
        countBwin = 0
        countA = 0
        countB = 0
        for j in range(n):
            if plays[j] == "A":
                countA += 1
                if countA == i:
                    countAwin += 1
                    countA = 0
                    countB = 0
            else:
                countB += 1
                if countB == i:
                    countBwin += 1
                    countA = 0
                    countB = 0
        if countA == 0 and countB == 0:
            if countAwin > countBwin and plays[-1] == "A":
                return "A"
            elif countBwin > countAwin and plays[-1] == "B":
                return "B"
    return "?"


t = int(input())
for _ in range(t):
    n = int(input())
    plays = input().strip()
    print(determine_game_winner(n, plays))
