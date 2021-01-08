'''
1. You are given a 10*10 2-D array(arr) containing only '+' and '-' characters, which represents a 
   crossword puzzle. 
2. You are also given n number of words which need to be filled into the crossword.
3. Cells containing '-' are to be filled with the given words.

Sample Input:

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++

4

LONDON
DELHI 
ICELAND 
ANKARA

Sample Output:

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++


https://www.youtube.com/watch?v=fUAZS-sdP2Q&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=8

'''

def crossWordPuzzle(arr, words, vidx):
    '''
    arr: 2D array containing + and -
    words: 1D array containing words
    vidx: index of word in words array
    '''
    
    if(vidx == len(words)):
        displayArray(arr)
        return
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            word = words[vidx]
            if(arr[i][j] == '-' or arr[i][j] == word[0]): # if cell have - or cell have first char of word
                if(canFillHorizontally(arr, word, i, j) == True): # check if we can place word horizontally
                    wePlaced = placeHorizontally(arr, word, i, j)
                    crossWordPuzzle(arr, words, vidx+1)
                    unPlaceHorizontally(arr, wePlaced, i, j) # un-place words horizontally to check for other possibilities
                    
                if(canFillVertically(arr, word, i, j) == True): # check if we can place word vertically
                    wePlaced = placeVertically(arr, word, i, j)
                    crossWordPuzzle(arr, words, vidx+1)
                    unPlaceVertically(arr, wePlaced, i, j) # un-place words vertically to check for other possibilities
                    
def canFillHorizontally(arr, word, i, j):
    
    if(j-1 >= 0 and arr[i][j-1] != '+'): # check if anything/nothing in left side and if there then check it is + or not
        return False
    elif(j+len(word) < len(arr[0]) and arr[i][j+len(word)] != '+'): # check if + is there in right side or at the end
        return False
    
    for jj in range(len(word)):
        
        if(j + jj >= len(arr[0])): # if placing word is moving out of array in right side
            return False
        
        if(arr[i][j + jj] == '-' or arr[i][j + jj] == word[jj]):
            continue
        else:
            return False
        
    return True

def canFillVertically(arr, word, i, j):
    
    if(i-1 >= 0 and arr[i-1][j] != '+'): # check if anything/nothing in up side and if there then check it is + or not
        return False
    elif(i + len(word) < len(arr) and arr[i + len(word)][j] != '+'): # check if + is there in down side or at the end
        return False
    
    for ii in range(len(word)):
        
        if(i + ii >= len(arr)): # if placing word is moving out of array in down side
            return False
        
        if(arr[i + ii][j] == '-' or arr[i + ii][j] == word[ii]):
            continue
        else:
            return False
        
    return True
                

def placeHorizontally(arr, word, i, j):
    
    wePlaced = [False] * len(word) # boolean array to keep track which word placed so while backtracking we will remove only those placed words
    
    for jj in range(len(word)):
        
        if(arr[i][j + jj] == '-'):
            arr[i][j + jj] = word[jj]
            wePlaced[jj] = True
            
    return wePlaced


def unPlaceHorizontally(arr, wePlaced, i, j):
    
    for jj in range(len(wePlaced)):
        if(wePlaced[jj] == True):
            arr[i][j + jj] = '-'
            

def placeVertically(arr, word, i, j):
    
    wePlaced = [False] * len(word) # boolean array to keep track which word placed so while backtracking we will remove only those placed words
    
    for ii in range(len(word)):
        
        if(arr[i + ii][j] == '-'):
            arr[i + ii][j] = word[ii]
            wePlaced[ii] = True
            
    return wePlaced


def unPlaceVertically(arr, wePlaced, i, j):
    
    for ii in range(len(wePlaced)):
        if(wePlaced[ii] == True):
            arr[i + ii][j] = '-'

def displayArray(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end = " ")
        print()

if __name__ == "__main__":
    arr = [
            ['+','-','+','+','+','+','+','+','+','+'],
            ['+','-','+','+','+','+','+','+','+','+'],
            ['+','-','+','+','+','+','+','+','+','+'],
            ['+','-','-','-','-','-','+','+','+','+'],
            ['+','-','+','+','+','-','+','+','+','+'],
            ['+','-','+','+','+','-','+','+','+','+'],
            ['+','+','+','+','+','-','+','+','+','+'],
            ['+','+','-','-','-','-','-','-','+','+'],
            ['+','+','+','+','+','-','+','+','+','+'],
            ['+','+','+','+','+','-','+','+','+','+']
        ]
    
    words = ['LONDON', 'DELHI','ICELAND','ANKARA']
    crossWordPuzzle(arr, words, 0)