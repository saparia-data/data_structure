'''
Shortest Path in Directed Acyclic Graph

https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/

'''
from collections import defaultdict

class Graph: 
    def __init__(self,vertices): 
  
        self.V = vertices # No. of vertices 
  
        # dictionary containing adjacency List 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph[u].append((v,w)) 
    
    # function to get topological sort    
    def topologicalSortUtil(self,v,visited,stack):
        
        visited[v] = True
        
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if(visited[node] == False):
                    self.topologicalSortUtil(node, visited, stack)
                    
        stack.append(v)
        
    
        
    def shortestPath(self, s): 
        
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if(visited[i] == False):
                self.topologicalSortUtil(s, visited, stack)
                
        # Initialize distances to all vertices as infinite and 
        # distance to source as 0 
        dist = [float("Inf")] * (self.V) 
        dist[s] = 0
        print(stack)
        while stack: 
  
            # Get the next vertex from topological order 
            i = stack.pop()
            #print(i) 
  
            # Update distances of all adjacent vertices 
            for node,weight in self.graph[i]: 
                if dist[node] > dist[i] + weight: 
                    dist[node] = dist[i] + weight 
  
        # Print the calculated shortest distances 
        for i in range(self.V): 
            print("%d" % dist[i]) if dist[i] != float("Inf") else  "Inf" ,
            
g = Graph(6) 
g.addEdge(0, 1, 5) 
g.addEdge(0, 2, 3) 
g.addEdge(1, 3, 6) 
g.addEdge(1, 2, 2) 
g.addEdge(2, 4, 4) 
g.addEdge(2, 5, 2) 
g.addEdge(2, 3, 7) 
g.addEdge(3, 4, -1) 
g.addEdge(4, 5, -2) 
  
# source = 1 
s = 1
  
print ("Following are shortest distances from source %d " % s) 
g.shortestPath(s) 