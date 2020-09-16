'''
You are given a string str. You need to remove the pair of duplicates.
Note: The pair should be of adjacent elements and after removing a pair the remaining string is joined together. 

Input:
The first line of input contains T denoting the number of test cases. T test cases follow. 
Each testcase contains one line of input containing string str.

Output:
For each testcase, in a new line, print the modified string. If the final string is empty, then print "Empty String".

Your Task:
This is a function problem. You only need to complete the function removePair() that takes a string as a parameter 
and returns the modified string. Return an empty string if the whole string is deleted.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
N = length of string.

Constraints:
1 <= T <= 100
1 <= |str| <= 103

Examples:
Input:
2
aaabbaaccd
aaaa
Output:
ad
Empty String

Explanation:
Testcase1: Remove (aa)abbaaccd =>abbaaccd
Remove a(bb)aaccd => aaaccd
Remove (aa)accd => accd
Remove a(cc)d => ad

Testcase 2: Remove (aa)aa => aa
Again removing pair of duplicates then (aa) will be removed and we will get 'Empty String'.

hints:

Push the first character into a stack.
pop if the top of the stack is equal to current character else push it into the stack.

'''
def removePair(s):
    
    stack = []
    
    stack.append(s[0])
    curr_index = 1
    
    while(curr_index < len(s)):
        if(len(stack) == 0):
            stack.append(s[curr_index])
            
        elif(s[curr_index] == stack[-1]):
            stack.pop()
            
        else:
            stack.append(s[curr_index])
            
        curr_index += 1
        
    ans = ""
    
    for char in stack:
        ans += char
        
    if(len(ans) == 0):
        ans = "Empty String"
        
    return ans

s = ['a','a','b','b','b','d','d','d','d']
print(removePair(s))