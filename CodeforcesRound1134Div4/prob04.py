def solve(n, s):
    alphabet = [
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    result = 0
    for i in alphabet:
        check = False
        for j in range(n // 2):
            left = s[j]
            right = s[n - j - 1]
            if (left > right and left >= i > right) or (
                left < right and left < i <= right
            ):
                check = True
                break
        if not check:
            result += 1
    return 25 - result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
