'''
1. You are give a number of boxes (nboxes) and number of identical items (ritems).
2. You are required to place the items in those boxes and print all such configurations possible.

Items are identical and all of them are named 'i'.

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


https://www.youtube.com/watch?v=wOaxJAtJ2Mo&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=20


'''

def combination(currentBox, totalBoxes, ssf, totalSelection, asf): # ssf -> selection so far
    
    if(currentBox > totalBoxes):
        
        if(ssf == totalSelection):
            print(asf)
        
        return
    
    
    combination(currentBox + 1, totalBoxes, ssf + 1, totalSelection, asf + "i")
    combination(currentBox + 1, totalBoxes, ssf, totalSelection, asf + "-")


if __name__ == "__main__":
    
    numberOfBoxes = 5
    numberOfItems = 3
    combination(1, numberOfBoxes, 0, numberOfItems, "")