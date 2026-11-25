# B. Did Not Go to Print
from collections import deque


def solve(n, s):
    check = [0] * n
    queue = deque()
    result = 0
    for i in range(len(s)):
        if s[i] == "1":
            queue.append(i)
        elif s[i] == "2":
            if queue:
                index = queue.pop()
                check[int(index)] = 1
            else:
                check[i] = 1
            result += 1
        else:
            check[i] = 1
            result += 1
    print(n - result)
    return " ".join(str(i + 1) for i in range(len(check)) if check[i] == 0)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
