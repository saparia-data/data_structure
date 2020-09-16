'''
Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

Input:
First line of input contains number of testcases T. For each testcase, 
first line of input contains length of linked list N and next line contains N integers as data of linked list.

Output:
For each test case output will be 1 if the linked list is a palindrome else 0.

User Task:
The task is to complete the function isPalindrome() which takes head as reference as the only parameter 
and returns true or false if linked list is palindrome or not respectively.

Expected Time Complexity: O(N)
Expected Auxialliary Space Usage: O(1)  (ie, you should not use the recursive stack space as well)

Constraints:
1 <= T <= 103
1 <= N <= 50

Example:
Input:
2
3
1 2 1
4
1 2 3 4
Output:
1
0

Explanation:
Testcase 1: The given linked list is 1 2 1 , which is a pallindrome and Hence, the output is 1.
Testcase 2: The given linked list is 1 2 3 4 , which is not a pallindrome and Hence, the output is 0.

hints:

1. To check if linked list is palindrome, you need the data of first n/2 nodes of the the linked list.
2. Just use a data structure called stack to store data of the first n/2 nodes of the linked list.
3. Now, start traversing from mid of the linked list and compare data of the linked list with that on the top of the stack, 
   each time incrementing the middle and popping the top element from the stack.

Alternative approach (without using additional space)
1. Divide list in 2 halves.
2. Reverse the second half.
3. Check whether the 2 small lists are identical.
    (Note : In this particular method, it is a good practise to make input list same as before)

'''
def reverseList(head):  
    current = head;  
    prevNode = None;  
    nextNode = None;  
      
    #Swap the previous and next nodes of each node to reverse the direction of the list  
    while(current != None):  
        nextNode = current.next;  
        current.next = prevNode;  
        prevNode = current;  
        current = nextNode;  
    return prevNode;  
          
    #isPalindrome() will determine whether given list is palindrome or not.  

# returns the size of linked list
def getSize(head):
    count = 0
    curr_node = head
    while(curr_node):
        count +=1
        curr_node = curr_node.next
    return count

def isPalindrome(head):  
    current = head;  
    flag = True;  
      
    s = getSize(head)
    #Store the mid position of the list  
    mid = (s//2) if(s%2 == 0) else ((s+1)//2);
    
    #Finds the middle node in given singly linked list  
    for i in range(1, mid):  
        current = current.next;  
          
    #Reverse the list after middle node to end  
    revHead = reverseList(current.next);  
      
    #Compare nodes of first half and second half of list  
    while(head != None and revHead != None):  
        if(head.data != revHead.data):  
            flag = False;  
            break;  
              
        head = head.next;  
        revHead = revHead.next;  
        
    return flag