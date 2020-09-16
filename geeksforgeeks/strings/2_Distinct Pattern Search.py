'''
Given a string S and a pattern P (of distinct characters) consisting of lowercase characters. 
The task is to check if pattern P exists in the given string S or not.

Note : Pattern has distinct characters. There might be repetitions in text.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains string S and next line contains pattern P.

Output:
For each testcase, print "Yes" if pattern is found in the given string, else print "No".

User Task:
The task is to complete the function search() which finds for the pattern with distinct characters. 
The function takes string and pattern as parameters and returns either true or false. Return true if pattern is found else return false.

Constraints:
1 <= T <= 100
1 <= |S|, |P| <= 103

Example:
Input:
2
abceabcdabceabcd
abcd
abceabcdabceabcd
gfhij

Output:
Yes
No

Hints:

1)
1.You should think of some technique with window sliding. 
Think of something which can be used for distinct characters in the pattern. Distinct characters in the pattern will help you optimize the window sliding.

2)
1.Use window sliding technique to find the pattern in given string.
2.Make a boolean function in which window starts from 0th index of the string and scan for the characters in the pattern.
3.At any point if you found that character in the pattern doesn't match with the character in window, then break from there and slide the window just
  after the previous point where character doesn't match in the window.
4.When a mismatch occurs after x(arbitrary number of characters) matches, we know that the first character of pattern will not match the x matched
  characters because all characters of pattern are different. So we can always slide the pattern by x without missing any valid shifts.

This concept uses efficient sliding window algorithm, as we have distinct characters in the pattern. 

def search(p,s):

'''

def search(p,s):
    
    m = len(p)
    n = len(s)
    
    for i in range(n - m + 1):
        
        j = 0
        
        for j in range(m):
            
            if(s[i + j] != p[j]):
                break
            j += 1
            
        if(j == 0):
            i += 1
                
        elif(j == m):
            return True
            
        else:
            i += j
    return False
   
if __name__ == '__main__':
    s = "abceabcdabceabcd"
    p = "abcd"
    print(search(p, s)) 