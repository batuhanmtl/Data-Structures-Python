class Node(object):
    
    def __init__(self,value):
        """
        node creation : node has value and next pointer
        """
        self.value =value
        self.nextnode=None
    
    def setNextNode(self,node):
        """
        Determines the next node
        """
        self.nextnode=node
    
    def getNextNode(self):
        """
        Returns the next node
        """
        return self.nextnode
    
    def getNodeValue(self):
        """
        Returns the value inside the node   
        """
        return self.value
        
# node city. node value city plate
ankara =Node("06")
istanbul=Node("34")
izmir=Node("35")
samsun=Node("55")

ankara.setNextNode(istanbul)

#ankara -> istanbul
print(ankara.getNextNode().getNodeValue())

#istanbul -> izmir
istanbul.setNextNode(izmir)
print(istanbul.getNextNode().getNodeValue())

#izmir -> samsun
izmir.setNextNode(samsun)
print(izmir.getNextNode().getNodeValue())

#ankara -> istanbul -> izmir -> samsun
print(ankara.getNextNode().getNextNode().getNextNode().getNodeValue())

        
    