# green_gold_dog, array and permutation
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    for item in a:
        index = sorted_a.index(item)
        sorted_a[index] = 0
        print(n - index, end=" ")
    print()
