'''
Given two strings s1 and s2. The task is to check if s2 is a rotated version of the string s1.
The characters in the strings are in lowercase.

Input:
The first line of the input contains a single integer T, denoting the number of test cases.
Then T test case follows. Each testcase contains two lines for s1 and s2.

Output:
For each testcase, in a new line, print "1" if s2 is a rotated version of s1 else print "0".

User Task:
The task is to complete the function areRotations() which checks if the two strings are rotations of each other.
The function returns true if string 1 can be obtained by rotating string 2, else it returns false.

Constraints:
1 <= T <= 103
1 <= |s1|, |s2| <= 107

Example:
Input:
4
geeksforgeeks
forgeeksgeeks
mightandmagic
andmagicmigth
mushroomkingdom
itsamemario
geekofgeeks
geeksgeekof
Output:
1
0
0
1

Explanation:
Testcase 1: s1 is geeksforgeeks, s2 is forgeeksgeeks. Clearly, s2 is a rotated version of s1 as s2 can be obtained by left-rotating s1 by 5 units.
Testcase 2: Here with any amount of rotation s2 can't be obtained by s1.
Testcase 3: S1 and s2 are completely different strings so s2 can't be obtained by any rotation of s1.
Testcase 4: s1 is geekofgeeks, s2 is geeksgeekof. Clearly , s2 is a rotated version of s1. 

hints:

Step 1: Create a temp string and store concatenation of str1 to str1 in temp. 
             temp = str1.str1
Step 2: If str2 is a substring of temp then str1 and str2 are 
            rotations of each other.
Example:                 
                     str1 = "ABACD"
                     str2 = "CDABA"

     temp = str1.str1 = "ABACDABACD"
     Since str2 is a substring of temp, str1 and str2 are 
     rotations of each other.

'''
def areRotations(s1,s2):
    
    temp = s1 + s2
    if(len(s1) == len(s2) and s2 in temp):
        return True
    return False
    
    
s1="geeksforgeeks"
s2="forgeeksgeeks"
print(areRotations(s1, s2))