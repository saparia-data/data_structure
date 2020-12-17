'''
print below pattern

1    
1    1    
1    2    1    
1    3    3    1    
1    4    6    4    1    
        
'''

def print_pattern_13(n):
    
    for i in range(n):
        val = 1
        for j in range(i+1):
            print(val, end="\t")
            val = (val * (i-j)) // (j+1)
        print()
    
    
    
    
print_pattern_13(5)