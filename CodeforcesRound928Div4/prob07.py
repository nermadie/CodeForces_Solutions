# G. Vlad and Trouble at MIT
def solve(n, a, s):
    connected_node = {}
    for i in range(2, n + 1):
        connected_node.setdefault(i, set())
        connected_node[i].add(a[i - 2])
        connected_node.setdefault(a[i - 2], set())
        connected_node[a[i - 2]].add(i)
    party_nodes = set()
    sleep_nodes = set()
    for i in range(n):
        if s[i] == "P":
            party_nodes.add(i + 1)
        elif s[i] == "S":
            sleep_nodes.add(i + 1)
    if len(party_nodes) == 0:
        return 0
    stack = [party_nodes.pop()]
    result = 0
    while stack or party_nodes:
        if len(stack) == 0 and len(party_nodes) != 0:
            stack.append(party_nodes.pop())
        current_node = stack.pop()
        print("current_node", current_node)
        for neighbor in connected_node[current_node]:
            if neighbor == current_node:
                continue
            if neighbor in sleep_nodes:
                result += 1
                continue
            if neighbor in party_nodes:
                party_nodes.remove(neighbor)
            stack.append(neighbor)
    return connected_node, {"result": result}


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    print(solve(n, a, s))
