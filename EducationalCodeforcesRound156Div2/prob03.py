# Function to find the character at a given position in string S
def remove_and_lex_minimal(s, longest_increase_subsequence):
    for i in range(longest_increase_subsequence[0], len(s) - 1):
        if s[i] > s[i + 1]:
            # Nếu tìm thấy ký tự lớn hơn ký tự tiếp theo, loại bỏ nó
            longest_increase_subsequence[0] = (
                longest_increase_subsequence[0] - 1
                if longest_increase_subsequence[0] > 0
                else 0
            )
            return s[:i] + s[i + 1 :]
        else:
            if i + 1 > longest_increase_subsequence[0]:
                longest_increase_subsequence[0] = i + 1

    # Nếu không tìm thấy ký tự nào để loại bỏ, loại bỏ ký tự cuối cùng
    return s[:-1]


def find_char_in_S(s1, pos):
    longest_increase_subsequence = [0]
    count_passed = 0
    while len(s1) + count_passed < pos:
        count_passed += len(s1)
        s1 = remove_and_lex_minimal(s1, longest_increase_subsequence)
    return s1[pos - 1 - count_passed]


# Read the number of test cases
t = int(input())


# Process each test case
for _ in range(t):
    # Read the input values for the test case
    s1 = input()
    pos = int(input())

    # Find and print the character at the given position
    result = find_char_in_S(s1, pos)
    print(result, end="")
