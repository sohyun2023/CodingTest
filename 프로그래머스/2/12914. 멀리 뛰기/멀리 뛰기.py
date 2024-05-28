def solution(n):
    MOD = 1234567
    # 조합의 수를 저장할 배열을 초기화합니다.
    ways = [0] * (n + 1)
    
    # 기본 초기 조건을 설정합니다.
    ways[0] = 1  # 0칸을 가는 방법은 한 가지 (아무것도 하지 않는 것)
    ways[1] = 1  # 1칸을 가는 방법은 한 가지 (1칸을 한 번 가는 것)

    # 숫자 2부터 n까지 각 숫자에 대해 가능한 조합의 수를 계산합니다.
    for i in range(2, n + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % MOD

    return ways[n]

    
    