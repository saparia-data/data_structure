'''
Given a string S and a pattern P both of lowercase characters. The task is to check if the given pattern exists in the given string or not.

Input:
First line of input contains number of testcases T. For each testcase, first line will the string and second line will be the pattern to be searched.

Output:
For each testcase, print "Yes" if pattern exists or "No" if doesn't.

User Task:
The task is to complete the function search() which finds the pattern in the given string. 
The function takes pattern and string as parameters and returns either true or false. Return true if pattern exists else return false.

Constraints:
1 <= T <= 100
1 <= |S|, |P| <= 103

Example:
Input:
2
aabaacaadaabaaabaa
aaba
aabaacaadaabaaabaa
ccda

Output:
Yes
No

Hints:
1. Simply apply brute force to search for the pattern. Take a function of boolean type and start from a window of size equal to the size of pattern.
2. If you are getting character matched with the window in string, then continue for next character, 
else break and start checking for window slided with one to the right.
3. In this way, iterate till whole string exhausted.
4. If anywhere you found a match with the pattern, then return true from the function which you are using for pattern search.

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
            
        if(j == m):
            return True
    return False

if __name__ == '__main__':
    s = "AABAACAADAABAAABAA"
    p = "ABAA"
    print(search(p, s)) 