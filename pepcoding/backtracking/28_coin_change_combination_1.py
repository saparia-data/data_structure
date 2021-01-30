'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the combinations of the n coins (non-duplicate) using 
   which the amount "amt" can be paid.
   

Sample Input:

5

2
3
5
6
7

12
Sample Output

2-3-7-.
2-4-6-.
3-4-5-.
5-7-.


https://www.youtube.com/watch?v=ZiwJdiSGXB4&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=38


'''

def coinChange(i, coins, amtsf, tamt, asf): #amtsf -> amount so far, tamt -> total amount
    
    if(i == len(coins)):
        
        if(amtsf == tamt):
            print(asf + ".")
        return
    
    
    coinChange(i +1, coins, amtsf + coins[i], tamt, asf + str(coins[i]) + "-")
    coinChange(i +1, coins, amtsf + 0, tamt, asf)



if __name__ == "__main__":
    
    
    n = 5
    coins = [2,3,4,5,6,7]
    amount = 12
    coinChange(0, coins, 0, 12, "")