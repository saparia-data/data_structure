'''
Given two Binary Search Trees(without duplicates). Find need to print the common nodes in them. In other words, find intersection of two BSTs

Example:

Input:

BST1:
                  5
               /     \
             1        10
           /   \      /
          0     4    7
                      \
                       9
BST2:
                10 
              /    \
             7     20
           /   \ 
          4     9
          
Output: 4 7 9 10

-use level order traversal and store nodes in list for BST1 and BST2. check if element of BST1 list is in list of BST2.

https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/

'''

