# C. Turtle Fingers: Count the Values of k
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factors(n):
    prime_factor_dict = {}
    while not n % 2:
        if 2 in prime_factor_dict:
            prime_factor_dict[2] += 1
        else:
            prime_factor_dict[2] = 1
        n //= 2
    while not n % 3:
        if 3 in prime_factor_dict:
            prime_factor_dict[3] += 1
        else:
            prime_factor_dict[3] = 1
        n //= 3
    i = 5
    while n != 1:
        if is_prime(i):
            while not n % i:
                if i in prime_factor_dict:
                    prime_factor_dict[i] += 1
                else:
                    prime_factor_dict[i] = 1
                n //= i
        i += 2

    return prime_factor_dict

def distinct_k_values(a, b, l):
    large = max(a, b)
    small = min(a, b)
    small_clone = small
    while(large >= small_clone):
        if large == small_clone:
            count_small = 0
            while(l % small == 0):
                l //= small
                count_small += 1
            return count_small + 1
        small_clone *= small

    l_factors = prime_factors(l)
    large_factors = prime_factors(large)
    small_factors = prime_factors(small)
    max_large = 1000001
    result = 0
    for factor in large_factors:
        if factor in l_factors:
            max_large = min(max_large, l_factors[factor] // large_factors[factor])
        else:
            max_large = 0
            break
    if max_large == 1000001:
        max_large = 0
    for i in range(max_large + 1):
        if i > 0:
            for factor in large_factors:
                l_factors[factor] -= large_factors[factor]
        max_small = 1000001
        for factor in small_factors:
            if factor in l_factors:
                max_small = min(max_small, l_factors[factor] // small_factors[factor])
            else:
                max_small = 0
                break
        if max_small == 1000001:
            max_small = 0
        result += max_small + 1
    return result



t = int(input())

for _ in range(t):
    a, b, l = map(int, input().split())
    print(distinct_k_values(a, b, l))

