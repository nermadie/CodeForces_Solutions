# Maximum Rounding
def maximize_x(x):
    if x[0] >= "5":
        return "1" + "0" * len(x)
    i = 0
    count4 = 0
    while i < len(x):
        if x[i] >= "5":
            x = x[: i - count4] + "0" * (len(x) - i + count4)
            if i - count4 == 0:
                x = "1" + x
            else:
                x = str(int(x[: i - count4]) + 1) + x[i - count4 :]
            break
        else:
            if x[i] == "4":
                count4 += 1
            else:
                count4 = 0
            i += 1

    return x


t = int(input())

for _ in range(t):
    x = input()

    print(maximize_x(x))
