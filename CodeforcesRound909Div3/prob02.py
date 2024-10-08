# 250 Thousand Tons of TNT
def get_all_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
        i += 1
    return divisors


def max_absolute_difference(n, weights):
    sum_all_prev_weights = [0] * n
    sum_all_prev_weights[0] = weights[0]
    for i in range(1, n):
        sum_all_prev_weights[i] = sum_all_prev_weights[i - 1] + weights[i]
    divisors = get_all_divisors(n)

    max_difference = 0

    for divisor in divisors:
        max_sum = 0
        min_sum = 100000000000000000
        for i in range(divisor - 1, n, divisor):
            sum_prev_weights = sum_all_prev_weights[i]
            if i - divisor >= 0:
                sum_prev_weights -= sum_all_prev_weights[i - divisor]
            if sum_prev_weights > max_sum:
                max_sum = sum_prev_weights
            if sum_prev_weights < min_sum:
                min_sum = sum_prev_weights
        if max_sum - min_sum > max_difference:
            max_difference = max_sum - min_sum
    return max_difference


# Input reading
t = int(input())

for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    print(max_absolute_difference(n, weights))
