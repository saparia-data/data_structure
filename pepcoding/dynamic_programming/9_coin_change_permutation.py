'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of permutations of the n coins using which the 
   amount "amt" can be paid.

Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be 
         used for many installments in payment of "amt"
Note2 -> You are required to find the count of permutations and not combinations i.e.
         2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same 
         combination. You should treat them as 3 and not 1.


Sample Input:

4

2
3
5
6

7

Sample Output:

5


https://www.youtube.com/watch?v=yc0LunmJA1A&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=14


'''

def coinChangePermutation(coins, n, target_amt):
    
    dp = [0] * (target_amt + 1)
    
    dp[0] = 1 # to pay 0 amount there is one way to pay that is to pay nothing
    
    for amt in range(1, len(dp)):
        
        for coin in coins:
            
            if(coin <= amt):
                ramt = amt - coin # ramt -> remaining amount
                dp[amt] += dp[ramt]
                
    return dp[target_amt]



if __name__ == "__main__":
    
    n = 4
    coins = [2,3,5,6]
    target_amt = 7
    
    print(coinChangePermutation(coins, n, target_amt))