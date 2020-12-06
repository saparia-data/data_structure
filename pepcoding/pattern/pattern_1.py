'''
print below pattern

*    
*    *    
*    *    *    
*    *    *    *    
*    *    *    *    *

'''

def print_pattern_1(n):
    
    for i in range(n+1):
        for j in range(i):
            print("*", end="\t")
        print()
        
print_pattern_1(5)