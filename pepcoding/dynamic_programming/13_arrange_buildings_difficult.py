'''
1. You are given a number n, which represents the length of a road. The road has n plots on it's each side.
2. The road is to be so planned that there should not be consecutive buildings on either side of the road.
3. You are required to find and print the number of ways in which the buildings can be built on both side of roads.

Sample Input:

6

Sample Output:

441


https://www.youtube.com/watch?v=0nF-BMYy7tc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=19


'''

def countBinaryStrings(n):
    
    oldBuilding = 1
    oldSpace = 1
    
    for i in range(2, n+1):
        
        newBuilding = oldSpace
        newSpace = oldBuilding + oldSpace
        
        oldBuilding = newBuilding
        oldSpace = newSpace
        
    total = oldBuilding + oldSpace
    
    return (total * total)




if __name__ == "__main__":
    
    n = 6
    print(countBinaryStrings(n))