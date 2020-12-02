'''
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. 
For example, "aba|b|bbabb|a|b|aba" is a palindrome partitioning of "ababbbabbababa". 
Determine the fewest cuts needed for a palindrome partitioning of a given string. 
For example, minimum of 3 cuts are needed for "ababbbabbababa". 
The three cuts are "a|babbbab|b|ababa". If a string is a palindrome, then minimum 0 cuts are needed. 
If a string of length n containing all different characters, then minimum n-1 cuts are needed.


https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

https://www.youtube.com/watch?v=qmTtAbOTqcg

refer rod cutting problem --> https://www.youtube.com/watch?v=eQuJb5gBkkc

'''
import sys

# O(n3) complexity

def palindrome_partition(s):
    
    n = len(s)
    
    dp = [[False for i in range(n)] for i in range(n)]
    
    gap = 0
    while(gap < n):
        
        i = 0
        j = gap
        while(j < n):
            
            if(gap == 0):
                dp[i][j] = True
            elif(gap == 1):
                dp[i][j] = s[i] == s[j]
            else:
                if(s[i] == s[j] and dp[i+1][j-1] == True):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                    
            i += 1
            j += 1
            
        gap += 1
            
    strg = [[0 for i in range(n)] for i in range(n)]
    
    gap = 0
    while(gap < n):
        
        i = 0
        j = gap
        while(j < n):
            
            if(gap == 0):
                strg[i][j] = 0
            elif(gap == 1):
                if(s[i] == s[j]):
                    strg[i][j] = 0
                else:
                    strg[i][j] = 1
            else:
                if(dp[i][j]):
                    strg[i][j] = 0
                else:
                    mini = sys.maxsize
                    
                    k = i
                    while(k < j):
                        left = strg[i][k]
                        right = strg[k+1][j]
                        mini = min(mini, left+right+1)
                        strg[i][j] = mini
                        k += 1
                        
            i += 1
            j += 1
        
        gap += 1
        
    return strg[0][n-1]

print(palindrome_partition("ababbbabbababa"))

# O(n2) solution

def palindrome_partition_1(s):
    
    n = len(s)
    
    dp = [[False for i in range(n)] for i in range(n)]
    
    gap = 0
    while(gap < n):
        
        i = 0
        j = gap
        while(j < n):
            
            if(gap == 0):
                dp[i][j] = True
            elif(gap == 1):
                dp[i][j] = s[i] == s[j]
            else:
                if(s[i] == s[j] and dp[i+1][j-1] == True):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                    
            i += 1
            j += 1
            
        gap += 1
            
    strg = [0 for i in range(n)]
    
    strg[0] = 0
    
    j = 1
    while(j < n):
        
        if(dp[0][j]):
            strg[j] = 0
        else:
            i = j
            mini = sys.maxsize
            while(i >= 1):
                if(dp[i][j]):
                    mini = min(mini, strg[i-1])
                i -= 1
                
        strg[j] = mini + 1
        j += 1
        
    return strg[n-1]

print(palindrome_partition_1("ababbbabbababa"))
                
        
            
    