def max_employees_at_office(events):
    events.sort(
        key=lambda event: (event[0], -event[1])
    )  # Sắp xếp theo thời gian bắt đầu và loại sự kiện

    current_count = 0
    max_count = 0

    for event in events:
        if event[1] == "start":
            current_count += 1
        else:  # event[1] == 'end'
            current_count -= 1

        max_count = max(max_count, current_count)

    return max_count


# Đọc thông tin về n nhân viên
n = int(input())
events = []

# Đọc thông tin về thời gian đến và về của từng nhân viên và tạo danh sách sự kiện
for i in range(n):
    start, end = map(int, input().split())
    events.append((start, "start"))
    events.append((end, "end"))

result = max_employees_at_office(events)
print(result)
