'''
You are given an array of N+2 integer elements. All elements of the array are in range 1 to N. 
And all elements occur once except two numbers which occur twice. Find the two repeating numbers.

Input:
The first line of the input contains an integer T, denoting the total number of test cases. 
Then T test cases follow Each test case consists of two lines. 
First line of each test case contains an integer N denoting the range of numbers to be inserted in array of size N+2. 
Second line of each test case contains the N+2 space separated integers denoting the array elements.

Output:
Print the two elements occuring twice in the array. 
Order of the two elements must be according to second appearance, i.e., first print the element whose second occurrence arrives first. 
For example in 1 2 2 1, the output should be 2 1. And for 1 1 2 2, output should be 1 2.

User Task:
The task is to complete the function repeatedElements() which finds the two repeated element in the array and prints them. 
The newline is added by the driver code automatically.

Constraints:
1 ≤ T ≤ 30
2 ≤ N ≤ 105
1 ≤ array[i] ≤ N

Example:
Input:
3
4
1 2 1 3 4 3
2
1 2 2 1
2
1 1 2 2
Output:
1 3
2 1
1 2

Explanation:
Testcase 1: In the given array, 1 and 3 are repeated two times.
Testcase 2: In the given array , 1 and 2 are repeated two times and second occurence of 2 comes before 1. So the output is 2 1.
Testcase 3: In the given array , 1 and 2 are repeated two times and the output is 1 2.

hints:

The complete Solution :

Traverse the complete array, take the array elements as index and mark the element at this index postion.
Marking can be done, for example by multiplying the element at this index by -1.
Also, check if the element at this index is already negative, if it is output the index.

'''
print("-------------------------------------------------------------------")
def twoRepeated(arr,n):
    
    temp = [0] * n
    
    for i in range(n):
        temp[arr[i]] += 1
        
    #print(temp)
    
    for i in range(n):
        if(temp[i] == 2):
            print(i) 
            
print("-------------------------------------------------------------------")
def twoRepeated1(arr,n):
    
    for i in range(0,n+2):
        
        # check if element is non-negative then
        # make it negative to mark it as visited
        if arr[abs(arr[i])]>0:
            arr[abs(arr[i])]=-arr[abs(arr[i])]
        
        # if already visited, then the element is repeated
        else:
            print(abs(arr[i]),end=" ")
            
print("-------------------------------------------------------------------")

#use set()
    
arr = [1,2,1,3,4,3]
n = len(arr)
twoRepeated1(arr, n)