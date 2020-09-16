'''
The cost of stock on each day is given in an array A[] of size N. 
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Input: 
First line contains number of test cases T. First line of each test case contains an integer value N denoting the number of days, 
followed by an array of stock prices of N days. 

Output:
For each testcase, output all the days with profit in a single line. And if there is no profit then print "No Profit".

User Task:
The task is to complete the function stockBuySell() which finds the days of buying and selling stock and print them. 
The newline is automatically added by the driver code.

Constraints:
1 <= T <= 100
2 <= N <= 103
0 <= Ai <= 104

Example
Input:
4
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67
5
4 2 2 2 4
5
5 5 5 5 5

Output:
(0 3) (4 6)
(1 4) (5 9)
(3 4)
No Profit

Explanation:
Testcase 1: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit. Now, we buy stock on day 4 and sell it on day 6.
Testcase 2: We can buy stock on day 1, and sell it on 4th day, which will give us maximum profit. Now, we buy stock on day 5 and sell it on day 9.
Testcase 3: We can buy stock on day 3, and sell it on 4th day, which will give us maximum profit.
Testcase 4: We cannot sell any stock that will give us profit as the price remains same.

Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, output should be in a single line.

Hint:

Obviously, we need to sell when the prices are highest, and buy when prices are lowest.
But how to determine, that the prices are highest and lowest.
The Local Minima are the points of Lowest price and Local Maxima are the points of Highest price.
Iterate through the complete array, and store these points of Local Minima and then store these points of Local Maxima.
'''
def stockBuySell(A,N):
    
    if(N == 1):
        return
    
    i = 0
    while(i < N-1):
        
        while((i < N-1) and A[i + 1] <= A[i]):
            i += 1
            
        if(i == (N - 1)):
            break
        
        buy = i
        i += 1
            
        while((i < N-1) and A[i] >= A[i - 1]):
            i += 1
            
        sell = (i - 1)
            
        print("Buy on day: ",buy,"\t","Sell on day: ",sell)

    



A = [100,180,260,310,40,535,695]
N = len(A)

stockBuySell(A, N)