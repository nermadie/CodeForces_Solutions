# C. Vlad and a Sum of Sum of Digits
# Run with Python 3.8.5 will result better performance than PyPy
def sum_of_digits(n):
    result = 0
    divisor = 1
    while n >= divisor:
        higher_nums = n // (10 * divisor)
        current_digit = (n // divisor) % 10
        lower_nums = n % divisor
        result += (
            higher_nums * 45 * divisor
            + (((0 + current_digit - 1) * current_digit) // 2) * divisor
            + ((lower_nums + 1) * current_digit)
        )
        divisor *= 10
    return result


t = int(input())
result = []
for _ in range(t):
    n = int(input())
    result.append(sum_of_digits(n))
for i in result:
    print(i)
