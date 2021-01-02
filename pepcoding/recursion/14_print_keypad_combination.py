'''
1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map
    0 -> .;
   1 -> abc
   2 -> def
   3 -> ghi
   4 -> jkl
   5 -> mno
   6 -> pqrs
   7 -> tu
   8 -> vwx
   9 -> yz
   
Sample Input
78

Sample Output
tv
tw
tx
uv
uw
ux


https://www.youtube.com/watch?v=4yMtvToiJE0&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=35

'''
codes = [
        ".;",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tu",
        "vwx",
        "yz"
    ]

def getKeypadCombination(ques, ans):
    
    if(len(ques) == 0):
        print(ans)
        return
    
    ch = ques[:1]
    roq = ques[1:]
    
    codesforch = codes[int(ch)]
    
    for c in range(len(codesforch)):
        cho = codesforch[c]
        getKeypadCombination(roq, ans + cho)
        
getKeypadCombination("78", "")