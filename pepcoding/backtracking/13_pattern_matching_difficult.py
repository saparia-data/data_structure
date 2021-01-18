'''
1. You are given a string and a pattern. 
2. You've to check if the string is of the same structure as pattern without using any regular 
   expressions.
   

Sample Input:

graphtreesgraph
pep

Sample Output:

p -> graph, e -> trees, . 

https://www.youtube.com/watch?v=aVMyXDuSLNM&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=15&t=1s


'''
def patternMatching(str, pattern, hashMap, originalPattern):
    
    if(len(pattern) == 0):
        if(len(str) == 0):
            alreadyUsed = {}
            op = set(originalPattern) # here we require this to print only unique pattern and it's match
            for c in originalPattern:
                if(c not in alreadyUsed.keys()):
                    print(c + "->" + hashMap.get(c), end = " ,")
                    alreadyUsed[c] = True
            
        return
        
    
    
    ch = pattern[:1]
    rop = pattern[1:]
    
    if(ch in hashMap.keys()):
        previousMapping = hashMap.get(ch)
        
        if(len(str) >= len(previousMapping)):
            left = str[:len(previousMapping)]
            right = str[len(previousMapping):]
            if(previousMapping == left):
                patternMatching(right, rop, hashMap, originalPattern)
    else:
        
        for i in range(len(str)):
            left = str[:i+1]
            right = str[i+1:]
            hashMap[ch] = left
            patternMatching(right, rop, hashMap, originalPattern)
            hashMap.pop(ch)


if __name__ == "__main__":
    
    str = "graphtreesgraph"
    pattern = "pep"
    hashMap = {}
    patternMatching(str, pattern, hashMap, pattern)
    