'''
https://www.geeksforgeeks.org/building-heap-from-array/

'''
def heapify(arr, n, i): 
  
    largest = i; # Initialize largest as root 
    l = 2 * i + 1; # left = 2*i + 1 
    r = 2 * i + 2; # right = 2*i + 2 
  
    # If left child is larger than root 
    if l < n and arr[l] > arr[largest]: 
        largest = l; 
  
    # If right child is larger than largest so far 
    if r < n and arr[r] > arr[largest]: 
        largest = r; 
  
    # If largest is not root 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]; 
  
        # Recursively heapify the affected sub-tree 
        heapify(arr, n, largest); 
  
# Function to build a Max-Heap from the given array 
def buildHeap(arr, n): 
  
    # Index of last non-leaf node. It is like finding parent of leaf node i.e. parent of (size-1)th node parent = (n-1) -1 //2 = (n-2) // 2
    startIdx = (n-2) // 2; 
  
    # Perform reverse level order traversal 
    # from last non-leaf node and heapify 
    # each node 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i); 
  
# A utility function to print the array 
# representation of Heap 
def printHeap(arr, n): 
    print("Array representation of Heap is:"); 
  
    for i in range(n): 
        print(arr[i], end = " "); 
    print(); 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Binary Tree Representation 
    # of input array 
    # 1 
    #         /     \ 
    # 3         5 
    #     / \     / \ 
    # 4     6 13 10 
    # / \ / \ 
    # 9 8 15 17 
    arr = [ 1, 3, 5, 4, 6, 13,  
             10, 9, 8, 15, 17 ]; 
  
    n = len(arr); 
  
    buildHeap(arr, n); 
  
    printHeap(arr, n); 