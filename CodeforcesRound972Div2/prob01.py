# A. Simple Palindrome
def solve(n):
    vowels = ["a", "e", "i", "o", "u"]
    count = n // 5
    remain = n % 5
    result = []
    for i in range(5):
        if remain:
            result.append(vowels[i] * (count + 1))
            remain -= 1
        else:
            result.append(vowels[i] * count)
    return "".join(result)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
