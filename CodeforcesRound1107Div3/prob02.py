# B. Good times Good times
from collections import deque


def isGood(x, y):
    n = x * int(y)
    str_n = str(n)
    num_set = set(str_n)
    if len(num_set) <= 2:
        return True
    return False


def solve(x):
    # num_char = [
    #     "0",
    #     "1",
    #     "2",
    #     "3",
    #     "4",
    #     "5",
    #     "6",
    #     "7",
    #     "8",
    #     "9",
    # ]

    # queue = deque()
    # # item: (currentString, set(Already exist))
    # for i in range(1, 10):
    #     queue.append((str(i), set({str(i)})))
    # while queue:
    #     cur = queue.pop()
    #     if isGood(x, cur[0]):
    #         return cur[0]

    #     if len(cur[0]) == 10 or cur[0] == "1":
    #         continue

    #     if len(cur[1]) == 1:
    #         for nc in num_char:
    #             new_set = set(cur[1])
    #             new_set.add(nc)
    #             queue.append((cur[0] + nc, new_set))
    #     else:
    #         for c_in_set in cur[1]:
    #             queue.append((cur[0] + c_in_set, cur[1]))

    str_x = str(x)
    return "1" + "0" * (len(str_x) - 1) + "1"


t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))
