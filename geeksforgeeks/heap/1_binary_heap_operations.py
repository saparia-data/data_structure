'''
Insert and delete in binary heap

'''

def min_heapify(arr, n, i):
    parent = (i-1)//2
    if parent >= 0:
        if arr[parent] > arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            min_heapify(arr, n, parent)

def heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    
    smallest = i
    
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def insertKey (x, heap):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global curr_size
    heap[curr_size] = x
    curr_size += 1
    min_heapify(heap, curr_size, curr_size-1)

def deleteKey (x, heap):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global curr_size
    if curr_size > 0 and x >= 0 and x < curr_size:
        heap[x] = heap[curr_size-1]
        curr_size -= 1
        heapify(heap, curr_size, x)


def extractMin (heap):
    '''
    :return: return the minimum element from heap and remove it.
    '''
    global curr_size
    if curr_size > 0:
        element = heap[0]
    else:
        return -1
    
    deleteKey(0)
    return element

def getParent(x):  # get parent node , if exits else -1
    return (x - 1) // 2


def leftChild(x):  # get left child if exists, else -1
    return (2 * x + 1) if (2 * x + 1) < curr_size else -1


def rightChild(x):  # get right child if exits, else -1
    return (2 * x + 2) if (2 * x + 2) < curr_size else -1

def decreaseKey(heap, i, new_val): 
        heap[i]  = new_val  
        while(i != 0 and heap[getParent(i)] > heap[i]): 
            # Swap heap[i] with heap[parent(i)] 
            heap[i] , heap[getParent(i)] = heap[getParent(i)], heap[i]
