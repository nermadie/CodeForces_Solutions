def construct_array(n, a):
    b = [0] * n  # Khởi tạo mảng b với các phần tử ban đầu là 0

    for i in range(n - 1):
        b[i + 1] = a[i] ^ b[i]  # Tính toán phần tử tiếp theo của b

    return b  # Trả về mảng b


# Đọc đầu vào
n = int(input())
a = list(map(int, input().split()))

# Sử dụng hàm để tạo mảng b
result = construct_array(n, a)

# In ra mảng b
print(*result)
