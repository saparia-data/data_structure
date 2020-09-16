'''
Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its postorder traversal.

Input:
N = 5
arr[]  = {40,30,35,80,100}
Output: 35 30 100 80 40
Explanation: PreOrder: 40 30 35 80 100
InOrder: 30 35 40 80 100
Therefore, the BST will be:
              40
           /      \
         30       80
           \        \   
           35      100
Hence, the postOrder traversal will be: 35 30 100 80 40

https://www.youtube.com/watch?v=0QOtVxTVj4w

Method-1:

-insert nodes into BST
-Traverse BST in postOrder form

This can also be done using stack.

'''