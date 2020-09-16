'''
Given two BST, Return elements of both BSTs in sorted form.

First BST 
       3
    /     \
   1       5
Second BST
    4
  /   \
2       6

Output: 1 2 3 4 5 6

First BST 
          8
         / \
        2   10
       /
      1
Second BST 
          5
         / 
        3  
       /
      0
      
Output: 0 1 2 3 5 8 10 


https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/

'''
def merge(root1, root2): 
    res = []
    s1, s2, curr1, curr2 = [], [], root1, root2
    while curr1:
        s1.append(curr1)
        curr1 = curr1.left
    while curr2:
        s2.append(curr2)
        curr2 = curr2.left
    while s1 or s2:
        item1 = item2 = None
        if s1:
            item1 = s1[-1]
        if s2:
            item2 = s2[-1]
        if item1 and item2:
            if item1.data <= item2.data:
                # print(item1.data,end=' ')
                res.append (item1.data)
                s1.pop()
                item2 = None
            else:
                # print(item2.data,end=' ')
                res.append (item2.data)
                s2.pop()
                item1 = None
        elif item1:
            # print(item1.data, end=' ')
            res.append (item1.data)
            s1.pop()
        else:
            # print(item2.data, end=' ')
            res.append (item2.data)
            s2.pop()
        if item1 and item1.right:
            item1 = item1.right
            while item1:
                s1.append(item1)
                item1 = item1.left
        if item2 and item2.right:
            item2 = item2.right
            while item2:
                s2.append(item2)
                item2 = item2.left
    return res