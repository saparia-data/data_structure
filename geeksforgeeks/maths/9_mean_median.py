'''
Given an array a[ ] of size N. The task is to find the median and mean of the array elements.

Note: To find the median, you'd need to sort the array. Since sorting is convered in later tracks,
we have already provided the sort function to you in the code.

Input Format: 
The first line of input contains a single integer T denoting the number of test cases.
Then T test cases follow. Each test case consist of two line input, 1st line is the size of array and the 2nd line is the integer array elements.

Output Format: 
For each testcase, in a new line, print the space separated mean and median of the array elements.

Your Task:
This is a function problem. You just need to complete the following two function:

mean(): It takes the array and its size N as parameters and returns the mean as an integer.
median(): It takes the array and its size N as parameters and returns the median as an integer.
Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= a[i] <= 106

Example:
Input:
2
5
1 2 19 28 5
4
2 8 3 4

Output:
11 5
4 3

Explanation:
Testcase 1: For array of 5 elements , mean and median are 11 and 5 respectively.

Hints:
1) Mean is the average of all elements:

(a1+a2+a3+a4...an)/n

Median is the middle element in sorted elements.
If number of elements is odd, then middle element will be the median, else average of two mids will be the median.

def median(A,N):
    
    A.sort()
    
    ##Your code here
    #If median is fraction then convert the median to integer and return
    
def mean(A,N):
    ##Your code here
'''
def median(A,N):
    A.sort()
    
    if(N % 2 == 0):
        median = (A[N//2] + A[(N//2) - 1])//2
    else:
        median = A[N//2]
    return median

def mean(A,N):
    sum = 0
    for i in A:
        sum += i
        
    return sum//N
        
        
        
        










