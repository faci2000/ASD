import queue

def max_flow(Graph, start, end ):
    change = True
    max_flow=0
    #
    # wykonuje algorytm dopóki znajduje ścieżki 
    # do ujśćia z niezerowymi przepływami
    while change:
        change=False
        Parent = [-1 for i in range(len(Graph))]
        Parent[start]=-2
        BFS_queue = queue.Queue()
        BFS_queue.put(start)
        min_path_flow=0
        #
        # wyszukuje ścieżki z niezerowymi przepływami
        #
        while(not BFS_queue.empty() and not change):
            vert = BFS_queue.get()
            for i in range(len(Graph)):
                if Graph[vert][i]>0 and Parent[i]==-1:
                    Parent[i]=vert 
                    if i==end:
                        change=True
                        break
                    BFS_queue.put(i)
        #
        # znajduje namniejszy przepływ na scieżce
        #
        min_path_flow=2**30
        if change:
            i=end
            while i!=start:
                if min_path_flow>Graph[Parent[i]][i]:
                    min_path_flow=Graph[Parent[i]][i]
                i=Parent[i]
        #
        # zmniejszam przepływ i zwiekszam przepływ przeciwny
        #
            i=end
            while i!=start:
                Graph[Parent[i]][i]-=min_path_flow
                Graph[i][Parent[i]]+=min_path_flow
                i=Parent[i]
            max_flow+=min_path_flow
    return max_flow
    


                    





c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( max_flow( c, 0, 3 ) ) # wypisze 3