'''
Given a string S and a pattern P of lowercase characters. The task is to check if the pattern is present in string or not.

Input:
The first line of input contains the number of test cases T. For each testcase, 
the first line of input contains string S and the next line contains pattern P.

Output:
For each testcase, print "Yes" if the pattern is found in the string else print "No".

Your Task:
This is a function problem. You need to complete the function search which takes 3 arguments(S, P and prime q) 
and returns true if the pattern is found else returns false.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(1).
Note: N = |S|, M = |P|.

Constraints:
1 <= T <= 100
1 <= |S|, |P| <= 104

Example:
Input:
2
aabaacaadaabaaba
aaba
aabaacaadaabaaba
asdfa
Output:
Yes
No

Explanation:
Testcase 1: You can find the patter at starting at index 12.
Testcase 2: Pattern doesn't exist in the given string S.

'''
d = 256
def Rabin_Karp(pat, txt, q):
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
    p = 0    # hash value for pattern 
    t = 0    # hash value for txt 
    h = 1
    
    # The value of h would be "pow(d, M-1)% q"
    for i in range(M-1): 
        h = (h * d)% q
        #print(h)
        
    # Calculate the hash value of pattern and first window of text 
    for i in range(M): 
        p = (d * p + ord(pat[i]))% q 
        t = (d * t + ord(txt[i]))% q 
        
    # Slide the pattern over text one by one 
    for i in range(N-M + 1):
        # Check the hash values of current window of text and 
        # pattern if the hash values match then only check 
        # for characters on by one 
        if p == t: 
            # Check for characters one by one 
            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break
            j+= 1
            
            if j == M: 
                return True
            
        # Calculate hash value for next window of text: Remove 
        # leading digit, add trailing digit 
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
            
            # We might get negative values of t, converting it to 
            # positive 
            if t < 0: 
                t = t + q
    return i 
        
        
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
print(Rabin_Karp(pat, txt, q))