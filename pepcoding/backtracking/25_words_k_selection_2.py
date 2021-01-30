'''
1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
3. You are required to generate and print all ways you can select k distinct characters out of the 
   word.


Sample Input:

aabbbccdde
3

Sample Output:

abc
abd
abe
acd
ace
ade
bcd
bce
bde
cde


https://www.youtube.com/watch?v=fy5mFaHVuRs&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=27


'''

def generateUniqueWords(uniqueStr, cs, ts, lc, asf):  # lc -> last choice
    
    if(cs > ts):
        print(asf)
        return
    
    for i in range(lc+1, len(uniqueStr)):
        generateUniqueWords(uniqueStr, cs + 1, ts, i, asf + uniqueStr[i])



if __name__ == "__main__":
    
    str = "aabbbccdde"
    k = 3
    
    uniqueChar = set()
    uniqueStr = ""
    
    for c in str:
        if(c not in uniqueChar):
            uniqueChar.add(c)
            uniqueStr += c
    
    #print(uniqueChar)
    #print(uniqueStr)
    
    generateUniqueWords(uniqueStr, 1, k, -1, "")