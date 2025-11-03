# A. Blackboard Game
def solve(n):
  if n % 2 != 0:
    print("Alice")
    return
  groups = [0] * 4 # 4k, 4k+1, 4k+2, 4k+3
  for i in range(n):
    groups[i % 4] += 1

  if groups[0] == groups[3] and groups[1] == groups[2]:
    print("Bob")
  else:
    print("Alice")



t = int(input())
for _ in range(t):
  n = int(input())
  solve(n)