class Stacks:

    def __init__(self):
        """
        initialize (constructor)
        """
        self.items = []
        
    def isEmpty(self):
        """
        check if it is empty
        """
        return self.items == [] # boolean operation
        
    def push(self,item):
        """
        adds items to the stack
        """
        self.items.append(item)
        
    def pop(self):
        """
        remove items from stack
        """
        return self.items.pop()
        
    def top(self):
        """
        shows the last item in the stack
        """
        return self.items[len(self.items)-1]
        
    def size(self):
        """
        size of stack
        """
        return len(self.items)
        

#examples

stack = Stacks()
print(stack.isEmpty())

stack.push("fox")
print(stack.top())

stack.push("leon")
print(stack.top())

stack.push("cat")
print(stack.top())

stack.pop()
print(stack.pop())

stack.pop()
print(stack.isEmpty())
