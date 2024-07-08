def solution(k):
    if k == 0:
        return 1
    catalan = [0] * (k + 1)
    catalan[0] = 1
    for i in range(1, k + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    return catalan[k]
