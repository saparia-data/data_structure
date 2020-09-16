'''
Given an array of 0s, 1s and 2s. Arrange the array elements such that all 0s come first, followed by all the 1s and then, all the 2s.

Note: Do not use inbuilt sort function.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. The first line of each test case is N, size of the array.
The second line of each test case contains N space separated values of the array arr[].

Output: 
For each test case, print the sorted array in a new line.

Your Task:
You don't need to read input or print anything. Your task is to complete the function segragate012() 
which takes the array arr[] and the size of the array as inputs and updates the array arr[] 
such that all the 0s come before the 1s and all the 1s come before the 2s.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0
Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2.
Testcase 2: After segragating the 0s, 1s and 2s, we have 0 0 1.

hints:

1)
These are the folowing steps:

Maintain 3 variables low, high and mid
-low - all elements before low are 0
-mid - all elements between low and mid are 1
-high - all elements after high are 2

Initially low, mid are set at 0 and high is at n-1

Now, we iterate mid from 0 to high, and for every element
-if it is equal to 0, we swap it with element at low, and increement low and mid
-else if it is equal to 2, we swap it with element at high, and decreement high
-else we just increement mid (i.e element is equla to 1)

This method ensures partition, as low and high maintain elements according to their values, and then change their positions,
ensuring all elements before low are lower than low_value and all elements after high are higher than high_value

'''

def segragate012(a,n):
    
    low, mid = 0, 0
    high = n - 1
    
    while(mid <= high):
        
        if(a[mid] == 0):
            a[mid], a[low] = a[low], a[mid]
            low += 1
            mid += 1
            
        elif(a[mid] == 1):
            mid += 1
            
        elif(a[mid] == 2):
            a[mid], a[high] = a[high], a[mid]
            high -= 1
            
    return a

a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(a)
print(segragate012(a, n))
        