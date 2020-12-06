'''
print below pattern 

*    *    *    *    *    
*    *    *    *    
*    *    *    
*


'''

def print_pattern_2(n):
    
    for i in range(n, -1, -1):
        for j in range(i, -1, -1):
            print("*", end="\t")
        print()

print_pattern_2(5)            