import re

n = int(input())
for _ in range(n):
    point = input()
    match = re.findall(r'<a href="(.*?|\.\.\.)" class="(.*?)"', point)
    print(match[0][0], match[0][1])
