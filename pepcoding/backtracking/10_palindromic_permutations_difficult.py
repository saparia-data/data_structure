'''
1. You are given a string of length n.
2. You have to print all the palindromic permutations of the given string.
3. If no palindromic permutation exists for the given string, print "-1".

Sample Input:

aaabb

Sample Output:

ababa
baaab


https://www.youtube.com/watch?v=DwdWafLsGm0&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=12

'''

def reverseString(string):
    
    string = string[::-1] 
    return string

def generatePalindromicPermutations(currentSpot, totalSpot, hashMap, oddChar, asf):
    
    if(currentSpot > totalSpot):
        
        result = asf
        
        if(oddChar is not None):
            result += oddChar
            
        result += reverseString(asf)
        
        print(result)
        
        return
    
    for ch in hashMap.keys():
        freq = hashMap[ch]
        if(freq > 0):
            hashMap[ch] -= 1
            generatePalindromicPermutations(currentSpot + 1, totalSpot, hashMap, oddChar, asf + ch)
            hashMap[ch] = freq
    
    


if __name__ == "__main__":
    
    str = "aaabb"
    hashMap = {}
    
    # insert all chars and it's frequency in dict
    for ch in str:
        if(ch in hashMap.keys()):
            of = hashMap[ch]
            hashMap[ch] = of + 1
        else:
            hashMap[ch] = 1
        
    odds = 0
    oddChar = ""
    length = 0 # length of string
    
    # identify number of characters having off frequency
    
    for k in hashMap.keys():
        freq = hashMap[k]
        
        if(freq % 2 == 1):
            oddChar = k
            odds += 1
            
        hashMap[k] = freq // 2
        length += freq // 2 # here total frequency is equal to length of string
            
    if(odds > 1):
        print(-1)
    
    
    print(hashMap)
    generatePalindromicPermutations(1, length, hashMap, oddChar, "")
            
        
        