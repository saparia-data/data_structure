'''
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed infinite transactions.

Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) 
       before opening another transaction (another buy)



Sample Input:

9

11
6
7
19
4
1
6
18
4

Sample Output:

30



https://www.youtube.com/watch?v=HWJ9kIPpzXs&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=31


'''

def solution(prices, n):
    
    bd = 0 # buy date
    sd = 0 # sell date
    profit = 0
    
    for i in range(1, n):
        
        if(prices[i] >= prices[i-1]):
            sd += 1
        else:
            profit += prices[sd] - prices[bd]
            bd = sd = i
            
    profit += prices[sd] - prices[bd]
    
    return profit


if __name__ == "__main__":
    
    prices = [11,6,19,4,1,6,18,4]
    n = len(prices)
    print(solution(prices, n))