# C. Make Equal Again
def can_equalize_water(n, containers):
  left_sequence = 1
  right_sequence = 1
  for i in range (1, len(containers)):
    if containers[i] == containers[i-1]:
      left_sequence += 1
    else:
      break
  if left_sequence == n:
    return 0
  for i in range (len(containers)-2, -1, -1):
    if containers[i] == containers[i+1]:
      right_sequence += 1
    else:
      break

  if containers[0] == containers[-1]:
    return n - left_sequence - right_sequence
  else:
    return n - max(left_sequence, right_sequence)

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    containers = list(map(int, input().split()))
    print(can_equalize_water(n, containers))