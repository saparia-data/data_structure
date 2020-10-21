'''
A boy lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. 
He know that his password is the largest number of N digits that can be possible with given sum S. 
As he is busy doing his homework, help him retrieving his password.

Example 1:
Input:
N = 5, S = 12
Output: 93000
Explanation: Sum of elements is 12.
Largest possible 5 digit number is 93000.

Example 2:
Input:
N = 3, S = 29
Output: -1
Explanation: There is no such three digit
number whose sum is 29.



'''

def largestNum(n,s):
    
    if(s > 9 * n):
        return -1
    
    else:
        
        # base case
        if(n == 1 and s == 0):
            return s
        
        # maximum number of nines we can get
        nines = s // 9
        
        # the remaining digit
        s = s%9
        
        ans = '9' * nines
        
        if(len(ans) < n):
            ans += str(s)
            
            for i in range(n - nines - 1):
                ans += '0'
                
    return ans

s = 12
n = 5
print(largestNum(n, s))