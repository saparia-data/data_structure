'''
Given an array A[] of size N having distinct elements, the task is to find the next greater element for each element of the array 
in order of their appearance in the array. If no such element exists, output -1.

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. 
Each test case consists of two lines. The first line contains an integer N denoting the size of the array. 
The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Your Task:
This is a function problem. You only need to complete the function nextLargerElement that takes array and n as parameters 
and returns an array of length n denoting the next greater elements for all the corresponding elements in the input array.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
5
6 8 0 1 3
Output
3 4 4 -1
8 -1 1 3 -1

Explanation:
Testcase1: In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.

Testcase 2: In the array , the next larger element to 6 is 8 , for 8 there is no larger elements hence it is -1 , for 0 it is 1 , 
            for 1 it is 3 and then for 3 there is no larger elements and hence -1.


hints:

1) Push the first element to stack.
2) Pick rest of the elements one by one and follow the following steps in loop.
    a) Mark the current element as next.
    b) If stack is not empty, then pop an element from stack and compare it with next.
    c) If next is greater than the popped element, then next is the next greater element for the popped element.
    d) Keep popping from the stack while the popped element is smaller than next.next becomes the next greater element for all such popped elements
    e) Finally, push the next in the stack.
3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.

'''

def createStack(): 
    stack = [] 
    return stack 
  
def isEmpty(stack): 
    return len(stack) == 0
  
def push(stack, x): 
    stack.append(x) 
  
def pop(stack): 
    if isEmpty(stack): 
        print("Error : stack underflow") 
    else: 
        return stack.pop()
    
def printNGE(arr): 
    
    s = createStack()
    next = 0
    element = 0
    output = []
    push(s, arr[0])
    
    for i in range(1, len(arr), 1):
        
        if(isEmpty(s) == False):
            next = arr[i]
            element = pop(s)
            
            while(element < next):
                output.append(next)
                
                if(isEmpty(s) == True):
                    break
                
                element = pop(s)
                
            if(element > next):
                push(s, element)
                
        push(s, next)
        
    while isEmpty(s) == False: 
            element = pop(s) 
            next = -1
            output.append(-1)
        
    return output
    
arr = [4,5,2,25] 
print(printNGE(arr))
                
            