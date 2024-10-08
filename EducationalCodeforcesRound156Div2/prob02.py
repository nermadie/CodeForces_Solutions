import math


# Function to calculate the distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Function to find the minimum power needed to illuminate the path
def minimum_power_to_illuminate(Px, Py, Ax, Ay, Bx, By):
    # Calculate distances from O to P, A to P, and B to P
    AO = distance(Ax, Ay, 0, 0)
    BO = distance(Bx, By, 0, 0)
    AP = distance(Ax, Ay, Px, Py)
    BP = distance(Bx, By, Px, Py)
    AB = distance(Ax, Ay, Bx, By)

    if AO < AB / 2 and AP < AB / 2:
        return max(AO, AP)
    elif BO < AB / 2 and BP < AB / 2:
        return max(BO, BP)

    _O = min(AO, BO)
    _P = min(AP, BP)

    larger = max(_O, _P)

    if AB / 2 >= larger:
        return AB / 2
    else:
        return larger


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the coordinates
    Px, Py = map(int, input().split())
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())

    # Calculate and print the minimum power needed to illuminate the path
    result = minimum_power_to_illuminate(Px, Py, Ax, Ay, Bx, By)
    print(result)
