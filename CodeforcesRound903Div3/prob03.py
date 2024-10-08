# Perfect Square
def min_operations_to_perfect_square(n, matrix):
    # [i][j] => [j][n - i - 1]
    count = 0
    for i in range(n // 2):
        for j in range(n // 2):
            char1 = ord(matrix[i][j])
            char2 = ord(matrix[j][n - i - 1])
            char3 = ord(matrix[n - i - 1][n - j - 1])
            char4 = ord(matrix[n - j - 1][i])
            max_char = max(char1, char2, char3, char4)
            count += max_char * 4 - char1 - char2 - char3 - char4
    return count


# Input
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [input().strip() for _ in range(n)]
    result = min_operations_to_perfect_square(n, matrix)
    print(result)
