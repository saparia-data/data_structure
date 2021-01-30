'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the combinations of the n coins (same coin can be used 
   again any number of times) using which the amount "amt" can be paid.
   
   
Sample Input:

5

2
3
5
6
7

12

Sample Output:

2-2-2-2-2-2-.
2-2-2-3-3-.
2-2-2-6-.
2-2-3-5-.
2-3-7-.
2-5-5-.
3-3-3-3-.
3-3-6-.
5-7-.
6-6-.


https://www.youtube.com/watch?v=onUoUZDtak8&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=39


'''

def coinChange(i, coins, amtsf, tamt, asf): #amtsf -> amount so far, tamt -> total amount
    
    if(i == len(coins)):
        
        if(amtsf == tamt):
            print(asf + ".")
        
        return
    
    
    for j in range(tamt // coins[i], 0, -1):
        
        part = ""
        k = 0
        while(k < j):
            part += str(coins[i]) + "-"
            k += 1
            
        coinChange(i + 1, coins, amtsf + coins[i] * j, tamt, asf + part)
        
    
    coinChange(i + 1, coins, amtsf, tamt, asf)

if __name__ == "__main__":
    
    n = 5
    coins = [2,3,4,5,6,7]
    amount = 12
    coinChange(0, coins, 0, 12, "")