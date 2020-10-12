from operator import add

def generate(numRows):
    res = [[1]]
    for i in range(1, numRows):
        temp1 = res[-1] + [0]
        print('TEMP 1 ',temp1)
        temp2 = [0] + res[-1]
        print('TEMP 2 ', temp2)
        print('res before :',res)
        res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
        print('res after :',res)
    return res[:numRows]
print(generate(5))    