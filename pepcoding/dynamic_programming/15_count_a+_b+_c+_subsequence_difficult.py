'''
1. You are given a string str.
2. You are required to calculate and print the count of subsequences of the nature a+b+c+.

For abbc -> there are 3 subsequences. abc, abc, abbc
For abcabc -> there are 7 subsequences. abc, abc, abbc, aabc, abcc, abc, abc.


Sample Input:

abcabc

Sample Output:

7


https://www.youtube.com/watch?v=IV9pbZsi5cc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=21


'''

def countABCSubsequence(str):
    
    a = 0
    ab = 0
    abc = 0
    
    for i in range(len(str)):
        
        ch = str[i]
        
        if(ch == 'a'):
            a = 2 * a + 1
        elif(ch == 'b'):
            ab = 2 * ab + a
        elif(ch == 'c'):
            abc = 2 * abc + ab
            
    return abc


if __name__ == "__main__":
    
    str = "abcabc"
    
    print(countABCSubsequence(str))