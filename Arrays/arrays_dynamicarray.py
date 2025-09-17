import ctypes #using  c sata types to create arrays

class Meralist:
    def __ini__(self):
        self.size = 1
        self.n=  0
        #create a C type array with size = self.size
        self.A = self.__make_array(self.size)# cr eates arrat with  size  and stores  it in variable A 

        def __make_array(self,capacity):#input types of __make_array funtion
            #creates a c type array (static , preferential) with capacity
           return (capacity*ctypes.py_object)()#creates array with capacity and returns it
        
L = Meralist()
print(type(L))