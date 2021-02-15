'''
1. You are given a number n, representing the count of elements.
2. You are given n numbers, representing n elements.
3. You are required to find the maximum sum of a subsequence with no adjacent elements.


Sample Input:

6

5
10
10
100
5
6

Sample Output:

116



https://www.youtube.com/watch?v=VT4bZV24QNo&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=22


'''

def maxSumNonAdj(arr, n):
    
    include = arr[0]
    exclude = 0
    
    for i in range(1, n):
        
        new_include = exclude + arr[i]
        new_exclude = max(include, exclude)
        
        include = new_include
        exclude = new_exclude
        
    ans = max(include, exclude)
    return ans


if __name__ == "__main__":
    
    arr = [5, 10, 10, 100, 5, 6]
    n = len(arr)
    
    print(maxSumNonAdj(arr, n))