'''
Given a string S. The task is to print all permutations of a given string.

Input Format:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output Format:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Your Task:
This is a function problem. You only need to complete the function permutation that takes S as parameter 
and prints the permutations in lexicographically increasing order. The newline is automatically added by driver code.

Constraints:
1 ≤ T ≤ 100
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .

Hints:
1) Write a recursive function that employs swap to swap every character with every other character so as to generate all permutations.

'''

def toString(List): 
    return ''.join(List) 

def permute(a, l, r): 
    if l==r: 
        print(toString(a)) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            print(a,i)
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
            print(a,i)
# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1)

