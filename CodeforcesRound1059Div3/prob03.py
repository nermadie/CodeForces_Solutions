#C. Beautiful XOR
def solve(a, b):
  bin_a = bin(a)[2:]
  bin_b = bin(b)[2:]
  bin_b = bin_b.rjust(len(bin_a), "0")
  bin_a_len = len(bin_a)
  if b >= 2**bin_a_len:
    return -1
  elif b > a:
    print(1)
    return a ^ b
  elif b == a:
    return 0
  else:
    temp = ""
    check = False
    for i in range(bin_a_len):
      if bin_a[i] == "0" and bin_b[i] == "1":
        temp += "1"
        check = True
      else:
        temp += "0"
    if check:
      print(2)
      num_temp = int(temp, 2)
      return str(num_temp) + " " + str(num_temp^a^b)
    else:
      print(1)
      return a ^ b



t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))