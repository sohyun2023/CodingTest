
def solution(s):
    stack=[]
    stack.append(s[0])
    
    for i in range(1,len(s)):
        stack.append(s[i])
        if len(stack)>=2:
            if (stack[-1]==')' and stack[-2]=='('):
                stack.pop()
                stack.pop()
            else:
                continue
        else:
            continue
                
        
    if len(stack) > 0:
        return False
    else:
        return True

    