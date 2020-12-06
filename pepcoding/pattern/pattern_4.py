'''
print below pattern.

*    *    *    *    *    
     *    *    *    *    
          *    *    *    
               *    *    
                    *

'''

def print_pattern_4(n):
    
    n_star = n
    n_space = 0
    
    for i in range(n):
        
        for j in range(n_space):
            print(" ", end="\t")
        
        for j in range(n_star):
            print("*", end="\t")
            
        
            
        n_star -= 1
        n_space += 1
        print()
        
print_pattern_4(5)