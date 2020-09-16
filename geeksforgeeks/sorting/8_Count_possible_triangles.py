'''
Given an unsorted array arr of positive integers. 
Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 

Input: 
The first line of the input contains T denoting the number of test cases. 
The first line of the test case is the length of array N and the second line of the test case are its elements.

Output:
The number of possible triangles is displayed to the user.

Your Task:
This is a function problem. You only need to complete the function findNumberOfTriangles() that takes N as a parameter 
and returns the count of total possible triangles.

Expected Time Complexity: O(N2).
Expected Space Complexity: O(1).

Constraints:
1 <= T <= 10
3 <= N <= 103
1 <= arr[i] <= 103

Example:
Input:
2
3
3 5 4
5
6 4 9 7 8
Output:
1
10

Explanation:
Testcase 1: A triangle is possible with all the elements 5, 3 and 4.
Testcase 2: There are 10 triangles possible with the given elements like (6,4,9), (6,7,8),...

hints:

1)
1. Sort the element of the array .Sorting would help you to maintain the condition that for any three sides of  the triangle  a,b and c ,  max(a,b)<=c.
2. Now, traverse for each pair of element in the array and make the count of triplets such that (a+b)>c.

'''
#Big O(n3) solution
def findNumberOfTriangles(arr,n):
    
    i, j, k = 0, 0, 0
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[k] + arr[j] > arr[i]):
                    count += 1
                    
    print(count)
    
#Big O(n2) solution
def findNumberOfTriangles1(A,n):
    n = len(A); 
  
    A.sort(); 
    print(A) 
  
    count = 0; 
      
    for i in range(n - 1, 0, -1): 
        l = 0; 
        r = i - 1; 
        print(l,r)
        while(l < r): 
            if(A[l] + A[r] > A[i]): 
  
                # If it is possible with a[l], a[r] 
                # and a[i] then it is also possible 
                # with a[l + 1]..a[r-1], a[r] and a[i] 
                print(l,r,i)
                count += r - l;  
  
                # checking for more possible solutions 
                r -= 1;  
              
            else: 
  
                # if not possible check for  
                # higher values of arr[l] 
                l += 1;  
    print("No of possible solutions: ", count);



arr1 = [10, 21, 22, 100, 101, 200, 300]
n1 = len(arr1)
findNumberOfTriangles1(arr1, n1)
    