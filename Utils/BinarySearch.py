# =========================
# BINARY SEARCH BOUNDARIES
# =========================
# Quy ước đặt tên:
#   asc   : mảng tăng dần
#   desc  : mảng giảm dần
#   first : chỉ số nhỏ nhất thỏa điều kiện
#   last  : chỉ số lớn nhất thỏa điều kiện
#
# Điều kiện:
#   more : >
#   less : <
#   ge   : >=
#   le   : <=
#   exact: ==
#
# Tham số:
#   arr        : mảng đã được sắp xếp
#   x          : giá trị target
#   l, r       : (optional) giới hạn tìm kiếm [l, r] (inclusive)
#                nếu không truyền -> tìm toàn bộ mảng
#
# Kết quả:
#   trả về index thỏa điều kiện
#   không tồn tại -> -1


def _init_lr(arr, l, r):
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1
    return l, r


# ===== ASCENDING ARRAY =====


# FIRST i sao cho arr[i] > x
def bs_asc_first_more(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > x:
            res = m
            r = m - 1  # ép sang trái để lấy FIRST
        else:
            l = m + 1
    return res


# LAST i sao cho arr[i] > x
def bs_asc_last_more(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > x:
            res = m
            l = m + 1  # ép sang phải để lấy LAST
        else:
            l = m + 1
    return res


# FIRST i sao cho arr[i] < x
def bs_asc_first_less(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
            res = m
            r = m - 1  # tìm FIRST
        else:
            r = m - 1
    return res


# LAST i sao cho arr[i] < x
def bs_asc_last_less(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
            res = m
            l = m + 1  # tìm LAST
        else:
            r = m - 1
    return res


# FIRST i sao cho arr[i] >= x
def bs_asc_first_ge(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res


# LAST i sao cho arr[i] <= x
def bs_asc_last_le(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] <= x:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res


# ===== DESCENDING ARRAY =====


# FIRST i sao cho arr[i] > x
def bs_desc_first_more(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > x:
            res = m
            r = m - 1  # giá trị lớn nằm bên trái
        else:
            l = m + 1
    return res


# LAST i sao cho arr[i] > x
def bs_desc_last_more(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > x:
            res = m
            l = m + 1  # ép sang phải để lấy LAST
        else:
            r = m - 1
    return res


# FIRST i sao cho arr[i] < x
def bs_desc_first_less(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res


# LAST i sao cho arr[i] < x
def bs_desc_last_less(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
            res = m
            l = m + 1
        else:
            l = m + 1
    return res


# ===== EXACT MATCH =====


# FIRST i sao cho arr[i] == x (asc)
def bs_first_exact_asc(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            res = m
            r = m - 1  # tìm FIRST
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res


# LAST i sao cho arr[i] == x (asc)
def bs_last_exact_asc(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            res = m
            l = m + 1  # tìm LAST
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res


# FIRST i sao cho arr[i] == x (desc)
def bs_first_exact_desc(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            res = m
            r = m - 1
        elif arr[m] < x:
            r = m - 1
        else:
            l = m + 1
    return res


# LAST i sao cho arr[i] == x (desc)
def bs_last_exact_desc(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            res = m
            l = m + 1
        elif arr[m] < x:
            r = m - 1
        else:
            l = m + 1
    return res


# ===== TEST =====
if __name__ == "__main__":
    arr_asc = [1, 3, 5, 5, 7]
    arr_desc = [7, 5, 5, 3, 1]

    print("ASC first > 4 :", bs_asc_first_more(arr_asc, 4))  # 2
    print("ASC last  > 4 :", bs_asc_last_more(arr_asc, 4))  # 3
    print("ASC first < 4 :", bs_asc_first_less(arr_asc, 4))  # 0
    print("ASC last  < 4 :", bs_asc_last_less(arr_asc, 4))  # 1
    print("ASC first>= 5 :", bs_asc_first_ge(arr_asc, 5))  # 2
    print("ASC last <= 5 :", bs_asc_last_le(arr_asc, 5))  # 3

    print("DESC first > 4:", bs_desc_first_more(arr_desc, 4))  # 0
    print("DESC last  > 4:", bs_desc_last_more(arr_desc, 4))  # 2
    print("DESC first < 4:", bs_desc_first_less(arr_desc, 4))  # 3
    print("DESC last  < 4:", bs_desc_last_less(arr_desc, 4))  # 4

    print("ASC first ==5 :", bs_first_exact_asc(arr_asc, 5))  # 2
    print("ASC last  ==5 :", bs_last_exact_asc(arr_asc, 5))  # 3
    print("DESC first==5 :", bs_first_exact_desc(arr_desc, 5))  # 1
    print("DESC last ==5 :", bs_last_exact_desc(arr_desc, 5))  # 2
