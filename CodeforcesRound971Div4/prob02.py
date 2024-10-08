# B. osu!mania
# ------------------------------------------
def solve(n, beatmap):
    result = ""
    for line in beatmap:
        for i in range(len(line)):
            if line[i] == "#":
                result += str(i + 1) + " "
    return result[:-1][::-1]


# Input processing
t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of rows in the beatmap
    beatmap = [input() for _ in range(n)]  # Read the n lines of the beatmap
    result = solve(n, beatmap)
    # Output the result for the current test case
    print(" ".join(map(str, result)))
