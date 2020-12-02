'''
One of the rudimentary problems to understand DP is finding the nth Fibonacci number. 
Here, we will solve the problem using the top-down approach.
You are given a number N. You need to find Nth Fibonacci number.
The first two term of the series are 1 and 1.

Example 1:
Input:
N = 5
Output: 5

https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/

'''
def fib(n, lookup): 
  
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
  
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
  
    # return the value corresponding to that value of n 
    return lookup[n] 
# end of function 
  
# Driver program to test the above function 
def main(): 
    n = 34 
    # Declaration of lookup table 
    # Handles till n = 100  
    lookup = [None]*(101) 
    print("Fibonacci Number is ", fib(n, lookup)) 
  
if __name__=="__main__": 
    main()