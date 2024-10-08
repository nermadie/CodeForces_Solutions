# A. Odd One Out
def find_unique_value(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(find_unique_value(a, b, c))
