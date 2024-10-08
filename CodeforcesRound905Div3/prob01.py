# Morning
def calculate_time_to_enter_pin(pin):
    current_position = 0
    total_time = 0
    programs = "1234567890"

    for digit in pin:
        difference = abs(programs.find(digit) - current_position)
        total_time += difference + 1
        current_position = programs.find(digit)

    return total_time


t = int(input())
for _ in range(t):
    pin = input()
    print(calculate_time_to_enter_pin(pin))
