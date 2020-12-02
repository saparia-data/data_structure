'''
You are given an array A of size N. The array contains integers and is of even length. 
The elements of the array represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.

In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, 
and receives the value of the coin.

You need to determine the maximum possible amount of money you can win if you go first.

Example 1:
Input:
N = 4
A[] = {5,3,7,10}
Output: 15
Explanation: The user collects maximum
value as 15(10 + 5)

Example 2:
Input:
N = 4
A[] = {8,15,3,7}
Output: 22
Explanation: The user collects maximum
value as 22(7 + 15)

https://www.youtube.com/watch?v=ww4V7vRIzSk

'''

def optimalStrategyOfGame(arr, n):
    '''
    :param arr: given array
    :param n: given size of array
    :return: Integer 
    '''
    # Create a table to store  
    # solutions of subproblems  
    dp = [[0 for i in range(n)] for i in range(n)]
    #print(len(dp))

    # Fill table using above recursive  
    # formula. Note that the table is  
    # filled in diagonal fashion  
    # (similar to http:// goo.gl/PQqoS), 
    # from diagonal elements to 
    # table[0][n-1] which is the result.  
    gap = 0
    while(gap < n):
        i = 0
        j = gap
        while(j < n):
            
            if(gap == 0):
                dp[i][j] = arr[i]
                #print(dp)
                
            elif(gap == 1):
                dp[i][j] = max(arr[i], arr[j])
                #print(dp)
                
            else:
                val_1 = arr[i] + min(dp[i+2][j], dp[i+1][j-1])
                val_2 = arr[j] + min(dp[i+1][j-1], dp[i][j-2])
                final_val = max(val_1, val_2)
                dp[i][j] = final_val
            
            i += 1
            j += 1
        
        gap += 1       

    return dp[0][n - 1]


arr1 = [8, 15, 3, 7] 
n1 = len(arr1) 
print(optimalStrategyOfGame(arr1, n1))

arr2 = [ 2, 2, 2, 2 ] 
n2 = len(arr2) 
print(optimalStrategyOfGame(arr2, n2)) 
  
arr3 = [ 20, 30, 2, 2, 2, 10] 
n3 = len(arr3) 
print(optimalStrategyOfGame(arr3, n3))