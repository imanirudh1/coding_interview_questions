x = 0
y=0
def getTwoElements(arr, n): 
    global x, y  
    xor1 = arr[0] 
    for i in range(1, n): 
        xor1 = xor1 ^ arr[i] 
    for i in range(1, n + 1): 
        xor1 = xor1 ^ i
              
    print('Xor1 ',xor1)
    # set_bit_no = xor1 & ~(xor1 - 1) 
    set_bit_no = xor1 
    print('Set bit no ',set_bit_no)  
    for i in range(n): 
        if (arr[i] & set_bit_no) != 0: 
            x = x ^ arr[i]
            print('X : ',x)
        else: 
            y = y ^ arr[i] 
            print('Y : ',y)  
    for i in range(1, n + 1): 
        if (i & set_bit_no) != 0: 
            x = x ^ i 
        else: 
            y = y ^ i  
arr = [ 4,3,6,2,1,1] 
n = len(arr) 
      
getTwoElements(arr, n) 
  
print("The missing element is", x, 
      "and the repeating number is", y) 