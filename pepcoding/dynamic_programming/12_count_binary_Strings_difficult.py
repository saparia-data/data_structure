'''
1. You are given a number n.
2. You are required to print the number of binary strings of length n with no consecutive 0's.


Sample Input:

6

Sample Output:

21


https://www.youtube.com/watch?v=nqrXHJWMeBc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=18


'''

def countBinaryStrings(n):
    
    dpZeros = [0] * (n+1)
    dpOnes = [0] * (n+1)
    
    dpZeros[1] = 1
    dpOnes[1] = 1
    
    for i in range(2, n+1):
        dpOnes[i] = dpZeros[i - 1] + dpOnes[i - 1]
        dpZeros[i] = dpOnes[i - 1]
        
    return (dpZeros[n] + dpOnes[n]) 


def countBinaryStrings1(n):
    
    oldCountZero = 1
    oldCountOne = 1
    
    for i in range(2, n+1):
        
        newCountZero = oldCountOne
        newCountOne = oldCountOne + oldCountZero
        
        oldCountOne = newCountOne
        oldCountZero = newCountZero
        
    return (oldCountOne + oldCountZero)



if __name__ == "__main__":
    
    n = 6
    print(countBinaryStrings(n))
    print(countBinaryStrings1(n))