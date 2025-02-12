class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(data)
            else:
                self.left.add_child(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinarySearchTreeNode(data)
            else:
                self.right.add_child(data)

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements
    

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self.right.find_min()
            self.data = min_larger_node
            self.right = self.right.delete(min_larger_node)
        
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [18, 19, 25, 22, 24, 30, 50, 67, 383, 333, 9, 1,8888]
    numbers_tree = build_tree(numbers)
    print("In-order Traversal:", numbers_tree.in_order_traversal())
    print("Pre-order Traversal:", numbers_tree.pre_order_traversal())
    print("Minimum value:", numbers_tree.find_min())
    print("Maximum value:", numbers_tree.find_max())
    
    # Demonstrate delete functionality
    numbers_tree = numbers_tree.delete(25)
    print("In-order Traversal after deleting 25:", numbers_tree.in_order_traversal())


