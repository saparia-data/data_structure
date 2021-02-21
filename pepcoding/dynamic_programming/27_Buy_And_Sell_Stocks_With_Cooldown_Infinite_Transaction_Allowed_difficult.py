'''
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed infinite transactions, 
   but have to cooldown for 1 day after 1 transaction
   i.e. you cannot buy on the next day after you sell, you have to cooldown for a day at-least before buying again.
   
   
Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) 
       before opening another transaction (another buy).
       
Input Format:

A number n
.. n more elements


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

Sample Output:

19


https://www.youtube.com/watch?v=GY0O57llkKQ&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=33


'''

def solution(arr, n):
    
    obsp = -arr[0]
    ossp = 0
    ocsp = 0
    
    for i in range(1, n):
        
        nbsp = 0
        nssp = 0
        ncsp = 0
        
        if(ocsp - arr[i] > obsp):
            nbsp = ocsp - arr[i]
        else:
            nbsp = obsp
            
        
        if(obsp + arr[i] > ossp):
            nssp = obsp + arr[i]
        else:
            nssp = ossp
            
        if(ossp > ocsp):
            ncsp = ossp
        else:
            ncsp = ocsp
            
        obsp = nbsp
        ossp = nssp
        ocsp = ncsp
        
    return ossp



if __name__ == "__main__":
    
    arr = [10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25]
    n = len(arr)
    print(solution(arr, n))