class Queue:
    
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
     
    def enqueue(self,item):
        """
        add an item to the queue
        """
        self.items.insert(0,item)
     
    def dequeue(self):
        """
        remove item from queue
        """
        return self.items.pop()
            
    def size(self):
        """
        length of queue
        """
        return len(self.items)
        
#examples

queue = Queue()

queue.enqueue("A")
queue.enqueue("B")

print("size: ",queue.size())

queue.dequeue()
print("size: ",queue.size())

queue.dequeue()
print("size: ",queue.size())

print(queue.isEmpty())
