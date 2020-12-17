'''
print below pattern

1    
2    3    
4    5    6    
7    8    9    10    
11   12   13   14    15
        
'''

def print_pattern_11(n):
    
    val = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(val, end= "\t")
            val += 1
        print()
            
print_pattern_11(5)