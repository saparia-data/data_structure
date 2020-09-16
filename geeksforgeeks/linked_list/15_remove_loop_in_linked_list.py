'''
You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present.

Input:
First line of input contains number of testcases T. T testcases follow. For each testcase, 
first line of input contains length N of the linked list and next line contains N data of the linked list. 
The third line contains the position of the node(from head) to which the last node will get connected. If it is 0 then there is no loop.

Output:
For each testcase, in a new line, 1 will be printed if loop is removed and the list still has all N nodes connected to it, else 0 will be printed.

User Task:
Your task is to complete the function removeLoop(). The only argument of the function is head pointer of the linked list. 
Do not print anything. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.

Expected time complexity : O(n)

Expected auxiliary space : O(1)

Constraints:
1 <= T <= 102
1 <= N <= 104

Example:
Input:
2
3
1 3 4
2
4
1 8 3 4
0
Output:
1
1

Explanation:
Testcase 1: In the first test case N = 3.The linked list with nodes N = 3 is given. 
            Here, x = 2 which means last node is connected with xth node of linked list. Therefore, there exists a loop. 
            
Testcase 2: N = 4 and x = 0, which means lastNode->next = NULL, thus the Linked list does not contains any loop.

hints:

-Use the Hare Tortoise algorithm to find out if there is a loop.
A piece of code is run repeatedly in the Hare Tortoise algorithm, such that, with each execution, 
the Hare pointer moves 2 nodes ahead and the tortoise pointer moves one node ahead in the linked list. 
If the two meet, it means there is a loop in the list and the meeting node lies inside the loop.

-Next, find the size of the loop.
Make one pointer stay at the meeting point of Hare Tortoise and use the other pointer to complete one round around the loop. 
Count the steps required to cover the loop.

-Let s be the size of the loop.
Now we need 2 pointers again. The first pointer points at the head. Second pointer should be s nodes ahead.
Moves both pointers ahead step by step at same rate. This time the meeting point will be the junction node.

'''
def removeLoop(head):
    
    if(head is None):
        return
    
    slow = head
    fast = head.next
    
    while(fast != slow):
        if(fast is None or fast.next is None):
            return
        
        slow = slow.next
        fast = fast.next.next
        
    size = 1
    fast = fast.next
    while(fast != slow):
        size += 1
        fast = fast.next
        
    slow=head
    fast=head
    
    for _ in range(size - 1):
        fast = fast.next
        
    while(fast.next != slow):
        fast = fast.next
        slow = slow.next
        
    fast.next = None