'''
Given a Directed Graph. Count the total number of ways or paths that exist between two vertices in the directed graph. 
These paths doesn't contain any cycle.

https://www.geeksforgeeks.org/count-possible-paths-two-vertices/

'''
class Graph: 
  
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)] 
      
    def addEdge(self, u, v): 
          
        # Add v to u's list.  
        self.adj[u].append(v) 
      
    # Returns count of paths from 's' to 'd'  
    def countPaths(self, s, d): 
          
        # Mark all the vertices  
        # as not visited  
        visited = [False] * self.V 
      
        # Call the recursive helper  
        # function to print all paths  
        pathCount = [0]  
        self.countPathsUtil(s, d, visited, pathCount)  
        return pathCount[0] 
      
    # A recursive function to print all paths  
    # from 'u' to 'd'. visited[] keeps track   
    # of vertices in current path. path[]  
    # stores actual vertices and path_index  
    # is current index in path[]  
    def countPathsUtil(self, u, d,  
                       visited, pathCount): 
        #print(u,d)
        visited[u] = True
      
        # If current vertex is same as  
        # destination, then increment count  
        if (u == d): 
            pathCount[0] += 1
      
        # If current vertex is not destination  
        else: 
              
            # Recur for all the vertices  
            # adjacent to current vertex 
            i = 0
            while i < len(self.adj[u]): 
                if (not visited[self.adj[u][i]]):  
                    self.countPathsUtil(self.adj[u][i], d,  
                                        visited, pathCount) 
                i += 1
        #print(u)
        visited[u] = False
  
# Driver Code  
if __name__ == '__main__': 
  
    # Create a graph given in the  
    # above diagram  
    g = Graph(4)  
    g.addEdge(0, 1)  
    g.addEdge(0, 2)  
    g.addEdge(0, 3)  
    g.addEdge(2, 0)  
    g.addEdge(2, 1)  
    g.addEdge(1, 3)  
  
    s = 2
    d = 3
    print(g.adj)
    print(g.countPaths(s, d)) 