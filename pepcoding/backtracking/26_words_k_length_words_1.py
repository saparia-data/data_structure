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


https://www.youtube.com/watch?v=ZmAoj7wpMvM&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=28


'''

def generateUniqueWordsKLength(cc, uniqueStr, ssf, ts, spots):
    
    if(cc == len(uniqueStr)):
        
        if(ssf == ts):
            
            for c in spots:
                    print(c, end = "")
                
            print()
        
        return
    
    ch = uniqueStr[cc]
    
    for i in range(len(spots)):
        if(spots[i] == None):
            spots[i] = ch
            generateUniqueWordsKLength(cc + 1, uniqueStr, ssf + 1, ts, spots)
            spots[i] = None
            
    generateUniqueWordsKLength(cc + 1, uniqueStr, ssf, ts, spots)


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
    
    spots = [None] * k
    
    generateUniqueWordsKLength(0, uniqueStr, 0, k, spots)