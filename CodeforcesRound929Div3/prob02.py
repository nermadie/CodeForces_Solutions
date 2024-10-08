# B. Turtle Math: Fast Three Task
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    rem1_check = False
    rem2_check = False
    total_sum = 0
    for item in arr:
        total_sum += item
        if item % 3 == 1:
            rem1_check = True
        if item % 3 == 2:
            rem2_check = True
    if total_sum % 3 == 1:
        if rem1_check:
            print(1)
        else:
            print(2)
    elif total_sum % 3 ==2:
        print(1)
    else:
        print(0)



