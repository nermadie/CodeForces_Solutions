# A. Max Plus Size
def solve(n, a):
    if n == 1:
        return a[0] + 1
    odd_ele = [value for index, value in enumerate(a) if index % 2 == 0]
    even_ele = [value for index, value in enumerate(a) if index % 2 != 0]
    return max(max(odd_ele) + len(odd_ele), max(even_ele) + len(even_ele))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
