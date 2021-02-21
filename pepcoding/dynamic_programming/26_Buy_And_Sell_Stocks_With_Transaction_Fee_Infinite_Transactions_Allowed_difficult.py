'''
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are give a number fee, representing the transaction fee for every transaction.
4. You are required to print the maximum profit you can make if you are allowed infinite transactions, 
   but has to pay "fee" for every closed transaction.

Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) 
       before opening another transaction (another buy).

Input Format:

A number n
.. n more elements
A number fee


Sample Input:

12

10
15
17
20
16
18
22
20
22
20
23
25

3

Sample Output:

13


https://www.youtube.com/watch?v=pTQB9wbIpfU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=32


'''

def solution(arr, n, fee):
    
    obsp = -arr[0]
    ossp = 0
    #print(obsp, ossp)
    
    for i in range(1, n):
        
        nbsp = 0
        nssp = 0
        
        if(ossp - arr[i] > obsp):
            nbsp = ossp - arr[i]
        else:
            nbsp = obsp
            
        if(obsp + arr[i] - fee > ossp):
            nssp = obsp + arr[i] - fee
        else:
            nssp = ossp
            
        obsp = nbsp
        ossp = nssp
        
    return ossp


if __name__ == "__main__":
    
    arr = [10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25]
    n = len(arr)
    fee = 3
    print(solution(arr, n, fee))