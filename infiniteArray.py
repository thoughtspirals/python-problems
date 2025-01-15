class InfiniteArray:
    def __init__(self, generator_function):
        """
        Initialize the infinite array with a generator function.
        The generator function should yield elements of the array.
        """
        self.generator = generator_function()

    def __getitem__(self, index):
        """
        Simulate array indexing by generating elements up to the requested index.
        """
        for i, value in enumerate(self.generator):
            if i == index:
                return value
        raise IndexError("Index out of bounds (infinite array simulation)")

    def find_element(self, target):
        """
        Find the index of a target element in the infinite array.
        """
        for i, value in enumerate(self.generator):
            if value == target:
                return i
        return -1  # Return -1 if the element is not found
   
# Define a generator function for the infinite array
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Create an instance of InfiniteArray
infinite_array = InfiniteArray(infinite_sequence)

# Find an element in the infinite array
target = 899
index = infinite_array.find_element(target)
print(f"Element {target} found at index: {index}")