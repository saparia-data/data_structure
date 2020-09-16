'''
Given the adjacency list of a bidirectional graph. Your task is to print the adjacency list for each vertex.

https://www.youtube.com/watch?v=bs2er-CleeI

'''

# function to add an edge to graph 
def addEdge(self,u,v): 
    self.graph[u].append(v) 

def printGraph(g,v):
    '''
    :param g: given adjacency list of graph as defined in graph class.
    :param v: no of vertices in graph
    :return: print the adjacency list as shown.
    '''
    for i in range(v):
        edge_list = g[i]  # list containing nodes with this vertice.
        print(i, end=" ")
        if(len(edge_list)!=0):
            print("->", end=" ")
        else:
            print()
            continue

        # traverse the edges connected to this vertices
        for j in range(len(edge_list) - 1):
            print(edge_list[j], end=" ")
            print("->", end=" ")

        # print the last node in
        if (len(edge_list)):
            print(edge_list[-1])
            
v = 5
g = [[1,4],[0,4,2,3],[1,3],[1,4,2],[3,0,1]]
printGraph(g, v)