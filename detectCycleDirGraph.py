import collections
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.vertices=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def printGraph(self):
        print(self.graph)
        
    def isCyclic(self,n,graph):
        #keep count of vertices which have incoming node pointers
        #in degree 0 means this is not a child node of any node
        in_degree=[0]*n
        '''
        for i in range(n):
            for j in graph[i]:
                in_degree[j]+=1
        '''
        for key,value in graph.items():
            for v in value:
                in_degree[v]+=1
                
        
        print(in_degree)
        
        queue=[]
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                queue.append(i)
        
        count=0
        #print(in_degree)
        while queue:
            nodes=queue.pop(0)
            for v in graph[nodes]:
                in_degree[v]-=1
                if in_degree[v]==0:
                    queue.append(v)
                
            count+=1
        
        if count==n:
            return False
        else:
            return True
        
        
        

if __name__=="__main__":
    g=Graph(4)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2) 
    #g.addEdge(2,0) 
    g.addEdge(2,3) 
    #g.addEdge(3,3)
    g.printGraph()
    print(g.isCyclic(g.vertices,g.graph))
