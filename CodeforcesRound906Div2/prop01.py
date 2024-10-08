# Doremy's Paint 3
def is_good_array(n, arr):
    first = arr[0]
    second = None
    count_first = 1
    count_second = 0
    for i in range(1, n):
        if second == None and arr[i] != first:
            second = arr[i]
            count_second = 1
        elif second != None and arr[i] != first and arr[i] != second:
            return "No"
        elif arr[i] == first:
            count_first += 1
        else:
            count_second += 1
    if abs(count_first - count_second) <= 1:
        return "Yes"
    return "No" if second != None else "Yes"


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(is_good_array(n, arr))
