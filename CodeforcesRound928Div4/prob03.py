# C. Vlad and a Sum of Sum of Digits
def sum_of_digits(n):
    buffer10 = 0
    buffer100 = 0
    buffer1000 = 0
    buffer10000 = 0
    result = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            buffer10 += 1
        if i % 100 == 0:
            buffer100 += 1
            buffer10 = 0
        if i % 1000 == 0:
            buffer1000 += 1
            buffer10 = 0
            buffer100 = 0
        if i % 10000 == 0:
            buffer10000 += 1
            buffer10 = 0
            buffer100 = 0
            buffer1000 = 0
        result += buffer10 + buffer100 + buffer1000 + buffer10000 + i % 10
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    print(sum_of_digits(n))
