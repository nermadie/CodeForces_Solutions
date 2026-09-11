def solve(n, a, b):
    odd_count_1_in_a = 0
    even_count_1_in_a = 0
    odd_count_1_in_b = 0
    even_count_1_in_b = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == "1":
                even_count_1_in_a += 1
            if b[i] == "1":
                even_count_1_in_b += 1
        else:
            if a[i] == "1":
                odd_count_1_in_a += 1
            if b[i] == "1":
                odd_count_1_in_b += 1

    if odd_count_1_in_a != odd_count_1_in_b or even_count_1_in_a != even_count_1_in_b:
        return -1

    odd_list_a = [0] * odd_count_1_in_a
    even_list_a = [0] * even_count_1_in_a
    odd_list_b = [0] * odd_count_1_in_b
    even_list_b = [0] * even_count_1_in_b
    odd_list_a_index = 0
    even_list_a_index = 0
    odd_list_b_index = 0
    even_list_b_index = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == "1":
                even_list_a[even_list_a_index] = i
                even_list_a_index += 1
            if b[i] == "1":
                even_list_b[even_list_b_index] = i
                even_list_b_index += 1
        else:
            if a[i] == "1":
                odd_list_a[odd_list_a_index] = i
                odd_list_a_index += 1
            if b[i] == "1":
                odd_list_b[odd_list_b_index] = i
                odd_list_b_index += 1

    result = 0
    for i in range(odd_count_1_in_a):
        result += abs(odd_list_a[i] - odd_list_b[i])
    for i in range(even_count_1_in_a):
        result += abs(even_list_a[i] - even_list_b[i])
    return result // 2


t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    print(solve(n, a, b))
