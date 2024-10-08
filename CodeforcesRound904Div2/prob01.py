# Simple Design
def sumOfDigits(value):
    value_str = str(value)
    sum = 0
    for i in range(len(value_str)):
        sum += int(value_str[i])
    return sum


def addToDigits(value):
    i = 10
    while (value % i - value % (i // 10)) // i == 9:
        if i > value:
            break
        i *= 10
    return value + i // 10


def find_smallest_k_beautiful(x, k):
    remainder = sumOfDigits(x) % k
    diff = k - remainder

    while True:
        if sumOfDigits(x) % k == 0:
            return x
        else:
            x = addToDigits(x)


t = int(input())

for _ in range(t):
    x, k = map(int, input().split())
    print(find_smallest_k_beautiful(x, k))
