'''
1. You are given a number n and a number k separated by a space, representing the number of houses and number of colors.
2. In the next n rows, you are given k space separated numbers representing the cost of painting nth house with one of the k colors.
3. You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.

Input Format:

A number n
n1-0th n1-1st n1-2nd .. n1-kth
n2-0th n2-1st n2-2nd .. n2-kth
.. n number of elements


Sample Input:

4 3

1 5 7
5 8 4
3 2 9

1 2 4

Sample Output:

8


https://www.youtube.com/watch?v=jGywRalvoRw&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=24


'''
import sys


# O(n3) solution
def paintHouseManyColours(arr, n, c):
    
    dp = [[0 for j in range(c)] for i in range(n)]
    #print(dp)
    
    for i in range(len(arr[0])): # fill first row as it is
        dp[0][i] = arr[0][i]
        
    print(dp)
    
    for i in range(1, len(dp)):
        
        for j in range(len(dp[0])):
            
            minn = sys.maxsize
            
            for k in range(len(dp[0])):
                
                if(k != j):
                    if(dp[i - 1][k] < minn):
                        minn = dp[i - 1][k]
                        
            dp[i][j] = arr[i][j] + minn
            
    
    minn = sys.maxsize
    for i in range(len(dp[0])):
        if(dp[n - 1][i] < minn):
            minn = dp[n - 1][i]
    
    print(dp)
    return minn



# O(n2) solution
def paintHouseManyColoursOptimized(arr, n, c):
    
    dp = [[0 for j in range(c)] for i in range(n)]
    #print(dp)
    
    least = sys.maxsize
    sleast = sys.maxsize # second least
    
    for i in range(len(arr[0])): # fill first row as it is
        dp[0][i] = arr[0][i]
        
        if(arr[0][i] <= least):
            sleast = least
            least = arr[0][i]
        elif(arr[0][i] <= sleast):
            sleast = arr[0][i]
        
    print(dp)
    
    
    for i in range(1, len(dp)):
        
        nleast = sys.maxsize # new least
        nsleast = sys.maxsize # new second least
        
        for j in range(len(dp[0])):
            #print(least, sleast)
            if(least == dp[i - 1][j]):
                dp[i][j] = sleast + arr[i][j]
            else:
                dp[i][j] = least + arr[i][j]
             
            #print(dp)   
                
            if(dp[i][j] <= nleast):
                nsleast = nleast
                nleast = dp[i][j]
            elif(dp[i][j] <= nsleast):
                nsleast = dp[i][j]
                
        
        least = nleast
        sleast = nsleast
        
    print(dp)
    return least 
                
            




if __name__ == "__main__":
    
    n = 4 # number of houses
    c = 3 # number of colours
    arr = [
            [1, 5, 7],
            [5, 8, 4],
            [3, 2, 9],
            [1, 2, 4]
          ]
    
    print(paintHouseManyColours(arr, n, c))
    print(paintHouseManyColoursOptimized(arr, n, c))