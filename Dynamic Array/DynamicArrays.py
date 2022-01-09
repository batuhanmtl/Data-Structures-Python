import ctypes  # to creating a new array
class DynamicArray(object):

    #initialize(constructor)
    def __init__(self):

        self.n = 0 #number of elements
        self.capacity = 1 #capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """

        :return: number of elements in the array
        """
        return self.n

    def __getitem__(self, k):
        """

        return element at index k (value)
        """
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds!")

        return self.A[k]

    def append(self,element):
        """
        add element to array
        """
        #If the capacity is full, the capacity is doubled

        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n]=element #add element
        self.n +=1 # increase the number of elements by one

    def _resize(self,new_cap):
        """
         increase the capacity of the directory
        """
        B =self.make_array(new_cap) # creating the new array

        #transfer old array to new array  ( A to B )

        for k in range(self.n):
            B[k]=self.A[k]

        self.A=B              # update array
        self.capacity=new_cap  #update capacity


    def make_array(self,new_cap):
        """
        return new array
        """

        return (new_cap*ctypes.py_object)()

#examples

arr = DynamicArray()
arr.append(1)
print(arr[0])

arr.append(3)
print(arr[0],arr[1])


arr.append(5)
print(arr[0],arr[1],arr[2])


