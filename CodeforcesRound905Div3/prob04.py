# In Love
BOUND = None
MAX_BOUND = None
MIN_BOUND = None
def reset_minmax_bound():
    global BOUND, MAX_BOUND, MIN_BOUND
    cur_max_bound = MAX_BOUND
    cur_min_bound = MIN_BOUND
    for i in range(cur_max_bound, cur_min_bound-1, -1):
        if BOUND[i] != 0:
            MAX_BOUND = BOUND[i]
            break
    for i in range(cur_min_bound, cur_max_bound+1):
        if BOUND[i] != 0:
            MIN_BOUND = BOUND[i]
            break


def solve(sign, l, r):
    global BOUND
    max_bound =
    if sign == "+":
        BOUND[l] += 1
        BOUND[r] += 1
        reset_minmax_bound()
        sum_min_to_max = (MAX)
        return "YES"
    else:  # sign == "-"
        BOUND[l] -= 1
        BOUND[r] -= 1
        reset_minmax_bound()
        return "NO"


t = int(input())
for _ in range(t):
    command = input().split()
    BOUND = [0] * 100001
    MAX_BOUND = 100001
    MIN_BOUND = 0
    print(solve(command[0], int(command[1]), int(command[2])))
