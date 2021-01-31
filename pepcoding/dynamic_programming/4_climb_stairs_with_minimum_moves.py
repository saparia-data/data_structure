'''
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step you 
   could jump to in a single move.  You can of-course fewer number of steps in the move.
4. You are required to print the number of minimum moves in which you can reach the top of 
   staircase.
Note -> If there is no path through the staircase print null.


Sample Input:

10

3
3
0
2
1
2
4
2
0
0

Sample Output:

4


https://www.youtube.com/watch?v=d42uDPBOXSw&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=4
https://www.youtube.com/watch?v=Zobz9BXpwYE&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=5


'''

import sys

def climbStairsWithMinMoves(arr):
    
    dp = [None] * (len(arr) + 1)
    
    dp[n] = 0
    
    for i in range(n-1, -1, -1):
        
        minn = sys.maxsize
        
        j = 1
        while(j <= arr[i] and i+j <= len(dp)):
            
            if(dp[i + j] != None):
                minn = min(minn, dp[i + j])
                
            j += 1
                
        if(minn != sys.maxsize):
            dp[i] = minn + 1
            
    return dp[0]
                



if __name__ == "__main__":
    
    arr = [3,3,0,2,1,2,4,2,0,0]
    n = 10
    print(climbStairsWithMinMoves(arr))