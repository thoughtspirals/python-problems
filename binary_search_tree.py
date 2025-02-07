class BinarySearchTreeNode:
    def __init__(self, name, area):
        self.name = name  # Continent or Country Name
        self.area = area  # Area in square kilometers
        self.left = None
        self.right = None

    def add_child(self, name, area):
        if area == self.area:
            return  # Avoid duplicate area values

        if area < self.area:
            # Insert in the left subtree if area is smaller
            if self.left:
                self.left.add_child(name, area)
            else:
                self.left = BinarySearchTreeNode(name, area)
        else:
            # Insert in the right subtree if area is larger
            if self.right:
                self.right.add_child(name, area)
            else:
                self.right = BinarySearchTreeNode(name, area)

    def in_order_traversal(self):
        """Returns a sorted list of continents and countries based on area."""
        elements = []

        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit root node
        elements.append((self.name, self.area))

        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, area):
        """Search for a continent or country based on area."""
        if self.area == area:
            return self.name

        if area < self.area:
            if self.left:
                return self.left.search(area)
            else:
                return None

        if area > self.area:
            if self.right:
                return self.right.search(area)
            else:
                return None


def build_tree(data):
    """Builds a BST from the given list of (name, area) tuples."""
    root_name, root_area = data[0]  # First element as root
    root = BinarySearchTreeNode(root_name, root_area)

    for name, area in data[1:]:
        root.add_child(name, area)

    return root


if __name__ == "__main__":
    # List of Continents and Countries with Areas (in sq km)
    locations = [
        ("Asia", 44579000),
        ("Africa", 30370000),
        ("North America", 24709000),
        ("South America", 17840000),
        ("Antarctica", 14000000),
        ("Europe", 10180000),
        ("Australia", 8600000),
        ("Russia", 17098242),
        ("Canada", 9984670),
        ("USA", 9833517),
        ("China", 9596961),
        ("Brazil", 8515767),
        ("India", 3287263)
    ]

    tree = build_tree(locations)

    print("\nSorted Continents and Countries by Area:")
    for name, area in tree.in_order_traversal():
        print(f"{name}: {area} sq km")

    print("\nSearching for an area (9596961 sq km):")
    result = tree.search(9596961)
    if result:
        print(f"Found: {result}")
    else:
        print("Not found.")
