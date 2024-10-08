t = int(input())

for _ in range(t):
    ans1 = 0
    ans2 = 1
    string = input()
    cnt = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            cnt += 1
            ans1 += 1
            ans2 *= ans1
            ans2 %= 998244353

        else:
            ans2 *= cnt
            cnt = 1

    ans2 *= cnt

    print(ans1, ans2 % 998244353)
