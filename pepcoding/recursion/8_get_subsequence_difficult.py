'''
1. You are given a string str. Print all sub-sequence of string.

sample input:
abc

sample output:
[, c, b, bc, a, ac, ab, abc]

https://www.youtube.com/watch?v=Sa5PmCFF_zI&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=25

'''

def getSubSequence(input):
    
    if(len(input) == 0):
        lst = []
        lst.append("")
        return lst
    
    ch = input[:1]
    ros = input[1:]
    rres = getSubSequence(ros)
    myres = []
    
    for char in rres:
        myres.append(char)
        
    for char in rres:
        myres.append(ch+char)
        
    return myres

print(getSubSequence("abc"))
    