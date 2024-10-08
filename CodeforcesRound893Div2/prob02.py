# The Walkway
def min_cookies_petya_can_eat(n, m, d, sellers):


t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    sellers = list(map(int, input().split()))
    print(min_cookies_petya_can_eat(n, m, d, sellers))
