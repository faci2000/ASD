import queue
def BFS( G, s):
    Dist = [(-1,-1) for i in range(len(G))]         #tworze tablice przwchowujaca rodzica i odleglosc
    Que = queue.Queue(len(G))                       #tworze kolejke przechowujaca kolejne wierzcholki
    # for i in range(len(G)):                       #Opcjonalnie dla kazdej silnie spojnie skladowej 
    #     if Dist[i][0]==-1:                        #mozna odpalac bfs'a
    Que.put(s)
    Dist[s]=(None,0)
    while not Que.empty():                           #wykonuje bfs'a pamietajac o aktualizujac 
        x=Que.get()                                  #rodzica i odleglosci
        for i in range(len(G)):
            if G[x][i]!=0:
                if Dist[i][1]==-1:
                    Dist[i]=(x,Dist[x][1]+1)
                    Que.put(i)
                else:
                    if Dist[i][1]>(Dist[x][1]+1):
                        Dist[i]=(x,Dist[x][1]+1)
    return Dist
                
                         


# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )