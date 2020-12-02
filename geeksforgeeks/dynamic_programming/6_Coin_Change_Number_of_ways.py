'''
ou have an infinite supply of coins, each having some value.
Find out the number of ways to use the coins to sum-up to a certain required value.

Example 1:
Input:
value = 4
numberOfCoins = 3
coins[] = {1,2,3}
Output: 4
Explanation: We need to make the change
for value = 4. The denominations are
{1,2,3} Change for 4 can be made:
1+1+1+1
1+1+2
1+3
2+2
So, as it is evident, we can do this in
4 ways.

https://www.youtube.com/watch?v=L27_JpN6Z1Q

'''
def numberOfWays(coins,numberOfCoins,value):
    
    table = [[0 for x in range(value+1)] for x in range(numberOfCoins)]
    print(table)
    
    for i in range(numberOfCoins):
        table[i][0] = 1
        
    print(table)
        
    for i in range(numberOfCoins):
        for j in range(value+1):
            if(coins[i] > j):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] + table[i][j-coins[i]]
                
    print(table)
    print(value,numberOfCoins)
    return table[numberOfCoins-1][value]
    

print(numberOfWays([2,5,3,6], 4, 10))