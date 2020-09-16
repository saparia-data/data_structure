'''
Given two sorted arrays arr[] and brr[] of size N and M respectively. The task is to find the union of these two arrays.
Union of two arrays can be defined as the common and distinct elements in the two arrays.

Input:
The first line of input contains the number of test cases T. 
For each test case, the first line of input contains the number of test cases T. 
For each test case, the first line of input contains the size of two arrays N and M. Next two lines contains N and M elements.

Output:
For each test case, print the union (common and distinct) of two arrays in a single line. 
You need to print the union in sorted order.

Your Task:
This is a function problem. You only need to complete the function findUnion() that takes N and M as parameters 
and returns the union of two arrays. The new line is automatically appended by the driver code.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(N+M).

Constraints:
1 <= T <= 100
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106

Example:
Input:
3
5 3
1 2 3 4 5
1 2 3
5 5
2 2 3 4 5
1 1 2 3 4
5 5
1 1 1 1 1
2 2 2 2 2
Output:
1 2 3 4 5
1 2 3 4 5
1 2

Explanation:
Testcase 1: Distinct elements including both the arrays are: 1 2 3 4 5.
Testcase 2: Distinct elements including both the arrays are: 1 2 3 4 5.
Testcase 3: Distinct elements including both the arrays are: 1 2.

hints:

1)
Use an unordered set and put all the elements of arr1 and arr2 in the set. 
Now iterate over it an insert all the elemets in a vector. Now sort the vector and print the answer.

But, in this approach you made no use of the fact that both the arrays are sorted. This approach may work even for 2 unsorted arrays.
Thus, the time complexity for this algorithm is O(NLogN) where N is the sum of lengths of both the arrays. 

2)
Can you make the use of the fact that both the arrays are sorted and optimize your code to O(N) (where N is the sum of lengths of both the arrays)?
How about maintaining an iterator to arr1 and another iterator for arr2 and always printing the smaller 
of both the elements (while checking for the duplicates as well)?

Did you take proper care of the case when one of the two arrays get exhausted while prinitng? 
What to do with the second array now? 

'''
def mergeArrays(a,b,n,m):
    
    union_list = list()
    i, j = 0, 0
    
    while(i < n and j < m):
        while(i+1 < n and a[i+1] == a[i]):
            i += 1
            
        while(j+1 < m and b[j+1] == b[j]):
            j += 1
        
        if(a[i] < b[j]):
            union_list.append(a[i])
            i += 1
        elif(a[i] > b[j]):
            union_list.append(b[j])
            j += 1
        else:
            union_list.append(b[j])
            i += 1
            j += 1
            
    while(i < n):
        while(i+1 < n and a[i+1] == a[i]):
            i += 1
        union_list.append(a[i])
        i += 1
    
    while(j < m):
        while(j+1 < m and b[j+1] == b[j]):
            j += 1
        union_list.append(b[j])
        j += 1
            
    return union_list

a = [1, 2, 2, 4, 5, 6] 
b = [2, 3, 5, 7, 7, 8, 9]
n = len(a)  
m = len(b)
print(mergeArrays(a, b, n, m))