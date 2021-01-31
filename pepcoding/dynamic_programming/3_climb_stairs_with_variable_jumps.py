'''
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. You are given n numbers, where ith element's value represents - till how far from the step you 
   could jump to in a single move.  
   You can of course jump fewer number of steps in the move.
4. You are required to print the number of different paths via which you can climb to the top.


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

5


https://www.youtube.com/watch?v=uNqoQ0sNZCM&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=3


'''

def countStairsPathWithVariableJump(arr):
    
    dp = [0] * (len(arr) + 1)
    
    dp[n] = 1
    
    for i in range(n-1, -1, -1):
        
        j = 1
        while(j <= arr[i] and i+j <= len(dp)):
            
            dp[i] += dp[i+j]
            j += 1
            
    return dp[0]


if __name__ == "__main__":
    
    arr = [3,3,0,2,1,2,4,2,0,0]
    n = 10
    print(countStairsPathWithVariableJump(arr))