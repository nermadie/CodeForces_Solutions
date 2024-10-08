# Sets and Union
ELEMENT_DICT = {}


def get_2nd_max_len_union(max_len):
    global ELEMENT_DICT
    len_list = {}
    for key, value in ELEMENT_DICT.items():
        len_list[key] = len(value)
    second_max_len = 0
    for key, value in ELEMENT_DICT.items():
        temp_len_list = dict(len_list)
        count = 0
        for item in value:
            for key2, value2 in ELEMENT_DICT.items():
                if item in value2:
                    temp_len_list[key2] -= 1
                    if temp_len_list[key2] == 0:
                        count += 1
        second_max_len = max(second_max_len, max_len - count)
    return second_max_len


t = int(input())
for _ in range(t):
    ELEMENT_DICT = {}
    n = int(input())
    sets = []
    union_all = set()
    max_len = 0

    for i in range(n):
        set_data = list(map(int, input().split()))
        temp_input_set = set_data[1:]
        for item in temp_input_set:
            if item not in ELEMENT_DICT:
                ELEMENT_DICT[item] = set()
            ELEMENT_DICT[item].add(i)
    max_len = len(ELEMENT_DICT)

    print(get_2nd_max_len_union(max_len))
