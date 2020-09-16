'''
Given a Binary Tree of N edges. The task is to convert this to a Circular Doubly Linked List(CDLL) in-place. 
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted CDLL. 
The order of nodes in CDLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (left most node in BT) must be head node of the CDLL.

Input:
S = 10 20 30 40 60
Output:
40 20 60 10 30 
30 10 60 20 40
Explanation: Given tree is 
     10
   /    \
  20    30
 /   \
40   60
After converting tree to CDLL, when
CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.

https://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/

'''

