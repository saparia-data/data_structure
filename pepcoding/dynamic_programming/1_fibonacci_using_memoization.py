'''
1. You are given a number n.
2. You are required to print the nth element of fibonnaci sequence.

0th element -> 0
1st element -> 1
2nd element -> 1
3rd element -> 2
4th element -> 3
5th element -> 5
6th element -> 8


https://www.youtube.com/watch?v=94dfRrDANRY&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=1&t=4s


'''

def fiboMemoized(n, qb):
    
    if(n == 0 or n == 1):
        return n
    
    if(qb[n] != 0):
        return qb[n]
    
    fibonm1 = fiboMemoized(n - 1, qb)
    fibonm2 = fiboMemoized(n - 2, qb)
    fibon = fibonm1 + fibonm2
    qb[n] = fibon
    return fibon


def Fibo(n, qb):
    
    qb[0] = 0
    qb[1] = 1
    
    for i in range(2, n+1):
        qb[i] = qb[i-1] + qb[i-2]
        
    return qb[n]


if __name__ == "__main__":
    
    n = 10
    qb = [0] * (n + 1)
    print(fiboMemoized(n, qb))
    print(Fibo(n, qb))