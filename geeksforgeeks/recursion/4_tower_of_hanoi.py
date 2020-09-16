'''
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. 
You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement 
so that all the discs reach the 3rd rod. Also, you need to find the total moves.
Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. 
Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. 

Input Format:
The first line of input is T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing N.

Output Format:
For each testcase, print the steps and the total steps taken. Please see the example output to see the steps format.

Your Task:
This is a function problem. You only need to complete the function to that takes following parameters:

N: number of discs
from: The rod number from which we move the disc
to: The rod number to which we move the disc
aux: The rod that is used as an auxillary rod
moves: reference to the moves variable to store total moves
The driver code prints the total moves.

Constraints:
1 <= T <= 16
1 <= N <= 16

Example:
Input:
2
2
3
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
move disk 1 from rod 1 to rod 3
move disk 2 from rod 1 to rod 2
move disk 1 from rod 3 to rod 2
move disk 3 from rod 1 to rod 3
move disk 1 from rod 2 to rod 1
move disk 2 from rod 2 to rod 3
move disk 1 from rod 1 to rod 3
7

Hints:

1) Write a recursive function with 4 parameters: n, from, to, aux, moves

class Hanoi:
    moves = 0  # stores count of moves. You need to update the count in this variable
    def toh(self, N, fromm, to, aux):

'''
class Hanoi:
    moves = 0  # stores count of moves. You need to update the count in this variable
    def toh(self, N, fromm, to, aux):
        if(N == 1):
            print("move " + str(N) + " from " + fromm + " to " + to)
            Hanoi.moves += 1
            return
    
        self.toh(N - 1, fromm, aux, to)
        Hanoi.moves += 1
        print("move " + str(N) + " from " + fromm + " to " + to)
        self.toh(N - 1, aux, to, fromm)

def main():
    h = Hanoi()
    h.toh(4, "A", "AX", "C")
    print(h.moves)
    
if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        



