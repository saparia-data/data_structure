'''
1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map :
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

678

Sample Output
[tv, tw, tx, uv, uw, ux]

['ptv', 'ptw', 'ptx', 'puv', 'puw', 'pux', 'qtv', 'qtw', 'qtx', 'quv', 'quw', 'qux', 'rtv', 'rtw', 'rtx', 'ruv', 'ruw', 'rux', 'stv', 'stw', 'stx', 'suv', 'suw', 'sux']

https://www.youtube.com/watch?v=3fjt19bjs3A&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=27

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

def getKeypadCombination(str):
    
    if(len(str) == 0):
        bres = []
        bres.append("")
        return bres
    
    ch = str[:1]
    ros = str[1:]
    
    rres = getKeypadCombination(ros)
    mres = []
    
    codeforch = codes[int(ch)]
    
    for i in range(len(codeforch)):
        chcode = codeforch[i]
        for char in rres:
            mres.append(chcode + char)
        
    return mres

print(getKeypadCombination("78"))
print(getKeypadCombination("678"))
