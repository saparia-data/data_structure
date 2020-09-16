'''
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list 
such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Input:
The first line of input contains the number of test cases T. For each test case, 
the first line of input contains the length of the linked list and next line contains N elements as the data in the linked list.

Output:
For each test case, segregate the 0s, 1s, and 2s and display the linked list.

Your Task:
The task is to complete the function segregate() which segregates the nodes in the linked list as asked in the problem statement 
and returns the head of the modified linked list. The printing is done automatically by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
8
1 2 2 1 2 0 2 2
4
2 2 0 1
Output:
0 1 1 2 2 2 2 2
0 1 2 2

Explanation:
Testcase 1: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.
Testcase 2: After arranging all the 0s,1s and 2s in the given format, the output will be 0 1 2 2.

hints:

1)
-Traverse the list and count the number of 0s, 1s and 2s. Let the counts be n1, n2 and n3 respectively.
-Traverse the list again, fill the first n1 nodes with 0, then n2 nodes with 1 and finally n3 nodes with 2.

2)
-Iterate through the linked list. Maintain 3 pointers named zero, one and two to point to current ending nodes of linked lists containing 0, 1, and 2 respectively. 
-For every traversed node, we attach it to the end of its corresponding list. 
-Finally we link all three lists. To avoid many null checks, we use three dummy pointers zeroD, oneD and twoD that work as dummy headers of three lists.

https://www.geeksforgeeks.org/sort-a-linked-list-of-0s-1s-or-2s/

'''

def sortList(self): 
    # initialise count of 0 1 and 2 as 0 
    count = [0, 0, 0] 
    
    ptr = self.head
    
    while(ptr):
        count[ptr.data] += 1
        ptr = ptr.next
        
    i = 0
    ptr = self.head
    
    while(ptr):
        if(count[i] == 0):
            i += 1
        else:
            ptr.data = i
            count[i] -= 1
            ptr = ptr.next