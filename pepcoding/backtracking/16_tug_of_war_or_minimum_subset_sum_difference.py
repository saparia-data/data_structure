'''
1. You are given an array of n integers.
2. You have to divide these n integers into 2 subsets such that the difference of sum of two subsets 
   is as minimum as possible.
3. If n is even, both set will contain exactly n/2 elements. If  is odd, one set will contain (n-1)/2 and 
   other set will contain (n+1)/2 elements.
4. If it is not possible to divide, then print "-1".


Sample Input:

6

1
2
3
4
5
6

Sample Output:

[1, 3, 6] [2, 4, 5]

https://www.youtube.com/watch?v=Q1fLW_zQr3M&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=18

'''
import sys

minDiff = sys.maxsize
ans = ""
def tugOfWar(arr, vidx, list1, list2, solist1, solist2): # solist1 -> sum of list1
    global minDiff
    global ans
    if(vidx == len(arr)):
        delta = abs(solist1 - solist2)
        if(delta < minDiff):
            minDiff = delta
            ans = str(list1) + " " + str(list2) 
        
    
    if(len(list1) < (len(arr) + 1) // 2): # to handle odd and even number of elements in arr
        list1.append(arr[vidx])
        tugOfWar(arr, vidx + 1, list1, list2, solist1 + arr[vidx], solist2)
        list1.pop()
    
    if(len(list2) < (len(arr) + 1) // 2):
        list2.append(arr[vidx])
        tugOfWar(arr, vidx + 1, list1, list2, solist1, solist2 + arr[vidx])
        list2.pop()
    
    
if __name__ == "__main__":
    
    arr = [1,2,3,4,5,6]
    list1 = []
    list2 = []
    
    tugOfWar(arr, 0, list1, list2, 0, 0)
    print(ans)