# C. Black Circles
import math


def get_distance(xys, xyt):
    return (xys[0] - xyt[0]) ** 2 + (xys[1] - xyt[1]) ** 2


def solve(n, xy, xys, xyt):
    st_distance = get_distance(xys, xyt)
    for i in range(n):
        if get_distance(xy[i], xyt) <= st_distance:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    xy = []
    for _ in range(n):
        xy.append(list(map(int, input().split())))
    xs, ys, xt, yt = map(int, input().split())
    xys = [xs, ys]
    xyt = [xt, yt]
    print(solve(n, xy, xys, xyt))
