'''
Given an undirected graph and an integer M. 
The task is to determine if the graph can be colored with at most M colors 
such that no two adjacent vertices of the graph are colored with the same color. 
Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Example 1:
Input:
N = 4
M = 3
E = 5
Edges[] = {(1,2),(2,3),(3,4),(4,1),(1,3)}
Output: 1
Explanation: It is possible to colour the
given graph using 3 colours.

https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

https://www.youtube.com/watch?v=miCYGGrTwFU

'''
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
  
    # A utility function to check if the current color assignment 
    # is safe for vertex v 
    def isSafe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # A recursive utility function to solve m 
    # coloring  problem 
    def graphColourUtil(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m + 1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v + 1) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == None: 
            return False
  
        # Print the solution 
        print("Solution exist and Following are the assigned colours:")
        for c in colour: 
            print(c) 
        return True
  
# Driver Code 
g = Graph(4) 
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]] 
m = 3
g.graphColouring(m)