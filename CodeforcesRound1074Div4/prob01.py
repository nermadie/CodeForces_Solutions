# A. Perfect Root
def perfect_root(n):
    return " ".join([str(i + 1) for i in range(n)])


t = int(input())
for _ in range(t):
    n = int(input())
    print(perfect_root(n))
