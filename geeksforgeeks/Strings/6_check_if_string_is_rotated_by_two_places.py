'''
Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. In the next two lines are two string a and b respectively.

Output:
For each test case in a new line print 1 if the string 'a' can be obtained by rotating string 'b' by two places else print 0.

User Task:
The task is to complete the function isRotated() which checks if given strings can be formed by rotations.
The function returns true if string 1 can be obtained by rotating string 2 by two places, else it returns false.

Expected Time Complexity: O(N).
Expected Space Complexity: O(N).
Challenge: Try doing it in O(1) space complexity.

Constraints:
1 <= T <= 50
1 <= length of a, b < 100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor
Output:
1
0

Explanation:
Testcase 1: amazon can be rotated anti-clockwise by two places, which will make it as azonam.
Testcase 2: If we rotate geeksforgeeks by two place in any direction , we won't get geeksgeeksfor.


hints:

Step1: There can be only two cases:
    a) Clockwise rotated
    b) Anti-clockwise rotated

Step 2: If clockwise rotated that means elements are shifted in right. So, check if a substring[2.... len-1] of string2
        when concatenated with substring[0,1] of string2 is equal to string1. Then, return true.

Step 3: Else, check if it is rotated anti-clockwise that means elements are shifted to left.
        So, check if concatenation of substring[len-2, len-1] with substring[0....len-3] makes it equals to string1. Then return true.

Step 4: Else, return false.

'''

def isRotated(s,p):
    n=len(p)
    if(n<3):
        return p==s
    anticlock_str=p[2:]+p[0:2]
    clockwise_str=p[-2]+p[-1]+p[:n-2]
    
    if(s==anticlock_str or s==clockwise_str):
        return True
    return False
    
s = "amazon"
p = "onamaz"
print(isRotated(s, p))