'''
Given a linked list of N positive integers. You need to swap elements pairwise. Your task is to complete the function pairwise_swap().

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines, the first line contains N(size of linked list). 
The second line contains N elements of linked list separately.

Output:
For each testcase, in new line, print the modified linked list.

User Task:
Since this is a functional problem you don't have to worry about input and output, you just have to complete the function pairwise_swap(). 
The printing is done automatically by the driver code.

Constraint:
1 <= T <= 100
1 <= N <= 100
1 <= Node values <= 1000

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Example:
Input:
2
7
1 2 3 4 5 6 7
6
1 2 3 4 5 6
Output:
2 1 4 3 6 5 7
2 1 4 3 6 5

Explanation:
Testcase 1: The linked list after swapping becomes: 1 2 3 4 5 6 7 -> 2 1 4 3 6 5 7.
Testcase 2: The linked list after swapping becomes: 1 2 3 4 5 6 -> 2 1 4 3 6 5.

hints:

1. At first, it comes in our mind that we can swap data of the nodes. But, this is not feasible solution.
2. Think of swapping the nodes by changing the pointers in the linked list.
3. Start from head of the linked list with temp as copy of head.
4. Now, take another pointer temp2 as temp->next (if exists).
5. Now, do the following for each pair:
    -> temp->next = temp1->next;
    -> temp1->next = temp;
    -> temp = temp->next;
    -> temp1 = temp->next;

'''
#This method swaps the data which is not feasible if linked list is too long
def pairwiseSwap(self): 
        temp = self.head 
         
        # There are no nodes in linked list 
        if(temp is None): 
            return 
         
        while(temp is not None and temp.next is not None): 
  
            # Swap data of node with its next node's data 
            temp.data, temp.next.data = temp.next.data, temp.data  
              
            # Move temp by 2 from the next pair 
            temp = temp.next.next
            
#This method changes the link
def pairwiseSwapLink(self):
    
    prev = self.head
    curr = self.head.next
    
    self.head = curr
    
    while(True):
        
        nxt = curr.next
        curr.next = prev
        
        if(next is None or nxt.next is None):
            prev.next = nxt
            break
        
        prev.next = nxt.next
        
        prev = nxt
        curr = nxt.next