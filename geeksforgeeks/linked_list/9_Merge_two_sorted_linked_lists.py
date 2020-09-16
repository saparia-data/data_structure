'''
Given two sorted linked lists consisting of N and M nodes respectively. 
The task is to merge both of the list (in-place) and return head of the merged list.
Note: It is strongly recommended to do merging in-place using O(1) extra space.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains N and M, 
and next two line contains N and M sorted elements in two lines for each.

Output:
For each testcase, print the merged list in sorted form.

User Task:
The task is to complete the function sortedMerge() which takes references to the heads of two linked lists as the arguments 
and returns the head of merged linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(1)

Constraints:
1 <= T <= 100
1 <= N, M <= 104
1 <= Node's data <= 105

Example:
Input:
2
4 3
5 10 15 40 
2 3 20
2 2
1 1
2 4 
Output:
2 3 5 10 15 20 40
1 1 2 4

Explanation:
Testcase 1: After merging the two linked lists, we have merged list as 2, 3, 5, 10, 15, 20, 40.
Testcase 2: After merging the given two linked list , we have 1, 1, 2, 4 as output.

'''
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def sortedMerge(head_A, head_B):
    # a dummy first node to hang the result on
    dummy = Node(0)
  
    # tail points to the last result node
    tail = dummy

    while head_A is not None and head_B is not None:
        # Compare the data of the two 
        # lists whichever lists' data is  
        # smaller, append it into tail and 
        # advance the head to the next Node 
        if head_A.data <= head_B.data:
            tail.next = head_A
            head_A = head_A.next;
        
        else:
            tail.next = head_B
            head_B = head_B.next
        
        tail = tail.next; 
    
    # inlcuding remaining nodes
    if head_A is None:
        tail.next = head_B
    if head_B is None:
        tail.next = head_A
    
    return dummy.next