'''
1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
3. You are required to generate and print all k length words (of distinct chars) by using chars of the 
   word.
   
   
Sample Input:

aabbbccdde
3

Sample Output:

abc
abd
abe
acb
adb
aeb
acd
ace
adc
aec
ade
aed
bac
bad
bae
cab
dab
eab
cad
cae
dac
eac
dae
ead
bca
bda
bea
cba
dba
eba
cda
cea
dca
eca
dea
eda
bcd
bce
bdc
bec
bde
bed
cbd
cbe
dbc
ebc
dbe
ebd
cdb
ceb
dcb
ecb
deb
edb
cde
ced
dce
ecd
dec
edc


https://www.youtube.com/watch?v=_geihPcxPag&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=29


'''

def generateUniqueWordsKLength(cs, ts, uniqueStr, usedChar, asf):
    
    if(cs > ts):
        print(asf)
        return
    
    for i in range(len(uniqueStr)):
        
        ch = uniqueStr[i]
        if(ch not in usedChar):
            usedChar.add(ch)
            generateUniqueWordsKLength(cs + 1, ts, uniqueStr, usedChar, asf + ch)
            usedChar.remove(ch)


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
    
    generateUniqueWordsKLength(1, k, uniqueStr, set(), "")