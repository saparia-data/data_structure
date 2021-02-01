'''
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number "tar".
4. You are required to calculate and print true or false, if there is a subset the elements of which add 
   up to "tar" or not.
   
   
Sample Input:

5

4
2
7
1
3

10

Sample Output:

true


https://www.youtube.com/watch?v=CqEsqfidKi0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=10
https://www.youtube.com/watch?v=tRpkluGqINc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=11


'''

def targetSumSubset(arr, n, tar):
    
    dp = [[False for j in range(tar+1)] for i in range(n+1)]
    #print(dp)
    
    for i in range(len(dp)):
        
        for j in range(len(dp[0])):
            
            if(i == 0 and j == 0):
                dp[i][j] = True
                
            elif(i == 0):
                dp[i][j] = False
                
            elif(j == 0):
                dp[i][j] = True
                
            else:
                
                if(dp[i-1][j] == True):
                    dp[i][j] = True
                
                else:
                    val = arr[i-1]
                    
                    if(j >= val):
                        
                        if(dp[i-1][j-val] == True):
                            dp[i][j] = True

    
    return dp[n][tar]
    

if __name__ == "__main__":
    
    n = 5
    arr = [4,2,7,1,3]
    tar = 10
    print(targetSumSubset(arr, n, tar))