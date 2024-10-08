# E. Romantic Glasses
def find_contiguous_subarray(n, arr):
    odd_list = [0]
    even_list = [0]
    odd_sum = 0
    even_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += arr[i - 1]
            even_list.append(even_sum)
        else:
            odd_sum += arr[i - 1]
            odd_list.append(odd_sum)
    isOddEnd = n % 2 == 1
    for i in range(0, len(odd_list) - 1):
        for j in range(i + 1, len(odd_list)):
            if odd_list[j] - odd_list[i] == even_list[j - 1] - even_list[i]:
                return "YES"
            if j != len(odd_list) - 1 or not isOddEnd:
                if odd_list[j] - odd_list[i] == even_list[j] - even_list[i]:
                    return "YES"
            if i > 0:
                if odd_list[j] - odd_list[i] == even_list[j - 1] - even_list[i - 1]:
                    return "YES"
                if j != len(odd_list) - 1 or not isOddEnd:
                    if odd_list[j] - odd_list[i] == even_list[j] - even_list[i - 1]:
                        return "YES"

    return "NO"


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_contiguous_subarray(n, arr))
