# A. Vlad and the Best of Five
t = int(input())

for _ in range(t):
    s = input()

    count_A = s.count('A')
    count_B = s.count('B')

    if count_A > count_B:
        print('A')
    else:
        print('B')
