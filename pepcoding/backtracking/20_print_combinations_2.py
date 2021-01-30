'''
1. You are give a number of boxes (nboxes) and number of identical items (ritems).
2. You are required to place the items in those boxes and print all such configurations possible.

Items are identical and all of them are named 'i'

Note 1 -> Number of boxes is greater than number of items, hence some of the boxes may remain 
          empty.


Sample Input:

5
3

Sample Output:

iii--
ii-i-
ii--i
i-ii-
i-i-i
i--ii
-iii-
-ii-i
-i-ii
--iii


https://www.youtube.com/watch?v=f6cL-VMIfTY&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=22


'''

def combination(boxesOccupied, ci, ti, bl): # bl -> box level
    
    if(ci > ti):
        
        for item in boxOccupied:
            if(item == True):
                print("i", end="")
            else:
                print("-", end="")
        print()
        
        return
    
    
    b = bl + 1
    while(b < len(boxOccupied)):
        
        if(boxesOccupied[b] == False):
            boxesOccupied[b] = True
            combination(boxesOccupied, ci + 1, ti, b)
            boxesOccupied[b] = False
        
        b += 1



if __name__ == "__main__":
    
    numberOfBoxes = 5
    numberOfItems = 3
    boxOccupied = [False] * numberOfBoxes
    combination(boxOccupied, 1, numberOfItems, -1)