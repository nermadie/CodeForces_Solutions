# Smilo and Monsters
def handle_remaining(remaining):
    if remaining == 0:
        return 0
    elif remaining == 1:
        return 1
    else:
        return (remaining // 2) + 1 + (remaining % 2)


def minimum_attacks(n, hordes):
    hordes.sort()
    left = 0
    right = len(hordes) - 1
    stack_combo = 0
    attacks = 0
    while left < right:
        stack_combo += hordes[left]
        attacks += hordes[left]
        left += 1
        if stack_combo > hordes[right]:
            if left == right:
                stack_combo -= hordes[right]
                attacks += 1 + handle_remaining(stack_combo) - stack_combo
            else:
                stack_combo -= hordes[right]
                right -= 1
                attacks += 1
                if left == right:
                    attacks += (
                        handle_remaining(stack_combo + hordes[left]) - stack_combo
                    )
        elif stack_combo == hordes[right]:
            stack_combo = 0
            right -= 1
            attacks += 1
            if right == left:
                attacks += handle_remaining(hordes[left])
        elif stack_combo < hordes[right] and left == right:
            attacks += handle_remaining(stack_combo + hordes[right]) - stack_combo
    return attacks


t = int(input())

for _ in range(t):
    n = int(input())
    hordes = list(map(int, input().split()))

    print(minimum_attacks(n, hordes))
