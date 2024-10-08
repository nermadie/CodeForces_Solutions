# Two Out of Three
def find_array_b(n, a):
    appeared = set()
    duplicate = {}
    for item in a:
        if item in appeared:
            duplicate[item] = 0
            if len(duplicate) == 2:
                break
        else:
            appeared.add(item)
    result = []
    check_first = True
    if len(duplicate) >= 2:
        for item in a:
            if item in duplicate and duplicate[item] == 0 and check_first == True:
                result.append("3")
                duplicate[item] = 1
                check_first = False
            elif item in duplicate and duplicate[item] == 0 and check_first == False:
                result.append("2")
                duplicate[item] = 1
            else:
                result.append("1")
        return result
    else:
        return [-1]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = find_array_b(n, a)
    if len(result) == 1:
        print(-1)
    else:
        print(*result)
