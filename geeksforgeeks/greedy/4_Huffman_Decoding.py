'''
Given a encoded binary string and a Huffman MinHeap tree, your task is to complete the function decodeHuffmanData(), 
which decodes the binary encoded string and return the original string. 

https://www.geeksforgeeks.org/huffman-decoding/

hints:

To decode the encoded data we require the Huffman tree. We iterate through the binary encoded data. 
To find character corresponding to current bits, we use following simple steps.

-We start from root and do following until a leaf is found.
-If current bit is 0, we move to left node of the tree.
-If the bit is 1, we move to right node of the tree.
-If during traversal, we encounter a leaf node, we print character of that particular leaf node 
 and then again continue the iteration of the encoded data starting from step 1.

'''

def decodeHuffmanData(root, binaryString):
    ans = ""
    curr = root
    for i in range(len(binaryString)):
        if binaryString[i]=='0':
            curr = curr.left
        else:
            curr = curr.right
        if(curr.left==None and curr.right==None):
            ans+=curr.data
            curr=root
    return ans