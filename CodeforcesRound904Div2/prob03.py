# Medium Design
t = int(input())

for _ in range(t):
    segments = {}
    n, m = map(int, input().split())
    for i in range(n):
        l, r = list(map(int, input().split()))
        if segments.get(l) is None:
            segments[l] = [r]
        else:
            segments[l].append(r)
        if segments.get(r + 1) is None:
            segments[r + 1] = [l]
        else:
            segments[r + 1].append(l)
    ans = count_cur_intersect = count_1 = count_m = 0
    sorted_segments = sorted(segments.items(), key=lambda x: x[0])
    for x, value in sorted_segments:
        for y in value:
            if x > m:
                break
            if x <= y:
                if x == 1:
                    count_1 += 1
                if y == m:
                    count_m += 1
                count_cur_intersect += 1
            else:
                if y == 1:
                    count_1 -= 1
                count_cur_intersect -= 1
        ans = max(ans, count_cur_intersect - min(count_1, count_m))
    print(ans)
