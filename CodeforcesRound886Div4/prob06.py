# We Were Both Children
def max_frogs_catched(n, hops):
    dict_hops = [0] * (n + 1)
    catch_hops = [0] * (n + 1)
    for hop in hops:
        if hop > n:
            continue
        dict_hops[hop] += 1
    for i in range(1, n + 1):
        if dict_hops[i] == 0:
            continue
        cur_hop = i
        while cur_hop <= n:
            catch_hops[cur_hop] += dict_hops[i]
            cur_hop += i
    return max(catch_hops)


t = int(input())
for _ in range(t):
    n = int(input())
    hops = list(map(int, input().split()))

    result = max_frogs_catched(n, hops)
    print(result)
