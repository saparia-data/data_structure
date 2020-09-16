'''
Given three sorted arrays A, B and C of size N, M and P respectively. 
The task is to merge them into a single array which must be sorted in increasing order.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains size of three arrays N, M and P. 
Next three lines contains N, M and P elements for arrays.

Output:
Output the merged sorted array.

Your Task:
This is a function problem. You only need to complete the function mergeThree() that takes A,B,C as parameters. 
The function returns an array or vector.

Constraints:
1 <= T <= 100
1 <= N, M, P <= 106
1 <= A[i], B[i], C[i] <= 106

Example:
Input:
2
4 5 6
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
2 3 4
1 2
2 3 4
4 5 6 7
Output:
1 1 1 2 2 2 3 3 3 4 4 4 5 5 6
1 2 2 3 4 4 5 6 7

Explanation:
Testcase 1: Merging these three sorted arrays, we have elements as 1 1 1 2 2 2 3 3 3 4 4 4 5 5 6.
Testcase 2: Merging three sorted arrays , we have elements as 1 2 2 3 4 4 5 6 7.

hints:

1)
Try solving it with same method as Merge 2 sorted arrays (Extra space allowed solution).
The difference is instead of 2, 3 arrays are available.
What all changes should occur due to this...??

2)
The complete solution:

Make an output array to store the complete result of merging 3 sorted arrays.
Iterate through all the 3 arrays at once, using different iterators for each array, and storing the minimum of all in the output array.
After this loop exits, this shows one loop has exhausted. And 2 arrays are still left. Make cases accordingly.
Total 3 cases will be made, i.e if A exhausts, iterate for B & C, and if B exhausts iterate for A & C, and so on.
After this loop also exits, a single array is still left. Make the cases for the same accordingly. And output the the remaining array.

'''
def mergeThree(A,B,C):
    
    m, n, o = len(A), len(B), len(C)
    i = j = k = 0
    
    # Destination array 
    d = []
    
    while(i < m and j < n and k < o):
        
        # Get Minimum element
        mini = min(A[i], B[j], C[k])
        
        d.append(mini)
        
        # Increment the source pointer which gives minimum element
        if(A[i] == mini):
            i += 1
        elif(B[j] == mini):
            j += 1
        elif(C[k] == mini):
            k += 1
        
    # Merge a and b if c has exhausted 
    while(i < m and j < n):
        if(A[i] <= B[j]):
            d.append(A[i])
            i += 1
        else:
            d.append(B[j])
            j += 1
        
    # Merge b and c if a has exhausted         
    while(j < n and k < o): 
        if(B[j] <= C[k]):
            d.append(B[j]) 
            j += 1
        else: 
            d.append(C[k]) 
            k += 1
        
    # Merge a and c if b has exhausted         
    while(i < m and k < o): 
        if(A[i] <= C[k]): 
            d.append(A[i]) 
            i += 1
        else: 
            d.append(C[k]) 
            k += 1
        
    #Take elements from a if b and c have exhausted        
    while(i < m): 
        d.append(A[i]) 
        i += 1

    # Take elements from b if a and c have exhausted 
    while(j < n): 
        d.append(B[j]) 
        j += 1

    # Take elements from c if a and b have exhausted 
    while(k < o):
        d.append(C[k]) 
        k += 1
      
    return d
    
A = [1, 2, 41, 52, 84] 
B = [1, 2, 41, 52, 67] 
C = [1, 2, 41, 52, 67, 85]

print(mergeThree(A, B, C)) 