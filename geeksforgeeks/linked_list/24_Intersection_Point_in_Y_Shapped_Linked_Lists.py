'''
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.

Note: Expected time complexity is O(m + n) where m and n are lengths of two linked lists.

Input:
First line of input is the number of test cases T. Every test case has four lines. First line of every test case contains three numbers, 
x (number of nodes before merge point in 1st list), y (number of nodes before merge point in 2nd list) and z (number of nodes after merge point). 
Next three lines contain x, y and z values.

Output:
Print the data of the node in the linked list where two linked lists intersects.

Your Task:
The task is to complete the function intersetPoint() which finds the point of intersection of two linked list. 
The function should return data value of a node where two linked lists merge. If linked list do not merge at any point, then it should return -1.

Challenge : Try to solve the problem without using any extra space.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= value <= 1000

Example:
Input:
2
2 3 2
10 20
30 40 50
5 10
2 3 2
10 20
30 40 50
10 20
Output:
5
10

Explanation:
Testcase 1: The point of intersection of two linked list is 5, means both of them get linked (intersects) with each other at node whose value is 5.
Testcase 2: The point of intersection of two linked list is 10. Hence, output is 10.

hints:

1)
- Iterate trough 1st linked list and hash it's value
- Now iterare trough 2nd linked list and check whether it's value is present in hash table.
- Return node as soon as u find the node in hash table
   
2) 
- Get count of the nodes in the first list, let be c1.
- Get count of the nodes in the second list, let be c2.
- Get the difference of counts d = abs(c1 – c2)
- Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
- Then we can traverse both the lists in parallel till we come across a common node.

'''

def getSize(head):
    ret = 0
    while head is not None:
        head = head.next
        ret+=1
    return ret

def intersetPoint(head1,head2):
    n1 = getSize(head1)
    n2 = getSize(head2)
    
    # if list1 is longer, we ignore some of its starting
    # elements till it has as many elements as list2
    while n1>n2:
        head1 = head1.next
        n1-=1
        
        
    # if list2 is longer, we ignore some of its starting
    # elements till it has as many elements as list1
    while n2>n1:
        head2 = head2.next
        n2-=1
        
    # now we simple traverse ahead till we get the
    # intersection point, if there is none, this loop
    # will break when both pointers point at NULL
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
        
    if(head1 is not None):
        return head1.data
    
    return -1