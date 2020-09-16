'''
Given an array arr[] of size N where every element is in range from 0 to n-1. Rearrange the given array so that arr[i] becomes arr[arr[i]]. 
This should be done with O(1) extra space.

Input Format:
First line contains an integer denoting the test cases 'T'. First line of each test case contains an integer value depicting size of array 'N' and 
next line contains N space separated integers denoting the elements of the array.

Output Format:
Print all elements of the array after rearranging, each separated by a space, in separate line for each test case.

User Task:
The task is to complete the function arrange() which arranges the elements in the array. The printing is done automatically done by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Arr[i] < N

Example:
Input:
3
2
1 0
5
4 0 2 1 3
4
3 2 0 1

Output:
0 1
3 4 2 0 1
1 0 3 2

Explanation:
Testcase 1: arr[0] = 1 and arr[arr[0]] = 0. Also, arr[1] = 0 and arr[arr[1]] = 1. So, rearranging elements, we get array as, 0 1.
Testcase 2: arr[0] = 4 and arr[arr[0]] = 3. Also, arr[1] = 0 and arr[arr[1]] = 4 and so on. So, rearranging elements, we get array as 3 4 2 0 1.
Testcase 3: arr[0] = 3 and arr[arr[0]] = 1. Also, arr[1] = 2 and arr[arr[1]] = 0 and so on. So, rearranging elements, we get array as 1 0 3 2.

Hints:
1)
There are multiple ways to solve this question.

We would be discussing a more generalised approach here, which can be used for other type of Rearranging problems.

For Rearranging array, we need to store a new value at the position of old value, but do not want to lose the old value too.
Also, we cannot use extra space for this operation (else it would not be Rearrangement and is very easy to execute).

Here, We will store both new value and old value at same position. But how is that possible..?? (No, I am not using pair)

2)
Here, We will use the formula Dividend = Divisor * Quotient + Remainder
where Divisor = size of array
           Quotient = New number at index i after rearrangement
           Remainder = Old Number at index i before rearrangement
           Dividend = The number stored at index i

While Traversing the array, we will Look for the value at arr[arr[i]] (which is to be stored at index i), multiply it with Divisor (size of array), 
and add the old value present at arr[i] to it.
Divisor is a value which is higher then values in array (in this case n - size of array, as array elements are between 0 to n-1)

Obviously, don't forget to remove the multiplier n from the values while accessing and outputting the new values.
'''
print("----------------------------------------O(n) with O(n) extra space---------------------------------------------------------")
def arrange(arr, n):
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[arr[i]]
    print(temp)
    
    
arr = [4,0,2,1,3]
n = len(arr)
arrange(arr, n)
print("---------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------O(n) with O(1) extra space---------------------------------------------------------")
def arrange2(arr, n): 
    
    # changing the array elements
    # to rearrange
    for i in range(0,n):
        arr[i]+=(arr[arr[i]]%n)*n
        print(arr[i])
        
    # reverting the elements
    for i in range(0,n):
        arr[i]=arr[i]//n
        
    print(arr)

arr = [4,0,2,1,3]
n = len(arr)
arrange2(arr, n)


