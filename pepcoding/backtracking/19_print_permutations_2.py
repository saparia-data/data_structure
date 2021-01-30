'''
1. You are give a number of boxes (nboxes) and number of non-identical items (ritems).
2. You are required to place the items in those boxes and print all such configurations possible.


Sample Input:

5
3

Sample Output:

12300
12030
12003
13200
10230
10203
13020
10320
10023
13002
10302
10032
21300
21030
21003
31200
01230
01203
31020
01320
01023
31002
01302
01032
23100
20130
20103
32100
02130
02103
30120
03120
00123
30102
03102
00132
23010
20310
20013
32010
02310
02013
30210
03210
00213
30012
03012
00312
23001
20301
20031
32001
02301
02031
30201
03201
00231
30021
03021
00321


https://www.youtube.com/watch?v=NWFpebVkmTI&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=21


'''

def permutations(cb, tb, itemsUsed, ssf, ts, asf):
    
    if(cb > tb):
        print(asf)
        return
    
    for i in range(ts):
        
        if(itemsUsed[i] == 0):
            itemsUsed[i] = 1
            permutations(cb + 1, tb, itemsUsed, ssf + 1, ts, asf + str(i + 1))
            itemsUsed[i] = 0
            
    permutations(cb + 1, tb, itemsUsed, ssf, ts, asf + str(0))
    

if __name__ == "__main__":
    
    numberOfBoxes = 5
    numberOfItems = 3
    itemsUsed = [0] * numberOfItems
    permutations(1, numberOfBoxes, itemsUsed, 0, numberOfItems, "")