def sub_lists (l): 
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:]
        print('orig : ',orig)
        new = l[i]
        print('new : ',new)
        for j in range(len(lists)):
            print(lists)
            print('[new]:',[new])
            print('lists[',j,'] : ',lists[j])
            lists[j] = lists[j] + [new]
            print('list[',j,'] :', lists[j])
            print('--------') 
        lists = orig + lists 
        print('Lists : ', lists)
        print('*************************')  
    return lists 
  
# driver code 
l1 = [1, 2, 3] 
print(sub_lists(l1)) 