# Prefix Permutation Sums
def is_possible_permutation(n, prefix_sums):
    appeared_numbers = [0] * (n + 1)
    missing = 0
    if prefix_sums[0] > n:
        if prefix_sums[0] > 2 * n - 1:
            return "NO"
        missing = prefix_sums[0]
    else:
        appeared_numbers[prefix_sums[0]] = 1
    for i in range(1, n - 1):
        num = prefix_sums[i] - prefix_sums[i - 1]
        if num > n:
            if missing == 0:
                missing = num
            else:
                return "NO"
        elif appeared_numbers[num] == 0:
            appeared_numbers[num] = 1
        else:
            if missing == 0:
                if num > 2 * n - 1:
                    return "NO"
                missing = num
            else:
                return "NO"
    if missing == 0:
        return "YES"
    for i in range(1, n + 1):
        if (
            1 <= missing - i <= n
            and i != missing - i
            and appeared_numbers[i] == 0
            and appeared_numbers[missing - i] == 0
        ):
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    prefix_sums = list(map(int, input().split()))
    print(is_possible_permutation(n, prefix_sums))
