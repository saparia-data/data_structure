d = {}

def findDuplicates(arr):
    for i in arr:
        try:
            d[i] += 1
        except:
            d[i] = 1
    l = []
    for items in d:
        if(d[items] > 1):
            l.append(items)
            
    return l

arr = [1,1,2,3,4,4,4,5]
print(findDuplicates(arr))
    
            