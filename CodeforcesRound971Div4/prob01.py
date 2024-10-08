# A. Minimize!
# -----------------
def solve(a, b):
    return b - a


# Input processing
t = int(input())  # Number of test cases

# Process each test case
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))
