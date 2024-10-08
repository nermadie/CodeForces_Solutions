# D. Divisible Pairs
def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))


def count_beautiful_pairs(n, x, y, arr):
    result1 = 0
    result2 = 0
    dict_inp = {}
    group_ai_mod_x = {}
    group_ai_mod_y = {}
    for item in arr:
        if item in dict_inp:
            dict_inp[item] += 1
        else:
            dict_inp[item] = 1
            temp1 = item % x
            temp2 = item % y
            if temp1 in group_ai_mod_x:
                group_ai_mod_x[temp1].append(item)
            else:
                group_ai_mod_x[temp1] = [item]
            if temp2 in group_ai_mod_y:
                group_ai_mod_y[temp2].append(item)
            else:
                group_ai_mod_y[temp2] = [item]
    # print(dict_inp, group_ai_mod_x, group_ai_mod_y, sep="\n")
    for item in dict_inp.keys():
        temp1 = (x - item % x) % x
        temp2 = item % y
        if not temp1 in group_ai_mod_x or not temp2 in group_ai_mod_y:
            continue
        temp_arr1 = group_ai_mod_x[(x - item % x) % x]
        temp_arr2 = group_ai_mod_y[item % y]
        intersection_arr = intersection(temp_arr1, temp_arr2)
        # print(item, intersection_arr, sep=": ")

        for intersection_item in intersection_arr:
            if intersection_item != item:
                result1 += dict_inp[intersection_item] * dict_inp[item]
            else:
                result2 += (dict_inp[item] * (dict_inp[item] - 1)) // 2
    return result1 // 2 + result2


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    print(count_beautiful_pairs(n, x, y, arr))
