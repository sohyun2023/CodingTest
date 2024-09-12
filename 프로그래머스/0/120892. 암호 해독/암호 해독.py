def solution(cipher, code):
    i=code-1
    ans=''
    while i<len(cipher):
        ans=ans+ cipher[i]
        i=i+code
    return ans
        
        