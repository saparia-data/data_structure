'''
Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. 
When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

Input:
The first line of input contains the number of test cases T. For each test case, 
the first line of input contains a number of nodes in the linked list, and the next line contains node data for N nodes.

Output:
For each test case, print the linked list with no repeating elements.

User Task:
You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list. 
You should not read any input from the stdin/console. Your function should return a pointer to a linked list with no duplicate element.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= T <= 100
1 <= size of linked lists <= 104
1 <= numbers in list <= 104

Example:
Input:
2
4
5 2 2 4
5
2 2 2 2 2
Output:
5 2 4
2

Explanation:
Testcase 1: Given linked list elements are 5->2->2->4, in which 2 is repeated only. So, we will delete the extra repeated elements 2 from the linked list and the resultant linked list will contain 5->2->4.
Testcase 2: Given linked list elements are 2->2->2->2->2, in which 2 is repeated. So, we will delete the extra repeated elements 2 from the linked list and the resultant linked list will contain only 2.

hint:
We traverse the link list from head to end. For every newly encountered element, we check whether it is in the hash table: 
if yes, we remove it; otherwise we put it in the hash table.

'''
def removeDuplicates(head):
    # base case of empty list or list with only one element
    if head is None or head.next is None:
        return head

    hash=set() # maintain a hash to check for already present elements.

    walk = head
    hash.add(head.data)
    
    while walk.next is not None:
        
        if walk.next.data in hash:
            walk.next = walk.next.next
            # if value in next node is already in set
            # we bypass the next node by linking current
            # node to the node two steps ahead
        
        else:
            hash.add(walk.next.data)
            # otherwise we simply add the value from
            # next node to set
            walk = walk.next
            # and move ahead
    
    return head