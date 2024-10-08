# Chemistry
def is_possible_palindrome(s, k):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    if odd_count > k + 1:
        return "NO"
    else:
        return "YES"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(is_possible_palindrome(s, k))
