'''
Quadratic probing is a collision handling technique in hashing. 
Quadratic probing says that whenever a collision occurs, search for i2 position.

Given an array of integers and a Hash table. 
Fill the elements of the array into the hash table by using Quadratic Probing in case of collisions.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input. 
The first line contains size of the hashtable. The second line contains size of the array. The third line contains elements of the array.

Output:
For each testcase, in a new line, print the hash table.

Your Task:
You don't need to read input or print anything. Your task is to complete the function QuadraticProbing() which takes the hash table hash[],
the hash table size hashSize, an array arr[] and the size of the array N as inputs and inserts all the elements of the array arr[] into the hash table 
using Quadratic Probing as a collision handling technique.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
2 <= hashSize (prime) <= 97
1 <= N < hashSize*0.5
0 <= Array[] <= 105

Examples:
Input:
2
11
4
21 10 32 43
11
4
880 995 647 172 
Output:
10 -1 -1 32 -1 -1 -1 -1 43 -1 21
880 -1 -1 -1 -1 995 -1 172 -1 647 -1 

Explanation:
Testcase1: 21%11=10 so 21 goes into hashTable[10] position. 10%11=10. hashTable[10] is already filled so we try for (10+12)%11=0 position.
hashTable[0] is empty so we put 10 there. 32%11=10. hashTable[10] is filled. We try (32+12)%11=0. 
But hashTable[0] is also already filled. We try (32+22)%11=3. hashTable[3] is empty so we put 32 in hashTable[3] position. 43 uses (43+33)%11=8. 
We put it in hashTable[8].

Testcase2: Using the similar approach as used in above explanation we will get the output like 880 -1 -1 -1 -1 995 -1 172 -1 647 -1.

Note:
All the positions that are unoccupied are denoted by -1 in the hash table.
An empty slot can only be found if load factor < 0.5 and hash table size is a prime number.
The given testcases satisfy the above condition so you can assume that an empty slot is always reachable.

hints:
1)
In Quadratic Probing, we insert any value x in the hash table at the index x%hashSize (let this index be ind).
If this index is already occupied by some other element, we simply check the slot (ind + 1*1)%hashSize. 
If even this is already filled, we move to the slot (ind + 2*2)%hashSize and so on till we find an empty slot. 

'''
def QuadraticProbing(hash, hashSize, arr, sizeOfArray):
    
    for i in range(sizeOfArray):
        if(hash[arr[i] % hashSize] == -1):
            hash[arr[i] % hashSize] = arr[i]
        
        #Else we quadratically traverse the array to find the empty position    
        else:
            k = arr[i] % hashSize
            power = 1
            while(hash[(k + power*power) % hashSize] != -1):
                power += 1
                
            hash[(k + power*power) % hashSize] = arr[i]
            
    return hash

arr = [21,10,32,43]
sizeOfArray = len(arr)
hashSize = 11
hash = [-1] * hashSize
print(QuadraticProbing(hash, hashSize, arr, sizeOfArray))