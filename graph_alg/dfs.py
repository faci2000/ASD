def true_dfs(Graph,Parent,x):               #rekrencyjna funkcja dfs przechodzaca
    for i in range(len(Graph[x])):          #po kolejnych wierzcholkach w glab
        if Parent[Graph[x][i]]==-1:
            Parent[Graph[x][i]]=x
            true_dfs(Graph,Parent,Graph[x][i])


def DFS( G ):
    Parent = [-1 for i in range(len(G))]
    for i in range(len(G)):                 #dla kazdego nieoodwiedzonego wierzcholka
        if Parent[i]==-1:                   #w tym tez dla kazdej spojnie skladowej
            Parent[i]=None                  #wywoluje rekurencyjnego dfsa
            true_dfs(G,Parent,i)
    return Parent


# elementarny test. Może wypisać np.
# [None, 0, 1, 2]
G = [[1,2],[0,2,3],[3,1,0],[2,1]]
print( DFS(G) )
