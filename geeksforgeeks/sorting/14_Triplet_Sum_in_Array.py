'''
Given an array and an integer. Find if there's a triplet in the array which sums up to the given integer. 

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. The first line of each test case constains two integers N, size of the array and X, the required sum. 
The second line of each test case contains N space separated values of the array arr[].

Output:
Print "1" (without quotes) if there exist three elements in arr[] whose sum is exactly X, else "0" (without quotes).

Your Task:
You don't need to read input or print anything. Your task is to complete the function find3Numbers() which takes the array arr[],
the size of the array (N) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.

Expected Auxiliary Space: O(1)
Expected Time Complexity: O(n2)

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6
Output:
1
1

Explanation:
Testcase 1: The triplet {1, 4, 8} in the array sums up to 13.
Testcase 2: The triplet {1, 3, 6} in the array sums up to 10.

hints:

1)
A naive approach for this is to consider all the possible triplets in the array and check if any of those sums up to X. 
But for this, we we'll require 3 nested loops which will make out time complexity O(n3).
Can you make it better? How about sorting the array? 

2)
Using the two-pointer theorem, we can find out a pair with a given sum in an array in O(n) 
(start iterating one pointer from the beginning and other from the end). 
Can we use this idea to solve this problem in O(n2) time?
For any element arr[i], if we're able to find a pair with sum X-arr[i], we're done. How can we do this?

'''
def find3Numbers(a, n, x):
    
    a.sort()
    #print(a)
    
    for i in range(n):
        l = i + 1
        r = n - 1
        
        while(l < r):
            curr_sum = a[i] + a[l] + a[r]
            
            if(curr_sum == x):
                print(a[i], a[l], a[r])
                return 1
            
            elif(curr_sum > x):
                r -= 1
                
            elif(curr_sum < x):
                l += 1
            
    return 0

a = [12, 3, 4, 1, 6, 9]
x = 24
n = len(a)
print(find3Numbers(a, n, x))
