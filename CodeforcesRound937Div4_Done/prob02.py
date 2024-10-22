# B. Upscaling
def solve(n):
    for i in range(2 * n):
        for j in range(2 * n):
            cur_i = i // 2
            cur_j = j // 2
            if (cur_i + cur_j) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()


t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
