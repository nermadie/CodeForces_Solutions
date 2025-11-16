# C. Remove Exactly Two
def solve(n, uv):
    if n <= 2:
        return 0

    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for u, v in uv:
        deg[u] += 1
        deg[v] += 1
        adj[u].append(v)
        adj[v].append(u)

    max_deg = max(deg[1:])
    candidates = [node for node in range(1, n + 1) if deg[node] == max_deg][:2]

    result = 0
    for candidate in candidates:
        for i in range(1, n + 1):
            if i == candidate:
                continue
            result = max(
                result, max_deg + deg[i] - 1 - (1 if candidate in adj[i] else 0)
            )

    return result


t = int(input())
for _ in range(t):
    n = int(input())
    uv = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(solve(n, uv))
