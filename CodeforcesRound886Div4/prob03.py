# Word on the Paper
def extract_word(column):
    result = ""
    cur_col = -1
    for i in range(8):
        if cur_col != -1:
            if column[i][cur_col] != ".":
                result += column[i][cur_col]
                continue
            else:
                break
        for j in range(8):
            if column[i][j] != ".":
                result += column[i][j]
                cur_col = j
    return result


t = int(input())

for _ in range(t):
    column = []
    for _ in range(8):
        column.append(input())
    word = extract_word(column)
    print(word)
