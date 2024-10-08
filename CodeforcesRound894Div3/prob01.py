# Gift Carpet
def vika_likes_carpet(n, m, carpet):
    name = "vika"
    cur_char_index = 0
    for j in range(m):
        for i in range(n):
            if carpet[i][j] == name[cur_char_index]:
                cur_char_index += 1
                break
        if cur_char_index == 4:
            return "YES"
    return "NO"


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    carpet = [input() for _ in range(n)]
    print(vika_likes_carpet(n, m, carpet))
