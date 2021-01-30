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


https://www.youtube.com/watch?v=4-Makzrj5qM&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=23&t=37s


'''

def generateWords(cs, ts, fmap, asf):
    
    if(cs > ts):
        print(asf)
        return
    
    
    for k in fmap.keys():
        if(fmap.get(k) > 0):
            fmap[k] = fmap.get(k) - 1
            generateWords(cs + 1, ts, fmap, asf + k)
            fmap[k] = fmap.get(k) + 1


if __name__ == "__main__":
    
    str = "aabb"
    fmap = {}
    
    #update frequency of every character in dict
    for i in range(len(str)):
        if(str[i] in fmap.keys()):
            val = fmap.get(str[i])
            fmap[str[i]] = val + 1
        else:
            fmap[str[i]] = 1
            
    generateWords(1, len(str), fmap, "")
            
