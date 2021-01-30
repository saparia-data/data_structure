'''
1. You are given a string which represents digits of a number.
2. You have to create the maximum number by performing at-most k swap operations on its digits.


Sample Input:

1234567
4

Sample Output:

7654321

https://www.youtube.com/watch?v=5crucASFoA4&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=24

'''

maxx = "0"

def swap(str, i, j):
    
    ith = str[i]
    jth = str[j]
    
    left = str[:i]
    middle = str[i+1:j]
    right = str[j+1:]
    
    return left + jth + middle + ith + right

def generateMaxNumber(str, k):
    
    global maxx
    
    if(int(str) > int(maxx)):
        maxx = str
        
    if(k == 0):
        return
    
    for i in range(len(str) - 1):
        for j in range(i+1, len(str)):
            if(str[i] < str[j]):
                str = swap(str, i, j)
                generateMaxNumber(str, k - 1)
                str = swap(str, i, j)
    



if __name__ == "__main__":
    
    str = "1234567"
    k = 4 # number of max swap
    generateMaxNumber(str, k)
    print(maxx)