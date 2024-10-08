def min_announcement_cost(n, p, a, b):
    if n == 1:
        return p

    residents = list(zip(a, b, range(n)))
    residents.sort(key=lambda x: x[1])

    total_cost = 0
    announced = [False] * n  # Did they get an announcement?

    for i in range(n):
        max_announce, cost, resident_idx = residents[i]

        if not announced[resident_idx]:
            announced[resident_idx] = True
            total_cost += p

        if i == n - 1:
            return total_cost

        if cost >= p:
            for j in range(i + 1, n):
                if not announced[residents[j][2]]:
                    total_cost += p
            return total_cost
        else:
            count = 0
            for j in range(max_announce):
                while True:
                    next_resident_idx = residents[i + j + count + 1][2]
                    if not announced[next_resident_idx]:
                        announced[next_resident_idx] = True
                        total_cost += cost
                        if i + j + count + 1 == n - 1:
                            return total_cost
                        break
                    else:
                        count += 1

    return 0


# Read the number of test cases
t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cost = min_announcement_cost(n, p, a, b)
    print(cost)
