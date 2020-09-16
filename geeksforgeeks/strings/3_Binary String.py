'''
Given a binary string S. The task is to count the number of substrings that start and end with 1. 
For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Each test case consist of an integer 'N' denoting the string length and next line is followed by a binary string.

Output:
For each testcase, in a new line, print the number of substring starting and ending with 1 in a separate line.

User Task:
The task is to complete the function binarySubstring() which counts the number of substrings starting and ending with 1 and returns count.

Constraints:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 104

Example:
Input:
2
4
1111
5
01101

Output:
6
3

Hints:

1)
1. Although this question is of string. You should think from mathematics point of view which help you get efficient algorithm.

2)
Formula to be used:

ans=n*(n-1)/2
This formula is to find total number of pairs form from an "n" elements.
So we count toal number of "1" in binary strings and apply above formula.

https://math.stackexchange.com/questions/2214839/exactly-how-does-the-equation-nn-1-2-determine-the-number-of-pairs-of-a-given

where n is the number of set bits.

def binarySubstring(n,s):

'''
print("---------------------------------------------")
def binarySubstring(n,s):
    count = 0
    
    for i in range(n):
        
        if(s[i] == '1'):
            
            for j in range(i+1,n):
                if(s[j] == '1'):
                    count += 1
                    
    return count
#complexity is O(n)
print("---------------------------------------------")

def binarySubstring(n,s):
    
    m = 0
    
    for i in range(n):
        if(s[i] == '1'):
            m += 1
            
    return m * (m - 1)//2

if __name__ == '__main__':
    
    s = "1111";
    n= len(s) 
    print(binarySubstring(n,s)) 
        
        
        
        
        