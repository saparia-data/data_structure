'''
Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:  
The first line of the input contains T denoting the number of testcases. 
The first line of the test case will be the size of array and second line will be the elements of the array.

Output: 
For each test case the output will be the majority element of the array. 
Output "-1" if no majority element is there in the array.

User Task:
The task is to complete the function findMajority() which finds the majority element in the array. 
If no majority exists, return -1.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3
Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
Testcase 2: Since, each element in {1,2,3} appears only once so there is no majority element.

hints:

1) Count linearly

2)
Step1: We will traverse the array and find the maximum occurring element in an array.
Step2: Then we'll check if that element count is more than (size of array)/2, if yes then print that element.
If no such elememt exists then print -1.

'''
def majorityElement(A,N):
    
    maxCount = 0
    index = -1
    
    for i in range(N):
        count = 0
        for j in range(N):
            if(A[i] == A[j]):
                count += 1
                
        if(count > maxCount):
            maxCount = count
            index = i
            
    if(maxCount > (N // 2)):
        print(A[index])
        
    else:
        print("Noooooooo")
        
        
A = [1, 1, 2, 1, 3, 5, 1] 
N = len(A)
majorityElement(A, N)
        
            
            