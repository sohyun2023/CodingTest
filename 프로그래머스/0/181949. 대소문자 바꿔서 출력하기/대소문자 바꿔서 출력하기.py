str = input()
ans=''
for i in str:
    if i.islower():
        ans+=i.upper()
    else:
        ans+=i.lower()
        
print(ans)
        
