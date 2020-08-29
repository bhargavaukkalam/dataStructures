import collections
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.vertices=vertices
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        print(self.graph)
        
    def isCyclic(self,n,graph):
        '''
        visited=[False]*n
        for i in range(n):
            if not visited[i] and self.isCyclicConnected(n,graph,i,visited):
                return True
        return False
        '''
        visited=[False]*len(graph)
        for k,v in graph.items():
            if not visited[k] and self.isCyclicConnected(n,graph,k,visited):
                return True
        return False
    
    def isCyclicConnected(self,n,graph,node,visited):
        parent=[-1]*len(graph)
        queue=[]
        queue.append(node)
        visited[node]=True
        
        while queue:
            n=queue.pop(0)
            for v in graph[n]:
                print(parent)
                if not visited[v]:
                    visited[v]=True
                    queue.append(v)
                    parent[v]=n
                elif parent[n]!=v:
                    return True
        return False
                    
                    
        
if __name__=="__main__":
    g=Graph(4)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(2,0)
    g.printGraph()
    print(g.isCyclic(g.vertices,g.graph),)
    
