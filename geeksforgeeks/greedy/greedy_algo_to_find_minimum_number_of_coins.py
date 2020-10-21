'''
Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency,
 i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, 
 what is the minimum number of coins and/or notes needed to make the change?
Examples:

Input: V = 70
Output: 2
We need a 50 Rs note and a 20 Rs note.

Input: V = 121
Output: 3
We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.

https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

'''

def findMin(V): 
      
    # All denominations of Indian Currency 
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000] 
    n = len(deno) 
      
    # Initialize Result 
    ans = [] 
    
    i = n - 1
    while(i >= 0): 
          
        # Find denominations 
        while (V >= deno[i]): 
            V -= deno[i] 
            ans.append(deno[i]) 
  
        i -= 1
        
    for i in ans:
        print(i, end = " ")
    
findMin(93)