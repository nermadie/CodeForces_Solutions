# C. Password Cracking
def solve(n):
    result = ""
    reversed_check = False
    while len(result) < n:
        if not reversed_check:
            print("? " + result + "1", flush=True)
            check = input()
            print()
            if check == "1":
                result += "1"
                continue
            print("? " + result + "0", flush=True)
            check = input()
            print()
            if check == "1":
                result += "0"
                continue
            reversed_check = True
        print("? 1" + result, flush=True)
        check = input()
        print()
        if check == "1":
            result = "1" + result
            continue
        else:
            result = "0" + result
            continue
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    print("!", solve(n), flush=True)
    print()
