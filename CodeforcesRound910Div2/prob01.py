def modify_string(n, k, s):
    temp = [0] * n
    countA = 0
    countB = 0
    for i in range(n):
        if s[i] == "A":
            countA += 1
            temp[i] = countA
        else:
            countB -= 1
            temp[i] = countB
    countB = -countB
    if countB != k:
        print(1)
        for i in range(n):
            if temp[i] == k - countB:
                print(i + 1, end=" ")
                if temp[i] < 0:
                    print("A")
                else:
                    print("B")
    else:
        print(0)


t = int(input())

for _ in range(t):
    nk = list(map(int, input().split()))
    s = input()
    modify_string(*nk, s)
