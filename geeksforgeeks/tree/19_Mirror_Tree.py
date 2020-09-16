'''
Given a Binary Tree, convert it into its mirror.

The tree is
        1         (mirror)     1
     /      \         =>      /  \
   3       2                  2   3
The inorder of mirror is 2 1 3

The tree is
                           10                                      10
                        /     \           (mirror)               /   \
                     20        30            =>                 30   20
                  /       \                                    /   \
               40       60                                   60    40
The inroder traversal of mirror is 30 10 60 20 40.


'''
def mirror(root):
    
    if(root is None):
        return
    else:
        mirror(root.left)
        mirror(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp