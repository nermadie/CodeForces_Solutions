# Aleksa and Stack
def construct_array(n):
    cur_num = 3
    print(cur_num, end=" ")
    for i in range(n - 1):
        if cur_num % 3 == 0:
            cur_num += 1
        else:
            cur_num += 2
        print(cur_num, end=" ")
    print()


# Input
t = int(input())
results = []

for _ in range(t):
    n = int(input())
    construct_array(n)
