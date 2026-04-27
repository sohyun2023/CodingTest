def solution(my_string, overwrite_string, s):
    my_str=list(my_string)
    my_str[s:s+len(overwrite_string)]=overwrite_string
    print(my_str)
    ans=''.join(my_str)
    return(ans)