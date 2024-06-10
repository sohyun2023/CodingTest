def solution(n):
    # 초기 피보나치 수열 값 설정
    fib = [0, 1]

    # 피보나치 수열 계산
    for j in range(2, n + 1):
        new = (fib[-1] + fib[-2]) % 1234567
        fib.append(new)
    
    # n번째 피보나치 수 반환
    return fib[n]