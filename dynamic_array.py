import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)
    
    def make_array(self,cap):
        return (cap*ctypes.py_object)()

    def append(self,ele):
        if self.n==self.capacity:
            self._resize(2*self.capacity)
