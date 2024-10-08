# Prime Deletion
def find_prime_sequence(digits):
    for char in digits:
        if char == "7":
            return "71"
        if char == "1":
            return "17"


t = int(input())

for _ in range(t):
    digits = input().strip()
    print(find_prime_sequence(digits))
