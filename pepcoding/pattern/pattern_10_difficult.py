'''
print below pattern

        *    
    *        *    
*                *    
    *        *    
        *    
        
'''

def print_pattern_10(n):
    
    n_space = n // 2;
    n_star = -1;
    
    for i in range(1, n+1):
        
        for j in range(1, n_space+1):
            print(" ", end="\t")
            
        print("*", end="\t")
        
        for j in range(1, n_star+1):
            print(" ", end="\t")
            
        if(i > 1 and i < n):
            print("*", end="\t")
            
        if(i <= n//2):
            n_space -= 1
            n_star += 2
        else:
            n_space += 1
            n_star -= 2
        
        print()
            
    
    
    
print_pattern_10(5)


