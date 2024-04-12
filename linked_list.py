class Node :
    """ An object for storing a single node
    of a linked list 
    Models two attributes, data and the link to the next 
    node in the list 
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self) -> str:
        return "<Node data : %s >" %self.data
    
class LinkedList:
    """Singly linked list
    """
    def __init__(self):
        self.head = None 
    
    def __isempty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        takes O(n) times
        """
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """ 
        Adds new node containing data at the head of 
        the list
        Takes O(1)     
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self,key):
        """
        Search for the first node containing data that matches the key
        Return the node or none if empty
        Takes O(n) times
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data,index):
        """
        Insert a new node containing data at index position
        Insertion takes O(1) constant time but finding the node at the insertion point
        takes linear O(n) times
        Takes overall O(n) times
        """
        if index == 0:
            self.add(data) 
            
        if index > 0:
            new_node = Node(data)
            
            position = index
            current = self.head
            while position > 1 :
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_nod = current.next_node
            
            prev_node.next_node = new_node
            new_node.next_node  = next_nod
    
    def remove(self,key):
        """
        Remove node  containing data that matches the key
        Retruns node or None if the key doesn't exist
        Takes =O(n) times
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found :
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current
             
    def __repr__(self) -> str:
        """
        Retruns string representation of the list
        takes O(n) times
        """  
        nodes = list()  
        current = self.head
        
        while current:
            if  current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)
            current = current.next_node 
        
        return '->'.join(nodes)   
        
def main():
    l = LinkedList()
    for i in range(10,100,10):
        l.add(i)
    print(l)
    n = l.insert(75,2)
    print(l)
    r = l.remove(75)
    print(r)
    
if __name__ == "__main__":
    main()