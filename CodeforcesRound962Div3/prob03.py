# C. Sort
def solve(n, q, a, b, lr):
    char_set = set(a).union(set(b))
    char_dict_a = {c: [0] for c in char_set}
    char_dict_b = {c: [0] for c in char_set}
    for i in range(n):
        for c in char_set:
            char_dict_a[c].append(char_dict_a[c][-1])
            char_dict_b[c].append(char_dict_b[c][-1])
        char_dict_a[a[i]][i + 1] = char_dict_a[a[i]][i] + 1
        char_dict_b[b[i]][i + 1] = char_dict_b[b[i]][i] + 1
    for l, r in lr:
        count = 0
        for c in char_set:
            count += abs(
                (char_dict_a[c][r] - char_dict_a[c][l - 1])
                - (char_dict_b[c][r] - char_dict_b[c][l - 1])
            )
        print(count // 2)


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = input()
    b = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    solve(n, q, a, b, lr)
