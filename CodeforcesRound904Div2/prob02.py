# Haunted House
# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    binary_str = input().strip()
    count = 0
    temp = 0
    for i in range(n):
        if binary_str[n - i - 1] == "0":
            temp = i - count + temp
            count += 1
            print(temp, end=" ")
    for i in range(n - count):
        print(-1, end=" ")
    print()
