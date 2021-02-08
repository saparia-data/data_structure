'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of combinations of the n coins using which the 
     amount "amt" can be paid.

Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be 
         used for many installments in payment of "amt"
Note2 -> You are required to find the count of combinations and not permutations i.e.
         2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same 
         combination. You should treat them as 1 and not 3.

Sample Input:

4

2
3
5
6

7

Sample Output:

2


https://www.youtube.com/watch?v=Ph1EB07Q4pA&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=12
https://www.youtube.com/watch?v=l_nR5X9VmaI&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=13


'''

def coinChangeCombination(coins, n, amt):
    
    dp = [0] * (amt+1)
    
    dp[0] = 1 # to pay 0 amount there is one way to pay that is to pay nothing
    
    for i in range(len(coins)):
        
        for j in range(coins[i], len(dp)):
            
            dp[j] += dp[j - coins[i]]
            
    return dp[amt] 


if __name__ == "__main__":
    
    n = 4
    coins = [2,3,5,6]
    amt = 7
    
    print(coinChangeCombination(coins, n, amt))