a='hello world'
def reversal(a):
    if len(a) <= 1:
        return a
    return reversal(a[1:]) + a[0]

print(reversal(a))    