s = 'bbabb'
if s == s[::-1]:
    print(s)
length = 1
l = 0
for n in range(1, len(s)):
    if n - length >= 1:
        substring = s[n - length - 1 : n + 1]
        
        if substring == substring[::-1]:
            print('subst 1 ',substring)
            l = n - length - 1
            length += 2
            continue
    if n - length >= 0:
        substring = s[n - length : n + 1]
        
        if substring == substring[::-1]:
            print('subst 2 ',substring)
            l = n - length
            length += 1
print(s[l:l+length])
