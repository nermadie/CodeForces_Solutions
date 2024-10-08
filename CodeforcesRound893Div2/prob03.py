# Yet Another Permutation Problem
def generate_max_score_permutation(n):
    ref_arr = [0] * (n + 1)
    result = []
    for i in range(1, n + 1):
        if ref_arr[i] == 0:
            while i <= n:
                ref_arr[i] = 1
                result.append(i)
                i *= 2
    print(*result)


t = int(input())
test_cases = [int(input()) for _ in range(t)]

for n in test_cases:
    generate_max_score_permutation(n)
