'''
print below pattern

                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *


'''

def print_pattern_3(n):
    
    n_star = 1
    n_space = n-1
    
    for i in range(n):
        
        for j in range(n_space):
            print(" ", end="\t")
            
        for j in range(n_star):
            print("*", end="\t")
            
        n_star += 1
        n_space -= 1
        print()
        
print_pattern_3(5)
        
        
        
        