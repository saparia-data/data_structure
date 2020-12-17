'''
print below pattern

        1    
    2   3   2    
3   4   5    4    3    
    2   3    2    
        1    

'''

def print_pattern_15(n):
    
    oval = 1
    stars = 1
    spaces = n // 2
    
    for i in range(1, n+1):
        val = oval
        for j in range(1, spaces+1):
            print(" ", end="\t")
            
        for j in range(1, stars+1):
            print(val, end="\t")
            if(j <= stars // 2):
                val +=1
            else:
                val -= 1
                
        print()
        if(i <= n//2):
            oval += 1
            spaces -= 1
            stars += 2
        else:
            oval -= 1
            spaces += 1
            stars -= 2
            
    
    
    
print_pattern_15(5)