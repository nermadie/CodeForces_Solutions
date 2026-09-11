def solve(n, a, b):
    odd_count_1_in_a = 0
    even_count_1_in_a = 0
    odd_count_1_in_b = 0
    even_count_1_in_b = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == "1":
                even_count_1_in_a += 1
            if b[i] == "1":
                even_count_1_in_b += 1
        else:
            if a[i] == "1":
                odd_count_1_in_a += 1
            if b[i] == "1":
                odd_count_1_in_b += 1
    if odd_count_1_in_a == odd_count_1_in_b and even_count_1_in_a == even_count_1_in_b:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    print(solve(n, a, b))
