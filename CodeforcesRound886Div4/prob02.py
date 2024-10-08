# Ten Words of Wisdom
def winner_of_show(n, responses):
    result = 0
    index = -1
    for i in range(len(responses)):
        if responses[i][0] <= 10:
            if responses[i][1] > result:
                result = responses[i][1]
                index = i
    return index + 1


t = int(input())

for _ in range(t):
    n = int(input())
    responses = [tuple(map(int, input().split())) for _ in range(n)]
    print(winner_of_show(n, responses))
