'''
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.
Note: The output should be based on 1-based indexing, i.e. if the equilibrium point occurs at 1st position then output would be 1.

User Task:
The task is to complete the function equilibriumPoint() which returns the point of equilibrium.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 108

Example:
Input:
2
1
1
5
1 3 5 2 2

Output:
1
3

Explanation:
Testcase 1: Since its the only element hence its the only equilibrium point.
Testcase 2: For second test case equilibrium point is at position 3 as elements below it (1+3) = elements after it (2+2).

Hints:

1) Initialize leftsum  as 0
2) Get the total sum of the array as sum
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
       // sum is now right sum
    b) If leftsum is equal to sum, then return current index. 
    c) leftsum = leftsum + arr[i] // update leftsum for next iteration.
4) return -1 // If we come out of loop without returning then
             // there is no equilibrium index

'''
print("----------------------------------------iterative method O(n2)-------------------------------------------------------")
def equilibriumPoint(A, N):
    
    
    for i in range(N):
        l_sum = 0
        r_sum = 0
        
        for j in range(i):
            l_sum += A[j]
            #print("inside L")
            #print(l_sum)
            
        for k in range(i+1, N):
            r_sum += A[k]
            #print("inside R")
            #print(r_sum)
            
        if(l_sum == r_sum):
            return True
        
    return False
        
A = [1,3,5,2,2]
N = len(A)

print(equilibriumPoint(A, N))
print("------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------prefix sum method O(n)----------------------------------------------------------")
def equilibriumPoint2(A, N):
    
    t_sum = sum(A)
    l_sum = 0
    
    for i in range(N):
        
        #print("l_sum="+str(l_sum))
        #print("t_sum="+str(t_sum))
        if(l_sum == t_sum - A[i]):
            return True
        
        l_sum += A[i]
        t_sum -= A[i]
    return False
        
A = [1,3,5,2,2]
N = len(A)

print(equilibriumPoint2(A, N))
        
        
        
        
        
        
        
        
            
    
    
    
    