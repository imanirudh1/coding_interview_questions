a="[(]"
def balanced_paren(a):
    if len(a)%2 != 0:
        return False
    opening=set('({[')
    matches=set([('(',')'),('[',']'),('{','}')])
    stack=[]
    for paren in a:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) ==0:
                return False
            last_open=stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0
print(balanced_paren(a))                            