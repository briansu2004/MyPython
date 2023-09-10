import heapq

# Create an unsorted list
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Convert the list into a min-heap in-place using heapify
heapq.heapify(data)

# The list 'data' is now a valid min-heap
print("Min-heap:", data)

# To extract the minimum element from the heap, you can use heappop
min_element = heapq.heappop(data)
print("Minimum element:", min_element)

# The list 'data' has been updated after the pop operation
print("Updated min-heap:", data)
