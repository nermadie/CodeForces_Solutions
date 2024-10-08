# A. Recovering a Small String
def decode_word(n):
  output = ""
  if n > 27:
      output = 'z' + output
      n -= 26
  else:
      output = chr(n + 96 - 2) + output
      return "aa" + output

  if n > 26:
      output = 'z' + output
      n -= 26
  else:
      output = chr(n + 96 - 1) + output
      return "a" + output
  return chr(n + 96) + output

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    print(decode_word(n))
