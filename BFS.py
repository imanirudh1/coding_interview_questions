from queue import Queue
adj_list={
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
}

visited={}
level={}
parent={}
bfs_travel_output=[]
queue=[]
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
s='A'
visited[s]=True
level[s]=0
queue.append(s)
while not len(queue)==0:
    u=queue.pop(0)
    bfs_travel_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.append(v)

print(bfs_travel_output)
print(parent)