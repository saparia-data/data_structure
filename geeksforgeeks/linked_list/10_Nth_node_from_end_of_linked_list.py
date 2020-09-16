'''
Nth node from end of linked list
Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.

Input:
The first line of input contains the number of testcase T. For each testcase, 
the first line of input contains the number of nodes in the linked list and the number N. The next line contains L nodes of the linked list.

Output:
For each testcase, output the data of node which is at Nth distance from the end or -1 in case node doesn't exist.

User Task:
The task is to complete the function getNthFromLast() which takes two arguments: reference to head and N and you need to return Nth from the end.

Note:
Try to solve in single traversal.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 200
1 <= L <= 103
1 <= N <= 103

Example:
Input:
2
9 2
1 2 3 4 5 6 7 8 9
4 5
10 5 100 5
Output:
8
-1

Explanation:
Testcase 1: In the first example, there are 9 nodes in linked list and we need to find 2nd node from end. 2nd node from end os 8.  
Testcase 2: In the second example, there are 4 nodes in the linked list and we need to find 5th from the end. 
            Since 'n' is more than the number of nodes in the linked list, the output is -1.
            
Hints:
1)First approach is to calculate the length of the linked list (L)and subtract n(position from the back) from it to get the position of the desired node from the front.

2)Another approach is to use two pointers. Both pointers are initialized to head. 
  Take a variable count starting from 0. First pointers moves forwards (one step each time) till the count becomes n-1 from the front. 
  Then the other pointer and the first pointer start moving simultaneously. This keeps on going till the first pointer becomes null. 
  At this point the second pointer will be at the desired node.

'''


class Node():
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
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def printNthFromLast(self, n):
        ref_ptr = self.head
        main_ptr = self.head
        counter = 0
        
        if(self.head is not None):
            while(counter < n):
                if(ref_ptr is None):
                    print("n is greater than number of nodes in linledlist")
                ref_ptr = ref_ptr.next
                counter += 1
                
            while(ref_ptr is not None):
                ref_ptr = ref_ptr.next
                main_ptr = main_ptr.next
                
        print(main_ptr.data)
        
llist = LinkedList() 
llist.push(20)
llist.push(4)
llist.push(15) 
llist.push(35)
llist.push(35) 
llist.push(45)
llist.printList()
print("------")
llist.printNthFromLast(3)
                