class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
               return
        
        if data<self.data:
            #So now we have to add this data in left sub-tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #So now we have to add this data in right sub-tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        
        #Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
            
        #Visit base node
        elements.append(self.data)
        
        #Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements    
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left is None:
                return False
            return self.left.search(value)
        
        if value > self.data:
            if self.right is None:
                return False
            return self.right.search(value)
        
            
    
def build_tree(elements):
    root = BinarySearchTreeNode(50)
        
    for i in range (len(elements)):
        root.add_child(elements[i])

    return root
       
if __name__ == '__main__':
    numbers = [ 18, 19, 25, 22, 24, 30, 50 ]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))        
