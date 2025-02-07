class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):  # Fixed typo (self instead of slef)
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):  # Recursively prints the tree
        print("  " *2* level + "|-- " + self.data)
        for child in self.children:
            child.print_tree(level + 1)  # Increase indentation for child nodes

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))  
    laptop.add_child(TreeNode("Surface"))  
    laptop.add_child(TreeNode("ThinkPad"))  

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone")) 
    cellphone.add_child(TreeNode("Samsung")) 
    cellphone.add_child(TreeNode("OnePlus"))
    cellphone.add_child(TreeNode("Google Pixel"))  # Fixed typo
    
    tv = TreeNode("T V")
    tv.add_child(TreeNode("Samsung"))

    # Add main categories to root
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root  # Must return the root node

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
