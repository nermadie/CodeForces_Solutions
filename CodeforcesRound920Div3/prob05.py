# E. Eat the Chip
def solve(h, w, a, b):
    # a[0] - b[0] % 2 == 1 -> Alice can win (0)
    # a[0] - b[0] % 2 == 0 -> Bob can win (1)
    able_winner = "Alice" if (a[0] - b[0]) % 2 == 1 else "Bob"
    if a[0] >= b[0]:
        return "Draw"
    # The able_loser cell that they can run away from the able_winner cell
    if able_winner == "Alice":
        num_of_b_moves = (b[0] - a[0] - 1) // 2
        left_most_b = b[1] - num_of_b_moves if b[1] - num_of_b_moves >= 1 else 1
        right_most_b = b[1] + num_of_b_moves if b[1] + num_of_b_moves <= w else w
        num_of_a_moves = num_of_b_moves + 1
        left_most_a = a[1] - num_of_a_moves if a[1] - num_of_a_moves >= 1 else 1
        right_most_a = a[1] + num_of_a_moves if a[1] + num_of_a_moves <= w else w
        if left_most_a <= left_most_b and right_most_a >= right_most_b:
            return able_winner
        else:
            return "Draw"
    else:
        num_of_b_moves = num_of_a_moves = (b[0] - a[0]) // 2
        left_most_a = a[1] - num_of_a_moves if a[1] - num_of_a_moves >= 1 else 1
        right_most_a = a[1] + num_of_a_moves if a[1] + num_of_a_moves <= w else w
        left_most_b = b[1] - num_of_b_moves if b[1] - num_of_b_moves >= 1 else 1
        right_most_b = b[1] + num_of_b_moves if b[1] + num_of_b_moves <= w else w
        if left_most_a >= left_most_b and right_most_a <= right_most_b:
            return able_winner
        else:
            return "Draw"


t = int(input())
for _ in range(t):
    h, w, xa, ya, xb, yb = map(int, input().split())
    a = (xa, ya)
    b = (xb, yb)
    print(solve(h, w, a, b))
