'''
Given two arrays A and B respectively of size N and M. 
The task is to print the count of elements in the intersection (or common elements) of the two arrays.
For this question, intersection of two arrays can be defined as the set containing distinct common elements between the two arrays.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case is N and M, N is the size of array A and M is size of array B. The second line of each test case contains N input A[i].
The third line of each test case contains M input B[i].

Output:
Print the count of intersecting elements.

Constraints:
1 ≤ T ≤ 100
1 ≤ N, M ≤ 105
1 ≤ A[i], B[i] ≤ 105

Example:
Input:
4
5 3
89 24 75 11 23
89 2 4
6 5
1 2 3 4 5 6
3 4 5 6 7
4 4
10 10 10 10
20 20 20 20
3 3
10 10 10
10 10 10
Output:
1
4
0
1

Explanation:
Testcase 1: 89 is the only element in the intersection of two arrays.
Testcase 2: 3 4 5 and 6 are the elements in the intersection of two arrays.
Testcase 3: Non of the elements are common so the output will be -1.
Testcase 4: 10 is the only element which is in the intersection of two arrays.

hints:

1)
Use hashing (direct index table) to check common elements in both the arrays.

2)
Hash the elements of the first array.
Now traverse second array and check if element exists in the hash, if it exists, then increase the count and erase that element from the hash.

'''

def arrayIntersection(a, b, n, m):
    
    mySet = set()
    
    for i in a:
        mySet.add(i)
    
    count = 0
    for i in b:
        if(i in mySet):
            count += 1
            mySet.remove(i)
            
    return count
    
    
a = [1,2,3,4,5,6]
b = [3,4,5,6,7]
n = len(a)
m = len(b)
print(arrayIntersection(a, b, n, m))