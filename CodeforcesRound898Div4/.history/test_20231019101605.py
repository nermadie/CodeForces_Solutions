n = int(input())
number_set = set(map(int, input().split()))
N = int(input())

for i in range(N):
    execute = input().split()
    if len(execute) == 1:
        number_set.pop()
    else:
        command = execute[0]
        x = int(execute[1])
        try:
            if command == "remove":
                number_set.remove(x)
            elif command == "discard":
                number_set.discard(x)
        except:
            continue

sum = 0
for item in number_set:
    sum += item
print(sum)
temp = [1, 2, 3]
temp.rotate()
print(temp)
