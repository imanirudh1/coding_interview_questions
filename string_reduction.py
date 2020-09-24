a='abcab'
b = []
count=0
for i in a:
    if i not in b:
        b.append(i)
    else:
        count += 1
print(count)        