'''
1. You are given a string str.
2. Print all permutations of a string.

Sample Input:

abc

Sample Output:

abc
acb
bac
bca
cab
cba

https://www.youtube.com/watch?v=sPAT_DbvDj0&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=43


'''

def printPermutations(ques, asf):
    
    if(len(ques) == 0):
        print(asf)
        return
    
    for i in range(len(ques)):
        ch = ques[i]
        qlpart = ques[:i]
        qrpart = ques[i+1:]
        ros = qlpart + qrpart
        printPermutations(ros, asf + ch)
        
        
printPermutations("abc", "")
        