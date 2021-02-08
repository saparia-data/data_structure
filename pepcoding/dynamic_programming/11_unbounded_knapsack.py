'''
1. You are given a number n, representing the count of items.
2. You are given n numbers, representing the values of n items.
3. You are given n numbers, representing the weights of n items.
3. You are given a number "cap", which is the capacity of a bag you've.
4. You are required to calculate and print the maximum value that can be created in the bag without 
   overflowing it's capacity.
   
Note -> Each item can be taken any number of times. You are allowed to put the same item again 
        and again.


Sample Input:

5

15 14 10 45 30
2 5 1 3 4

7

Sample Output:

100


https://www.youtube.com/watch?v=jgps7MXtKRQ&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=17


'''

def unboundedKnapsack(n, wts, vals, capacity):
    
    dp = [0] * (capacity + 1)
    
    dp[0] = 0
    
    for bagCapacity in range(1, len(dp)):
        
        maxx = 0
        
        for i in range(n):
            
            if(wts[i] <= bagCapacity):
                
                remainingCapacity = bagCapacity - wts[i]
                totalCapacity = dp[remainingCapacity] + vals[i]
                if(totalCapacity > maxx):
                    maxx = totalCapacity
                    
        dp[bagCapacity] = maxx
        
    return dp[capacity]
                



if __name__ == "__main__":
    
    n = 5
    vals = [15, 14, 10, 45, 30]
    wts = [2, 5, 1, 3, 4]
    capacity = 7
    
    print(unboundedKnapsack(n, wts, vals, capacity))