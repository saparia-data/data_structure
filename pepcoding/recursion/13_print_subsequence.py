'''
Sample Input
yvTA

Sample Output
yvTA
yvT
yvA
yv
yTA
yT
yA
y
vTA
vT
vA
v
TA
T
A


https://www.youtube.com/watch?v=Ke8TPhHdHMw&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=34&t=36s

'''

def getSubSequence(ques, ans):
    
    if(len(ques) == 0):
        print(ans)
        return
    
    ch = ques[:1]
    ros = ques[1:]
    
    getSubSequence(ros, ans + ch)
    getSubSequence(ros, ans + "")
    
getSubSequence("abc", "")