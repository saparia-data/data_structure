def isPalindromeRecursive(st, f, l):
    print("f=" + str(f) + " l=" + str(l))
    if(f == l):
        return True
    
    if(st[f] != st[l]):
        return False
    
    if(f < l):
        return isPalindromeRecursive(st, f+1, l-1)
    return True
    
def checkPalindrome(st):
    n= len(st)
    if(n == 0):
        return True
    
    return isPalindromeRecursive(st, 0, n-1)

'''
def iterativePalindrome(st):
    n = len(st)
    
    for i in range(n+1):
'''    
    

st = "geeg"
print(checkPalindrome(st))

