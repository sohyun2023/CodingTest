def is_valid_bracket_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
    return not stack

def rotate_string(s, x):
    return s[x:] + s[:x]

def solution(s):
    count = 0
    for x in range(len(s)):
        rotated = rotate_string(s, x)
        if is_valid_bracket_sequence(rotated):
            count += 1
    return count
