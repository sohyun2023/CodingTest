import numpy as np
def solution(n):
    s=np.sqrt(n)
    if s.is_integer():
        return (s+1)**2
    else:
        return -1
    