# Good Kid
def maximum_product(n, digits):
    digits.sort()
    digits[0] += 1
    product = 1
    for i in range(n):
        product *= digits[i]
    return product


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        digits = list(map(int, input().split()))

        print(maximum_product(n, digits))
