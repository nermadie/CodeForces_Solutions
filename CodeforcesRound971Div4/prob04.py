# D. Satyam and Counting
# ----------------------
def solve(n, points):
    result = 0
    point_dict = dict()
    for point in points:
        point_dict.setdefault(point[0], [False, False])
        point_dict[point[0]][point[1]] = True
        if point_dict[point[0]] == [True, True]:
            result += n - 2
        p_prev_2 = point_dict.get(point[0] - 2)
        p_prev_1 = point_dict.get(point[0] - 1)
        p_next_1 = point_dict.get(point[0] + 1)
        p_next_2 = point_dict.get(point[0] + 2)
        if point[1] == 0:
            if (
                p_prev_1 != None
                and p_next_1 != None
                and p_prev_1[1] == True
                and p_next_1[1] == True
            ):
                result += 1
            if (
                p_prev_1 != None
                and p_prev_2 != None
                and p_prev_1[1] == True
                and p_prev_2[0] == True
            ):
                result += 1
            if (
                p_next_1 != None
                and p_next_2 != None
                and p_next_1[1] == True
                and p_next_2[0] == True
            ):
                result += 1
        if point[1] == 1:
            if (
                p_prev_1 != None
                and p_next_1 != None
                and p_prev_1[0] == True
                and p_next_1[0] == True
            ):
                result += 1
            if (
                p_prev_1 != None
                and p_prev_2 != None
                and p_prev_1[0] == True
                and p_prev_2[1] == True
            ):
                result += 1
            if (
                p_next_1 != None
                and p_next_2 != None
                and p_next_1[0] == True
                and p_next_2[1] == True
            ):
                result += 1
    return result


# Input processing
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of points
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, points))
