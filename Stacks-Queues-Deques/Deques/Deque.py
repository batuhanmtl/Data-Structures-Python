class Deque:

    def __init__(self):
        
        """
        initialize (constructor)
        """
        
        self.items =[]

    def isEmpty(self):
        """
        check if it is empty
        """
        return self.items == [] # boolean operation
        
    def addFront(self,item):
        """
        Adding items to front deque
        """
        self.items.append(item)
    
    def addRear(self,item):
        """
        Adding items from rear to deque
        """
        self.items.insert(0,item)
    
    def removeFront(self):
        """
        Removing items from front deque
        """
        return self.items.pop()
    
    def removeRear(self):
        """
        Removing items from rear deque
        """
        return self.items.pop(0)
        
    def size(self):
        """
        length of deque
        """
        return len(self.items)
        
#examples

deque =Deque()

deque.addFront("deep")

deque.addRear("learning")

print("size: ",deque.size())

deque.removeFront()
deque.removeRear()


print(deque.isEmpty())  