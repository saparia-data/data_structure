'''
Given a string S consisting of lowercase latin letters, arrange all its letters in lexographical order using Counting Sort.

Input:
The first line of the input contains T denoting number of testcases.Then T test cases follow. Each testcase contains positive integer N denoting the length of string.The last line of input contains the string S.

Output:
For each testcase, in a new line, output the sorted string.

Your Task:
This is a function problem. You only need to complete the function countSort() that takes char array as parameter. 
The printing is done by driver code.

Constraints:
1 <= T <= 105
1 <= N <= 105

Example:
Input:
2
5
edsab
13
geeksforgeeks
Output:
abdes
eeeefggkkorss

Explanation:
Testcase 1: In lexicographical order , string will be abdes.
Testcase 2: In lexicographical order , string will be eeeefggkkorss.

hints:

1)
Store the count of elements. And use this count to sort the elements accordingly.


'''

def countingSort(s,n):
    
    freq=[0 for i in range(256)]
    print(freq)
    
    for char in s:
        freq[ord(char)] += 1
        
    print(freq)
        
    for i in range(256):
        for j in range(freq[i]):
            print(chr(i),end="")
        
        


s = "geeksforgeeks"
n = len(s)
countingSort(s, n)