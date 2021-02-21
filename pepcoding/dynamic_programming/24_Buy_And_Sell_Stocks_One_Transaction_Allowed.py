'''
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed a single transaction.


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

17


https://www.youtube.com/watch?v=4YjEHmw1MX0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=30


'''
import sys

def solution(prices, n):
    
    lst = sys.maxsize # lsf -> least so far
    op = 0 # op -> overall profit
    pist = 0 # pist -> profit if sold today
    
    for i in range(n):
        
        if(prices[i] < lst):
            lst = prices[i]
            
        pist = prices[i] - lst
        if(pist > op):
            op = pist
            
    return op



if __name__ == "__main__":
    
    prices = [11,6,19,4,1,6,18,4]
    n = len(prices)
    print(solution(prices, n))