'''
Understand how recursion works by guessing the output of this program
'''
def fun(n):
    
    if(n < 1):
        return
    else:
        print(n)
        fun(n-1)
        print(n)
               
fun(3)