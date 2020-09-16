'''
Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value,
second should be min value, third should be second max, fourth should be second min and so on.

Note: O(1) extra space is allowed. Also, try to modify the input array as required.

Input:
First line of input conatins number of test cases T. First line of test case contain an integer denoting the array size N and
second line of test case contain N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, Output the modified array with alternated elements.

User Task:
The task is to complete the function rearrange() which rearranges elements and shouldn't print anything.
Printing of the modified array will be handled by driver code.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= arr[i] <= 107

Example:
Input:
2
6
1 2 3 4 5 6
11 
10 20 30 40 50 60 70 80 90 100 110

Output:
6 1 5 2 4 3
110 10 100 20 90 30 80 40 70 50 60

Explanation:
Testcase 1: Max element = 6, min = 1, second max = 5, second min = 2, and so on... Modified array is : 6 1 5 2 4 3.
Testcase 2: Max element = 110, min = 10, second max = 100, second min = 20, and so on... Modified array is : 110 10 100 20 90 30 80 40 70 50 60.

Hints:
1) 
For Rearranging array, we need to store a new value at the position of old value, but do not want to lose the old value too.
Also, we cannot use extra space for this operation (else it would not be Rearrangement and is very easy to execute).
Here, We will store both new value and old value at same position. But how is that possible..?? (No, I am not using pair)

2)
Here, We will use the formula Dividend = Divisor * Quotient + Remainder
where Divisor = max_element
           Quotient = New number at index i after rearrangement
           Remainder = Old Number at index i before rearrangement
           Dividend = The number stored at index i

The even indices store Max elements and the odd indices store Min elements.
Traverse the array, and look for elements accordingly, multiply it with Divisor (max_element) and add the value present at arr[i]

Divisor is a value which is higher than values stored in array (in this case n - size of array, as array elements are between 0 to n-1)
Obviously, don't forget to remove the multiplier n from the values while accessing and outputting the new values.

'''

print("----------------------------------------O(n) with O(n) extra space-------------------------------------------------------")

def rearrange(arr, n):
    
    temp = [0] * n
    
    flag = True
    smallest = 0
    largest = n - 1
    
    
    for i in range(n):
        
        if(flag):
            temp[i] = arr[largest]
            largest -= 1
        else:
            temp[i] = arr[smallest]
            smallest += 1
            
        flag = bool(1 - flag)
        
    print(temp)
    
arr = [1,2,3,4,5,6]
n = len(arr)
rearrange(arr, n)
print("---------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------O(n) with O(1) extra space---------------------------------------------------------")
    
def rearrange2(arr, n):
    
    max_idx = n - 1
    min_idx = 0
    max_elem = arr[n - 1] + 1
    
    for i in range(0,n):
        
        if(i % 2 == 0):
            #print(i,arr[max_idx],max_elem)
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            #print("even")
            #print(arr[i])
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem ) * max_elem
            #print("odd")
            #print(arr[i])
            min_idx += 1 
    print(arr)
        
    for i in range(0, n) : 
        arr[i] = arr[i] // max_elem
        
    print(arr)
        
arr = [1,2,3,4,5,6,7]
n = len(arr)
rearrange2(arr, n)
        
        
        

