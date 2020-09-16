'''
Given Pointer/Reference to the head of a doubly linked list of N nodes, the task is to Sort the given doubly linked list 
using Merge Sort in both non-decreasing and non-increasing order.

Input:
There are be multiple test cases, for each test case function mergeSort() will be called separately. 
The only input to the function is the pointer/reference to the head of the doubly linked list.

Output:
For each test, print the sorted doubly linked list in both order i.e. in non-decreasing and non-increasing order.

Your Task:
The task is to complete the function sortDoubly() which sorts the doubly linked list. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 105

Example:
Input:
2
8
7 3 5 2 6 4 1 8
5
9 15 0 -1 0
Output:
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
-1 0 0 9 15
15 9 0 0 -1

Explanation:
Testcase 1: After sorting the given linked list in both ways, resultant matrix will be as given in the first two line of output, 
            where first line is the output for non-decreasing order and next line is for non-increasing order.
Testcase 2: After sorting the given linked list in both ways, the resultant list will be -1 0 0 9 15 in non-decreasing order 
            and 15 9 0 0 -1 in non-increasing order.

https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/

'''
def split(self, head):
    
    slow, fast = head, head
    
    while(fast.next is not None or fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    temp = slow.next
    slow.next = None    
    return temp

def merge(self, first, second):
    
    if(first is None):
        return second
    
    if(second is None):
        return first
    
    if(first.data < second.data):
        first.next = self.merge(first.next, second)
        first.next.prev = first
        first.prev = None
        return first
    else:
        second.next = self.merge(first, second.next) 
        second.next.prev = second 
        second.prev = None
        return second
    
def mergeSort(self, head):
    if(head is None or head.next is None):
        return self.head
    
    second = self.split(head)
    
    head = self.mergeSort(head)
    second = self.mergeSort(second)
    
    return self.merge(head, second)
    
    

    