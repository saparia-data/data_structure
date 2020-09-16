'''
Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.
Note: If the length of linked list is odd, then the extra node should go in the first list while splitting.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of nodes in the linked list and next line contains N elements of the linked list.

Output:
For each test, in a new line, print the sorted linked list.

Your Task:
For C++ and Python: The task is to complete the function mergeSort() which sort the linked list using merge sort function.
For Java: The task is to complete the function mergeSort() and return the node which can be used to print the sorted linked list.

Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 105

Note: Try to solve the problem in constant space.

Example:

Input:
2
5
3 5 2 4 1
3
9 15 0
Output:
1 2 3 4 5
0 9 15

Explanation:
Testcase 1: After sorting the given linked list, the resultant matrix will be 1->2->3->4->5.
Testcase 2: After sorting the given linked list , resultant will be 0->9->15.

https://www.geeksforgeeks.org/merge-sort-for-linked-list/

'''

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def getMiddle(self, head): 
        if (head == None): 
            return head 
  
        slow = head 
        fast = head 
  
        while (fast.next != None and fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
              
        return slow
    
    def sortedMerge(self, a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result
    
    def mergeSort(self, h): 
          
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
  
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the next of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist
    
    
li = LinkedList() 
      
# Let us create a unsorted linked list 
# to test the functions created.  
# The list shall be a: 2->3->20->5->10->15  
head = li.push(15) 
head = li.push(10) 
head = li.push(5) 
head = li.push(20) 
head = li.push(3) 
head = li.push(2) 
 
# Apply merge Sort  
li.head = li.mergeSort(li.head) 
print ("Sorted Linked List is:") 
li.printList() 