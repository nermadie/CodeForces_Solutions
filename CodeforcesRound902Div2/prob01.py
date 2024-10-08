def find_missing_efficiency(efficiencies):
    return -sum(efficiencies)


# Read the number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    efficiencies = list(map(int, input().split()))

    missing_efficiency = find_missing_efficiency(efficiencies)
    print(missing_efficiency)
