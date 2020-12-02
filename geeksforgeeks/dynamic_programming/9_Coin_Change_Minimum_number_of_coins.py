'''
You are given an amount denoted by value. You are also given an array of coins. 
The array contains the denominations of the give coins.
 You need to find the minimum number of coins to make the change for value using the coins of given denominations. 
 Also, keep in mind that you have infinite supply of the coins.

Example 1:
Input:
value = 5
numberOfCoins = 3
coins[] = {3,6,3}
Output: Not Possible
Explanation:We need to make the change for
value = 5 The denominations are {3,6,3}
It is certain that we cannot make 5 using
any of these coins.

Example 2:
Input:
value = 10
numberOfCoins = 4
coins[] = {2 5 3 6}
Output: 2
Explanation:We need to make the change for
value = 10 The denominations are {2,5,3,6}
We can use two 5 coins to make 10. So
minimum coins are 2.

https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

'''
import sys  
def minCoins(coins, m, V): 
      
    # table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[V] will have result 
    table = [0 for i in range(V + 1)] 
  
    # Base case (If given value V is 0) 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, V + 1): 
        table[i] = sys.maxsize 
  
    # Compute minimum coins required  
    # for all values from 1 to V 
    for i in range(1, V + 1): 
          
        # Go through all coins smaller than i 
        for j in range(m): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != sys.maxsize): 
                    table[i] = min(table[i], sub_res + 1)
                    
    return table[V] 
  
# Driver Code 
if __name__ == "__main__": 
  
    coins = [9, 6, 5, 1] 
    m = len(coins) 
    V = 11
    print(minCoins(coins, m, V))