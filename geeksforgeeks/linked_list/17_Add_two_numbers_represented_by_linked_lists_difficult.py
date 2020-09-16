'''
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. 
The sum list is a linked list representation of the addition of two input numbers.

Input:
The first line of input contains the number of test cases T. 
For each test case, the first line of input contains the length of the first linked list and next line contains N elements of the linked list. 
Again, the next line contains M, and the following line contains M elements of the linked list.

Output:
Output the resultant linked list.

User Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the new list.

Expected Time Complexity: O(N) + O(M)
Expected Auxiliary Space: O(N) + O(M)

Constraints:
1 <= T <= 100
1 <= N, M <= 5000

Example:
Input:
2
2
4 5
3
3 4 5
2
6 3
1
7
Output:
3 9 0  
7 0

Explanation:
Testcase 1: For the given two linked list (4 5) and (3 4 5), after adding the two linked list resultant linked list will be (3 9 0).
Testcase 2: For the given two linked list (6 3) and (7), after adding the two linked list resultant linked list will be (7 0).

hint:

Reverse lists and add nodes one by one. Also keep track of carry.

https://www.youtube.com/watch?v=HzWKOp0C_aU
'''
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

def reverse(head):
    # this function reverses the linked list
    prev = None
    current = head
    next = None
    
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    return prev

def addLists(first, second):
    
    first = reverse(first)
    second = reverse(second)
    
    carry = 0
    sumList = None
    
    while(first is not None or second is not None or carry > 0):
        newVal = carry
        
        if(first is not None):
            newVal += first.data
            
        if(second is not None):
            newVal += second.data
            
        carry = newVal // 10
        newVal = newVal % 10
        
        new_node = Node(newVal)
        new_node.next = sumList
        sumList = new_node
        
        if first:
            first = first.next     # moving to next node
        if second:
            second= second.next
    
    return sumList
        


