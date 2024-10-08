# D. Minimize the Difference
def solve(n, a):
    stack = []
    for item in a:
        sum = item
        count = 1
        while len(stack) > 0 and stack[-1][0] >= sum // count:
            cur_item_stack = stack.pop()
            sum += cur_item_stack[0] * cur_item_stack[1]
            count += cur_item_stack[1]
        stack.append((sum // count, count - sum % count))
        if sum % count != 0:
            stack.append((sum // count + 1, sum % count))
    return stack[-1][0] - stack[0][0]


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
