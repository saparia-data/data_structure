'''
print below pattern

0    
1    1    
2    3    5    
8    13   21    34    
55   89   144   233    377    
        
'''

def print_pattern_12(n):
    
    a = 0
    b = 1
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(a, end="\t")
            c = a + b
            a = b 
            b = c
        print()
            
print_pattern_12(5)