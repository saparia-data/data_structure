'''
Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
Two strings str1 and str2 are called isomorphic,
if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.

Input:
The first line contains an integer T, depicting total number of test cases. Each test case contains two strings each in new line.

Output:
Print "1" if strings are isomorphic and "0" if not.

User Task:
The task is to complete the function areIsomorphic() which checks if two strings are isomorphic.
The function returns true if strings are isomorphic else it returns false.

Constraints:
1 <= T <= 100
1 <= Length of Strings <= 103

Example:
Input:
2
aab
xxy
aab
xyz
Output:
1
0

Explanation:
Testcase 1: There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.
Testcase 2: There are two different characters in aab but there are three different characters in xyz.
            So there wont't be one to one mapping between str1 and str2.
            
hints:

1) If lengths of str1 and str2 are not same, return false.
2) Do following for every character in str1 and str2
   a) If this character is seen first time in str1, 
      then current of str2 must have not appeared before.
      (i) If current character of str2 is seen, return false.
          Mark current character of str2 as visited.
      (ii) Store mapping of current characters.
   b) Else check if previous occurrence of str1[i] mapped
      to same character.
      
https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

'''
from _collections import defaultdict
def areIsomorphic(s,p):
    d = defaultdict(chr)
    marked = [0 for i in range(26)]
    
    if(len(s) != len(p)):
        return False
    
    for i in range(len(s)):
        c = s[i]
        c_p = p[i]
        
        if(c not in d):
            if(marked[ord(c) - ord('a')]):
                return False
            else:
                marked[ord(c) - ord('a')] = 1
                d[c] = c_p
                
        else:
            if(d[c] != c_p):
                return False
    return True
                
    
    
s = "aab"
p = "xxy"
print(areIsomorphic(s, p))