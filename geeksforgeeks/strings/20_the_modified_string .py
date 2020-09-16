'''
Ishaan is playing with strings these days. He has found a new string. 
He wants to modify it as per the following rules to make it valid:

-The string should not have three consecutive same characters (Refer example for explanation).
-He can add any number of characters anywhere in the string.
-Find the minimum number of characters which Ishaan must insert in the string to make it valid.

Input: 
The first line of input contains a single integer T denoting the number of test cases. 
The only line of each test case contains a string S consisting of lowercase English Alphabets.

Output: 
For each test case, in a new line,  print the required answer in a new line.

Your Task:
This is a function problem. You only need to complete the function modified that returns the answer.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints : 
1 <= T <= 100
1 <= Length of S <= 105

Example : 
Input : 
3
aabbbcc
aaaaa
abcddee
Output : 
1
2
0

Explanation : 
Testcase 1: In aabbbcc 3 b's occur consecutively, we add a 'd',and Hence, output will be aabbdbcc.
Testcase 2: In aaaaa 5 a's occur consecutively, we need to add 2 'b', and Hence, the output will be aababaa.
Testcase 3: In abcddee, No character occurs 3 times, so no need to add anything.

hints:

1)
Start travesing string, and do following steps while traversing
-Step1: Keep count of same characters while traversing, suppose i.e. same
-Step2: Whenever a different character is encouneterd compute number of characters required to be added as (same-1)/2, keep adding  to ans.
-Step3: Make same = 1 after computing. And repeat steps1 to 3 for rest of characters.

'''
def modified(s):
    ans = 0
    same = 1
    
    for i in range(1, len(s)):
        
        if(s[i] == s[i-1]):
            same += 1
        else:
            ans += (same - 1) // 2
            same = 1
            
    ans += (same - 1) // 2
    return ans

s = "aabbbccc"
print(modified(s))