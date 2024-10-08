# Function to find a valid triplet for Monocarp
def find_triplet(n):
    # If n is divisible by 3, there is no valid triplet
    if n % 3 == 0:
        if n - 5 >= 7:
            return "YES\n1 4 {}".format(n - 5)
        else:
            return "NO"

    if (n - 1) % 3 == 0:
        if n - 1 - 4 >= 2:
            return "YES\n1 4 {}".format(n - 5)
        else:
            return "NO"
    elif (n - 1) % 3 == 1:
        if n - 1 - 2 >= 5:
            return "YES\n1 2 {}".format(n - 3)
        else:
            return "NO"
    else:
        return "NO"


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = find_triplet(n)
    print(result)
