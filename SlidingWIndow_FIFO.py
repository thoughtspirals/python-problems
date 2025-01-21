#3. Sliding Window Maximum Using FIFO Queue
#Difficulty: Hard

#Problem:
#Given an array of integers and a window size k, implement a function that returns the maximum element in each sliding window of size k. 
#The solution should use a queue to maintain the elements in the current window, ensuring that the first element of the queue is always the largest within the window.

from collections import deque

def sliding_window_maximum(nums, k):
    """
    Finds the maximum element in each sliding window of size k.

    Args:
        nums (list): List of integers.
        k (int): Size of the sliding window.

    Returns:
        list: List of maximums for each window.
    """
    # Edge case: if k is 0 or nums is empty
    if not nums or k == 0:
        return []
    
    # Deque to store indices of useful elements within the current window
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of the bounds of the sliding window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of elements smaller than the current element
        # as they are not useful for maximum
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current index to the deque
        dq.append(i)

        # Add the maximum of the current window to the result
        # The maximum is at the front of the deque
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Test the function
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
