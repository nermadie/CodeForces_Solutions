# C. Anya and 1100
def solve(s, q, queries):
    cur_count = 0
    for i in range(len(s) - 3):
        if s[i : i + 4] == "1100":
            cur_count += 1
    s = list(s)
    for i, v in queries:
        cur_pos = int(i) - 1
        for i in range(4):
            if cur_pos - i >= 0 and cur_pos - i + 3 < len(s):
                cur_substring_list = s[cur_pos - i : cur_pos - i + 4]
                cur_substring_string = "".join(cur_substring_list)
                if cur_substring_string == "1100":
                    cur_count -= 1
                cur_substring_list[int(i)] = v
                cur_substring_string = "".join(cur_substring_list)
                if cur_substring_string == "1100":
                    cur_count += 1
        s[cur_pos] = v
        if cur_count > 0:
            print("YES")
        else:
            print("NO")


t = int(input())
for _ in range(t):
    s = input()
    q = int(input())
    queries = []
    for _ in range(q):
        i, v = input().split()
        queries.append((i, v))
    solve(s, q, queries)
