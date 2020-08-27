import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)
    
    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()

    def append(self,ele):
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n]=ele
        self.n +=1    

    def _resize(self,new_cap):
        B=self.make_array(new_cap)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=new_cap
    def __len__(self):
        return self.n  

    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('k is out of bound')
        return self.A[k]              

arr=DynamicArray()
arr.append(1)
arr.append(2)
print('length of the arr: ',len(arr))
for i in range(0,len(arr)):
    print('Elements at %s index :'%(i),arr[i])