# D. Ingenuity-2
def solve(n, s):
    N_count = 0
    S_count = 0
    W_count = 0
    E_count = 0
    for c in s:
        if c == "N":
            N_count += 1
        elif c == "S":
            S_count += 1
        elif c == "W":
            W_count += 1
        else:
            E_count += 1
    if (N_count - S_count) % 2 == 1 or (W_count - E_count) % 2 == 1:
        return "NO"
    R_moves = {"N": 0, "S": 0, "W": 0, "E": 0}
    H_moves = {"N": 0, "S": 0, "W": 0, "E": 0}
    common_NS = min(N_count, S_count)
    common_EW = min(W_count, E_count)
    if common_NS % 2 == 0:
        R_moves["N"] = R_moves["S"] = common_NS // 2
        H_moves["N"] = H_moves["S"] = common_NS // 2
    else:
        R_moves["N"] = R_moves["S"] = common_NS // 2 + 1
        H_moves["N"] = H_moves["S"] = common_NS // 2
    if common_EW % 2 == 0:
        R_moves["W"] = R_moves["E"] = common_EW // 2
        H_moves["W"] = H_moves["E"] = common_EW // 2
    else:
        R_moves["W"] = R_moves["E"] = common_EW // 2
        H_moves["W"] = H_moves["E"] = common_EW // 2 + 1

    if N_count > S_count:
        H_moves["N"] += (N_count - S_count) // 2
        R_moves["N"] += (N_count - S_count) // 2
    else:
        H_moves["S"] += (S_count - N_count) // 2
        R_moves["S"] += (S_count - N_count) // 2
    if W_count > E_count:
        H_moves["W"] += (W_count - E_count) // 2
        R_moves["W"] += (W_count - E_count) // 2
    else:
        H_moves["E"] += (E_count - W_count) // 2
        R_moves["E"] += (E_count - W_count) // 2
    if sum(R_moves.values()) == 0 or sum(H_moves.values()) == 0:
        return "NO"
    result = []
    for move in s:
        if move == "N":
            if R_moves["N"] > 0:
                result.append("R")
                R_moves["N"] -= 1
            else:
                result.append("H")
        elif move == "S":
            if R_moves["S"] > 0:
                result.append("R")
                R_moves["S"] -= 1
            else:
                result.append("H")
        elif move == "W":
            if R_moves["W"] > 0:
                result.append("R")
                R_moves["W"] -= 1
            else:
                result.append("H")
        else:
            if R_moves["E"] > 0:
                result.append("R")
                R_moves["E"] -= 1
            else:
                result.append("H")
    return "".join(result)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
