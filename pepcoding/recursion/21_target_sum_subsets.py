'''
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number "tar".
4. calculate and print all subsets of given elements, the contents of which sum to "tar". Use sample input and output to get more idea.


Sample Input:

5
10
20
30
40
50

60

Sample Output:

10, 20, 30, .
10, 50, .
20, 40, .


https://www.youtube.com/watch?v=HGDmj5NrrjM&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=49


'''

def printTargetSumSubset(arr, idx, res_set, sos, target):
    
    if(idx == len(arr)):
        if(sos == target):
            print(res_set)
        
        return
    
    printTargetSumSubset(arr, idx+1, res_set + str(arr[idx])+",", sos+arr[idx], target)
    printTargetSumSubset(arr, idx+1, res_set, sos, target)
    
arr = [10,20,30,40,50]
target = 70
printTargetSumSubset(arr, 0, "", 0, target)