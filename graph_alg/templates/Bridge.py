def dfs_bridges(Graph,Low,Ord,x,order):
    for i in range(len(Graph[x])):
        for j in range(len(Graph[Graph[x][i][0]][0])):
            if Graph[Graph[x][i][0]][j][0]==x:
                Graph[Graph[x][i][0]][j]=(Graph[Graph[x][i][0]][j][0],False)
                Graph[x][i]=(Graph[x][i][1],False)

        if Low[Graph[x][i][0]]==-1:
            Low[Graph[x][i][0]]=order
            Ord[Graph[x][i][0]]=order
            order+=1
            dfs_bridges(Graph,Low,Ord,Graph[x][i][0],order)
        if Low[x]==-1:
            Low[x]=Low[Graph[x][i][0]]
        else:
            Low[x]=min(Low[Graph[x][i][0]],Low[x])



def bridges(Graph):
    Low=[-1 for i in range(len(Graph))]
    Ord=[0 for i in range(len(Graph))]
    order=0
    dfs_bridges(Graph,Low,Ord,0,order)
    return Low,Ord


Graph=[ [(4,True),(2,True)],
        [(6,True),(5,True),(2,True)],
        [(0,True),(4,True),(1,True)],
        [(5,True)],
        [(0,True),(2,True)],
        [(7,True),(3,True),(1,True)],
        [(7,True),(1,True)],
        [(5,True),(6,True)]]
print(bridges(Graph))
    