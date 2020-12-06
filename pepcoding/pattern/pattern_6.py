'''
print below pattern

*    *    *        *    *    *    
*    *                  *    *    
*                            *    
*    *                  *    *    
*    *    *        *    *    *    

'''

def print_pattern_6(n):
    
    n_star = n//2 + 1
    n_space = 1
    
    for i in range(1, n+1):
        
        for j in range(n_star):
            print("*", end=" ")
            
        for j in range(n_space):
            print(" ", end=" ")
            
        for j in range(n_star):
            print("*", end=" ")
            
        if(i <= n//2):
            n_space += 2
            n_star -= 1
        else:
            n_space -= 2
            n_star += 1
            
        print()
        
print_pattern_6(5)
            