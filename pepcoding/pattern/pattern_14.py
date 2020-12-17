'''
print below pattern

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30    
        
'''

def print_pattern_14(n):
    
    for i in range(1, 11):
        pattern = str(n) + " * " + str(i) + " = " + str(n * i)
        print(pattern)
    
print_pattern_14(3)