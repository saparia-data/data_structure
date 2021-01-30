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


https://www.youtube.com/watch?v=PiwttDa5FMA&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=26


'''

def generateUniqueWords(i, uniqueStr, ssf, ts, asf):
    
    if(i == len(uniqueStr)):
        if(ssf == ts):
            print(asf)
            
        return
    
    
    
    ch = uniqueStr[i]
    generateUniqueWords(i+1, uniqueStr, ssf, ts, asf + "")
    generateUniqueWords(i+1, uniqueStr, ssf + 1, ts, asf + ch)


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
    
    generateUniqueWords(0, uniqueStr, 0, k, "")