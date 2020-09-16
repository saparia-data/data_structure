'''
https://www.geeksforgeeks.org/previous-greater-element/

'''
def prevGreater(arr, n):
    
    s = list()
    s.append(arr[0])
    output = []
    
    output.append(-1)
    
    for i in range(1, n):
        
        while(len(s) > 0 and s[-1] < arr[i]):
            s.pop()
            
        if(len(s) == 0):
            output.append(-1)
        else:
            output.append(s[-1])
            
        s.append(arr[i])
        
    return output
        
arr = [ 10, 4, 2, 20, 40, 12, 30 ] 
n = len(arr) 
print(prevGreater(arr, n))
    