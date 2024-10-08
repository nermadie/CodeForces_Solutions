# D. Test of Love
def solve(n, m, k, a):
    a = "0" + a
    last_right = 0
    last_water = 0
    cur_pos = 0
    while True:
        if cur_pos + m > n:
            return "YES"
        check_to_water = True
        check_found_water = False
        for i in range(m + cur_pos, last_right, -1):
            last_right = cur_pos + m
            if a[i] == "W":
                if not check_found_water:
                    last_water = i
                    check_found_water = True
            if a[i] == "L":
                cur_pos = i
                check_to_water = False
                break
        if check_to_water:
            if last_right != last_water or k == 0:
                return "NO"
            k -= 1
            cur_pos = last_water
            while True:
                cur_pos += 1
                if cur_pos > n:
                    return "YES"
                if a[cur_pos] == "L":
                    break
                if a[cur_pos] == "W":
                    if k == 0:
                        return "NO"
                    k -= 1
                if a[cur_pos] == "C":
                    return "NO"


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input()
    print(solve(n, m, k, a))
