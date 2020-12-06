'''
print below pattern

        *    
    *   *    *    
*    *  *    *    *    
    *   *    *    
        *    


'''

def print_pattern_5(n):
    
    n_space = n//2
    n_star = 1
    
    for i in range(1,n+1):
        
        for j in range(n_space):
            print(" ", end="\t")
            
        for j in range(n_star):
            print("*", end="\t")
            
        if(i <= n//2):
            n_space -= 1
            n_star += 2
        else:
            n_space += 1
            n_star -= 2
            
        print()
        
print_pattern_5(5)
        
        
        