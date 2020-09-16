'''
Linear probing is a collision handling technique in hashing. Linear probing says that whenever a collision occurs,
search for the immediate next position.

Given an array of integers and a hash table size. Fill the array elements into a hash table using Linear Probing to handle collisions.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input.
The first line contains size of the hashtable. The second line contains size of the array. The third line contains elements of the array.

Output:
For each testcase, in a new line, print the hash table.

Your Task:
You don't need to read input or print anything. Your task is to complete the function linearProbing() which takes as input a empty hash table (hash),
the hash table size (hashSize), an integers array arr[] and its size N and inserts all the elements of the array arr[] into the given hash table.
The empty cells of the hash table are to be given a value of -1. Also, if there's no more space to insert a new element, just drop that element. 

Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= hashSize <= 100
1 <= sizeOfArray <= 100
0 <= Array[] <= 105

Examples:
Input:
2
10
4
4 14  24 44
10
4
9 99 999 9999
Output:
-1 -1 -1 -1 4 14 24 44 -1 -1
99 999 9999 -1 -1 -1 -1 -1 -1 9

Explanation:

Testcase1: 4%10=4. So put 4 in hashtable[4]. Now, 14%10=4, 
but hashtable[4] is already filled so put 14 in the next slot and so on.

Testcase2: 9%10=9. So put 9 in hashtable[9]. Now, 99%10=9, but hashtable[9] is already filled 
so put 99 in the (99+1)%10 =0 slot so 99 goes into hashtable[0] and so on.

hints:

1)
In Linear Probing, we insert any value x in the hash table at the index x%hashSize.
If this index is already occupied by some other element, we simply search for the next free position in the hash table.

'''
def linearProbing(hashSize, arr, sizeOfArray):
    
    hash = [-1] * hashSize
    
    for i in range(sizeOfArray):
        
        if(hash[arr[i] % hashSize] == -1):
            hash[arr[i] % hashSize] = arr[i]
        
        #else linearly move from the filled position to find an empty place. 
        #Mod by hashSize ensures that we remain inside the hashTable
        else:
            k = (1 + arr[i]) % hashSize
            counter = 0
            
            while(counter < hashSize and hash[k] != -1):
                k = (1+k) % hashSize
                counter += 1
                
            if(counter < hashSize):
                hash[k] = arr[i]
                
    return hash
            
                
arr = [4,14,24,44]
sizeOfArray = len(arr)
hashSize = 10
print(linearProbing(hashSize, arr, sizeOfArray))