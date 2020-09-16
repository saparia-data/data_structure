'''
Given a singly linked list of size N, and an integer K. You need to swap the Kth node from beginning and Kth node from the end in the linked list.
Note: You need to swap the nodes through the links and not changing the content of the nodes.

Input: 
The first line of input contains the number of testcases T. 
The first line of every test-case contains N, number of nodes in a linked list, and K, the nodes to be swapped, 
and the second line contains the elements of the linked list.

Output:  
For each test case, if the nodes are swapped correctly, the output will be 1, else 0.

User Task: 
The task is to complete the function swapkthnode(), which has arguments head, num(no of nodes), and K, and it should return a new head. 
The validation is done internally by the driver code to ensure that the swapping is done by changing references/pointers only. 
 A correct code would always cause output as 1.

Expected Time Complexity: O(n)
Expected Auxillary space Complexity: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= K <= 103

Example:
Input:
3
4 1
1 2 3 4
5 3
1 2 3 4 5
4 4
1 2 3 4
Output:
1
1
1

Explanation:
Testcase 1: Here K = 1, hence after swapping the 1st node from the beginning and end the new list will be 4 2 3 1.
Testcase 2: Here k = 3, hence after swapping the 3rd node from the beginning and end the new list will be 1 2 3 4 5.
Testcase 3: Here k = 4, hence after swapping the 4th node from the beginning and end the new list will be 4 2 3 1.

hints:

1) Simply find both K nodes from front and end and swap them using temp node.

2) Consider the following testcases:

Let X be the kth node from beginning and Y be the kth node from end. Following are the interesting cases that must be handled.
- Y is next to X
- X is next to Y
- X and Y are same
- X and Y don't exist (k is more than number of nodes in linked list)

'''

class Node: 
    def __init__(self, data, next = None): 
        self.data = data 
        self.next = next
      
class LinkedList: 
  
    def __init__(self, *args, **kwargs): 
        self.head = Node(None) 
         
    def push(self, data): 
        node = Node(data) 
        node.next = self.head 
        self.head = node 
      
    # Print linked list 
    def printList(self): 
        node = self.head 
        while node.next is not None: 
            print(node.data, end = " ") 
            node = node.next
      
    # count number of node in linked list 
    def countNodes(self): 
        count = 0
        node = self.head 
        while node.next is not None: 
            count += 1
            node = node.next
        return count 
    
    def swapKth(self, k): 
  
        # Count nodes in linked list 
        n = self.countNodes() 
  
        # check if k is valid 
        if n<k: 
            return
  
        """ 
        If x (kth node from start) and  
        y(kth node from end) are same  
        """
        if (2 * k - 1) == n: 
            return
  
        """ 
        Find the kth node from beginning of linked list.  
        We also find previous of kth node because we need  
        to update next pointer of the previous.  
        """
        x = self.head 
        x_prev = Node(None) 
        for i in range(k - 1): 
            x_prev = x 
            x = x.next
  
        """ 
        Similarly, find the kth node from end and its  
        previous. kth node from end is (n-k+1)th node  
        from beginning  
        """
        y = self.head 
        y_prev = Node(None) 
        for i in range(n - k): 
            y_prev = y 
            y = y.next
  
        """ 
        If x_prev exists, then new next of it will be y.  
        Consider the case when y->next is x, in this case,  
        x_prev and y are same. So the statement  
        "x_prev->next = y" creates a self loop. This self  
        loop will be broken when we change y->next.  
        """
        if x_prev is not None: 
            x_prev.next = y 
  
        # Same thing applies to y_prev 
        if y_prev is not None: 
            y_prev.next = x 
          
        """ 
        Swap next pointers of x and y. These statements  
        also break self loop if x->next is y or y->next  
        is x  
        """
        temp = x.next
        x.next = y.next
        y.next = temp 
  
        # Change head pointers when k is 1 or n 
        if k == 1: 
            self.head = y 
          
        if k == n: 
            self.head = x
            
llist = LinkedList() 
for i in range(8, 0, -1): 
    llist.push(i) 
llist.printList()
llist.swapKth(3)
print("\nAfter swapping")
llist.printList()