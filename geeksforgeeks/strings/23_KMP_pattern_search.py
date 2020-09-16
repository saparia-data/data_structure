'''
Given a string S and a pattern P of all lowercase characters. The task is to check if the pattern exists in the string or not.

Input:
The first line of input contains the number of test cases T. For each testcase, 
the first line of input contains string S and the next line contains pattern P.

Output:
For each testcase, print "Yes" if the pattern is found in the string, and "No" if the pattern is not found in the string.

Your Task:
The task is to complete the function KMPSearch() which returns true or false depending on whether pattern is present in the string or not, 
and computeLPSArray() which computes the longest prefix suffix for every index.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(M).
Note: N = |S|, M = |P|.

Constrsaints:
1 <= T <= 100
1 <= |S|, |P| <= 104

Example:
Input:
2
aabaacaadaabaaba
aaaab
aabaacaadaabaaba
caada
Output:
No
Yes

Explanation:
Testcase 1: Given pattern is not found in the given string S.
Testcase 2: Given pattern is found in the given string S.

https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
Refer videos also

'''
def computeLPSArray(pat, M, lps):
    lps[0]
    len = 0
    i = 1
    
    while(i < M):
        if(pat[i] == pat[len]):
            len += 1
            lps[i] = len
            i += 1
        else:
            if(len != 0):
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    i, j = 0, 0
    lps = [0] * M
    
    computeLPSArray(pat, M, lps)
    
    while(i < N):
        if(pat[j] == txt[i]):
            i += 1
            j += 1
        
        if(j == M):
            return True
        
        elif(i < N and pat[j] != txt[i]):
            if(j != 0):
                j = lps[j - 1]
            else:
                i += 1
    return False

txt = "aabaacaadaabaaba"
pat = "caada"
print(KMP(pat, txt))
                