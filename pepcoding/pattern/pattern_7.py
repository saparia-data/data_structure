'''
print below pattern

*    
    *    
        *    
            *    
                *

'''

def print_pattern_7(n):

    for i in range(1, n+1):
        
        for j in range(1, i+1):
            if(j == i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
                
        print()
        
print_pattern_7(5)
        
        
        
        