'''
Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.

Input:
First line of input contains number of testcases T. For each testcase, 
first line of input contains length of linked list and next line contains the data of linked list. 
Third line contains an integer denoting the position of the linked list node(counting from head) to which the last node connects in order to create a loop. If this integer is 0, this means no loop exists.

Output:
For each testcase, print "True", if linked list contains loop, else print "False".

User Task:
The task is to complete the function detectloop() which contains reference to the head as only argument. 
This function should return 1 if linked list contains loop, else return 0.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= Data on Node <= 103

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
True
False

Explaination:
Testcase 1: In above test case N = 3. The linked list with nodes N = 3 is given. Then value of x=2 is given 
            which means last node is connected with xth node of linked list. Therefore, there exists a loop. 
Testcase 2: For N = 4 ,x = 0 means then lastNode->next = NULL, then the Linked list does not contains any loop.



https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
'''
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print it the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next
            
    def detectLoop(self): 
        slow_p = self.head 
        fast_p = self.head 
        while(slow_p and fast_p and fast_p.next): 
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p: 
                return True
            
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
  
# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
if(llist.detectLoop()): 
        print("Found Loop")
else: 
        print("No Loop")