# B. Startup
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    brand_costs = [0] * k
    for _ in range(k):
        a, b = map(int, input().split())
        brand_costs[a - 1] += b
    brand_costs.sort(reverse=True)
    print(sum(brand_costs[: min(n, k)]))
