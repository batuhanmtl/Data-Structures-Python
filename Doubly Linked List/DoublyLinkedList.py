class doublyLinkedListNode(object):

    def __init__(self,value):
        """
        create node : node has value next pointer and previous pointer
        """
        self.value = value
        self.nextnode=None
        self.prevnode=None
        
    def setNextNode(self,node):
        """
        Sets the next node
        """
        self.nextnode=node
       
    def setPrevNode(self,node):
        """
        Sets the previous node
        """
        self.prevnode=node
    
    def getNextNode(self):
        """
        returns the next node
        """
        return self.nextnode
        
    def getPrevNode(self):
        """
        returns the previous node
        """
        return self.prevnode
    
    def getNodeValue(self):
        """
        Returns the node value
        """
        return self.value
        
#examples

ankara = doublyLinkedListNode("06")
bolu = doublyLinkedListNode("14")
istanbul = doublyLinkedListNode("34")

#ankara <-> bolu
ankara.setNextNode(bolu) # ankara -> bolu
bolu.setPrevNode(ankara) # bolu -> ankara

print(ankara.getNextNode().getNodeValue()) # ankara -> bolu
print(bolu.getPrevNode().getNodeValue())    # bolu -> ankara