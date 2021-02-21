'''
1. You are given a number n, representing the number of days.
2. You are given n numbers, where ith number represents price of stock on ith day.
3. You are required to print the maximum profit you can make if you are allowed two transactions at-most.

Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) 
       before opening another transaction (another buy).
       

Input Format:

A number n
.. n more elements


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



https://www.youtube.com/watch?v=wuzTpONbd-0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=34&t=1s


'''

def solution(arr, n):
    
    mpist = 0 # max profit if sold today
    leastsf = arr[0] # least so far
    dp_left = [0] * len(arr)
    
    for i in range(1, len(arr)):
        
        if(arr[i] < leastsf):
            leastsf = arr[i]
            
        mpist = arr[i] - leastsf
        
        if(mpist > dp_left[i-1]):
            dp_left[i] = mpist
        else:
            dp_left[i] = dp_left[i-1]
            
            
    mpibt = 0 # max profit if bought today
    maxat = arr[len(arr) - 1] # max after today
    dp_right = [0] * len(arr)
    
    for i in range(len(arr) - 2, -1, -1):
        
        if(arr[i] > maxat):
            maxat = arr[i]
            
        mpibt = maxat - arr[i]
        
        if(mpibt > dp_right[1+1]):
            dp_right[i] = mpibt
        else:
            dp_right[i] = dp_right[i+1]
            
    op = 0 # overall profit
    
    for i in range(len(arr)):
        if(dp_left[i] + dp_right[i] > op):
            op = dp_left[i] + dp_right[i]
            
    return op
    
    


if __name__ == "__main__":
    
    arr = [11, 6, 7, 19, 4, 1, 6, 18, 4]
    n = len(arr)
    
    print(solution(arr, n))