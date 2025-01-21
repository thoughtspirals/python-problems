# Explanation:
# enqueue(x):

# Push the element x onto the input_stack.
# dequeue():

# If the output_stack is empty, transfer all elements from input_stack to output_stack (reversing their order).
# Pop the top element from the output_stack (front of the queue).
# peek():

# Similar to dequeue(), but instead of popping from output_stack, just return the top element.
# is_empty():

# Check if both input_stack and output_stack are empty.


class QueueUsingStacks:
    def __init__(self):
        # Two stacks: input_stack for enqueue and output_stack for dequeue
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, x):
        """Adds an element to the queue."""
        self.input_stack.append(x)

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        # If output_stack is empty, transfer elements from input_stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        # If output_stack is still empty, queue is empty
        if not self.output_stack:
            raise IndexError("Queue is empty")
        
        return self.output_stack.pop()

    def peek(self):
        """Returns the front element without removing it."""
        # If output_stack is empty, transfer elements from input_stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop()) #pop() removes the last element of the list and returns it.
        
        # If output_stack is still empty, queue is empty
        if not self.output_stack:
            raise IndexError("Queue is empty")
        
        return self.output_stack[-1] # This is how this line works. It returns the last element of the list.

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return not (self.input_stack or self.output_stack)

# Testing the QueueUsingStacks class
queue = QueueUsingStacks()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.input_stack)  # Output: [10, 20, 30]

print("Peek:", queue.peek())  # Output: Peek: 10
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 10

queue.enqueue(40)
print("Peek:", queue.peek())  # Output: Peek: 20

print("Dequeue:", queue.dequeue())  # Output: Dequeue: 20
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 30
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 40

# Trying to dequeue from an empty queue
try:
    queue.dequeue()
except IndexError as e:
    print(e)  # Output: Queue is empty
