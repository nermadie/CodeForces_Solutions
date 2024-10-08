# D. Sakurako's Hobby
def solve(n, p, s):
    result = [[0, False] for _ in range(n)]
    for i in range(n):
        if result[i][1] == False:
            black_traveled = 0
            traveled = set()
            traveled.add(i)
            cur_value = p[i] - 1
            while cur_value != i:
                traveled.add(cur_value)
                if s[cur_value] == "0":
                    black_traveled += 1
                cur_value = p[cur_value] - 1
            if s[i] == "0":
                black_traveled += 1
            for item in traveled:
                result[item] = [black_traveled, True]
    for item in result:
        print(item[0], end=" ")
    print()


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    solve(n, p, s)
