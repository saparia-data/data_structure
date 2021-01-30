'''
1. You are given a word (may have one character repeat more than once).
2. You are required to generate and print all arrangements of these characters.

Sample Input:

aabb

Sample Output:

aabb
abab
abba
baab
baba
bbaa

https://www.youtube.com/watch?v=D7kSjpIVQFA&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=25

'''

def generateWords(currentChar, str, spots, lastOccurence):
    
    if(currentChar == len(str)):
        
        for c in spots:
            print(c, end="")
            
        print()
        
        return
    
    ch = str[currentChar]
    lo = lastOccurence.get(ch) # lo -> last occurence in which spot
    
    for i in range(lo + 1, len(str)):
        
        if(spots[i] == None):
            spots[i] = ch
            lastOccurence[ch] = i
            generateWords(currentChar + 1, str, spots, lastOccurence)
            spots[i] = None
            lastOccurence[ch] = lo



if __name__ == "__main__":
    
    str = "aabb"
    
    spots = [None] * len(str)
    lastOccurence = {}
    
    for ch in str:
        lastOccurence[ch] = -1
        
    generateWords(0, str, spots, lastOccurence)
    