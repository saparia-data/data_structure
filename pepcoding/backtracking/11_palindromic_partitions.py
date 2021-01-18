'''
1. You are given a string of length n.
2. You have to partition the given string in such a way that every partition is a palindrome.

Sample Input:

pep

Sample Output:

(p) (e) (p) 
(pep) 


https://www.youtube.com/watch?v=wvaYrOp94k0&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=13

'''

def isPalindrome(str):
    
    l = 0
    r = len(str) - 1
    
    while(l < r):
        if(str[l] != str[r]):
            return False
        l += 1
        r -= 1
        
    return True

def palindromicPartitions(str, asf):
    
    if(len(str) == 0):
        print(asf)
        return
    
    for i in range(len(str)):
        
        prefix = str[:i+1]
        ros = str[i+1:]
        
        if(isPalindrome(prefix) == True):
            palindromicPartitions(ros, asf + "(" + prefix + ") ")



if __name__ == "__main__":
    
    str = "pep"
    palindromicPartitions(str, "")