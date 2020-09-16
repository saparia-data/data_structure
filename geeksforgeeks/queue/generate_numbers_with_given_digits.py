'''
Suppose given digits are 5 and 6, We need to generate numbers in increasing order which have 5 and 6 only

Example:

if n = 5

output should be -> 5,6,55,56,65,66,555

'''

from queue import Queue

def printDigits(n1, n2, n):
    
    q = Queue()
    q.put(str(n1))
    q.put(str(n2))
    
    res = []
    
    
    while(n > 0):
        n -= 1
        curr = q.get()
        
        res.append(curr)
        
        q.put(curr + "5")
        q.put(curr + "6")
           
    return res

n1 = 5
n2 = 6
n = 7
print(printDigits(n1, n2, n))
        
        