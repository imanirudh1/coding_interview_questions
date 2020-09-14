class Graph:
    def __init__(self,Nodes,isDirected=False):
        self.nodes=Nodes
        self.adj_list={}
        self.isDirected=isDirected
        for node in self.nodes:
            self.adj_list[node]=[]

    def print_adj_list(self):
        for node in self.nodes:
            print(node,' -> ',self.adj_list[node])

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        if not self.isDirected:        
            self.adj_list[v].append(u) 
    def degree(self,node):
        return len(self.adj_list[node])           

g=Graph(['A','B','C'])
g.add_edge('A','B')
g.add_edge('A','C')

print(g.degree('A'))