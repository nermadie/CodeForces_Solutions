# C. Snowfall
def solve(n, a):
  six_list = []
  three_list = []
  two_list = []
  other_list = []
  for i in a:
    if i % 6 == 0:
      six_list.append(i)
    elif i % 3 == 0:
      three_list.append(i)
    elif i % 2 == 0:
      two_list.append(i)
    else:
      other_list.append(i)

  result = six_list + three_list + other_list + two_list
  return " ".join(map(str, result))

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))