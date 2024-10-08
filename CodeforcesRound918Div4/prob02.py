# B. Not Quite Latin Square
def find_missing_letter(square):
    for line in square:
        check = False
        for letter in line:
            if letter == "?":
                check = True
        tempList = ["A", "B", "C"]
        if check:
            for letter in line:
                if letter in tempList:
                    tempList.remove(letter)
            return tempList[0]


t = int(input())
for _ in range(t):
    square = [input() for _ in range(3)]
    print(find_missing_letter(square))
