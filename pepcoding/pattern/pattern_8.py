'''
print below pattern

                *    
            *        
        *            
    *                
*

'''

def print_pattern_8(n):

    for i in range(1, n+1):
        
        for j in range(1, n+1):
            if(i+j == n+1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
                
        print()
        
print_pattern_8(5)