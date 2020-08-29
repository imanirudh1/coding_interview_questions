a='anirudh'
def unique_char(a):
    s=set()
    for i in a:
        if i in s:
            return False
        else:
            s.add(i)
    return True
    
print(unique_char(a))                