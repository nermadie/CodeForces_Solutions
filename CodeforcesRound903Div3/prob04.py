# Divide and Equalize
import math
from collections import Counter


def find_divisors(number):
    divisors = []
    temp_number = number
    i = 2
    while number != 1 and i <= temp_number:
        while True:
            if number % i == 0:
                divisors.append(i)
                number //= i
            else:
                break
        i += 1
    return divisors


def is_possible_to_equalize(n, arr):
    divisors = []
    for i in range(n):
        divisors.extend(find_divisors(arr[i]))
    counter = Counter(divisors)
    elements = counter.elements()
    for element in elements:
        if counter[element] % n != 0:
            return "NO"
    return "YES"


# Input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = is_possible_to_equalize(n, arr)
    print(result)
