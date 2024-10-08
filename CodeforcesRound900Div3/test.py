import bisect

arr = [1, 3, 5, 7, 9]
a = int(input("Nhập số a: "))

lower_bound = bisect.bisect_left(arr, a)
upper_bound = bisect.bisect_right(arr, a)

print(lower_bound, upper_bound, sep=" ")
