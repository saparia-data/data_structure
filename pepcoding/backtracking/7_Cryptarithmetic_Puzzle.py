'''
1. You are given three strings s1, s2 and s3.
2. First two are supposed to add and form third. s1 + s2 = s3
3. You have to map each individual character to a digit, so that the above equation holds true.

Sample Input:

team
pep
toppr

Sample Output:

a-3 e-9 m-4 o-1 p-2 r-6 t-0 
a-3 e-9 m-5 o-1 p-2 r-7 t-0 
a-3 e-9 m-6 o-1 p-2 r-8 t-0 
a-4 e-9 m-2 o-1 p-3 r-5 t-0 
a-4 e-9 m-5 o-1 p-3 r-8 t-0 
a-5 e-9 m-2 o-1 p-4 r-6 t-0 
a-5 e-9 m-3 o-1 p-4 r-7 t-0 
a-6 e-9 m-2 o-1 p-5 r-7 t-0 
a-6 e-9 m-3 o-1 p-5 r-8 t-0 
a-7 e-9 m-2 o-1 p-6 r-8 t-0 



https://www.youtube.com/watch?v=RG5rWV6in38&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=9

'''

def getNum(s, hash):
    
    num = ""
    
    for i in range(len(s)):
        ch = s[i]
        num += str(hash.get(ch))
        
    return int(num)
    
    
def solvePuzzle(unique, idx, hash, usedNumbers, s1, s2, s3):
    
    if(idx == len(unique)):
        
        num1 = getNum(s1, hash)
        num2 = getNum(s2, hash)
        num3 = getNum(s3, hash)
        
        if(num1 + num2 == num3):
            for i in range(26):
                ch = chr(ord('a') + i) # to print keys in alphabetical order
                if(ch in hash.keys()):
                    print(ch + "-" + str(hash[ch]) + " ", end = " ")
            print()
            
        return
    
    
    ch = unique[idx]
    
    for num in range(10):
        if(usedNumbers[num] == False):
            usedNumbers[num] = True
            hash[ch] = num
            solvePuzzle(unique, idx+1, hash, usedNumbers, s1, s2, s3)
            usedNumbers[num] = False
            hash[ch] = -1


if __name__ == "__main__":

    s1 = "team"
    s2 = "pep"
    s3 = "toppr"
    
    #hash all characters from all three strings such that no characters repeats
    
    hash = {}
    unique = ""
    
    # hash s1
    for i in range(len(s1)):
        if(s1[i] not in hash.keys()):
            hash[s1[i]] = -1
            unique += s1[i]
    
    # hash s2        
    for i in range(len(s2)):
        if(s2[i] not in hash.keys()):
            hash[s2[i]] = -1
            unique += s2[i]
    
    # hash s3        
    for i in range(len(s3)):
        if(s3[i] not in hash.keys()):
            hash[s3[i]] = -1
            unique += s3[i]
            
    #print(hash)
    #print(unique)
    
    usedNumbers = [False] * 10
    solvePuzzle(unique, 0, hash, usedNumbers, s1, s2, s3)
