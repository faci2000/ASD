import queue
def count_shortest_paths( Graph, start, end ):
    Shortest_paths=[len(Graph)+1 for i in range(len(Graph)) ]
    Paths_counter=[0 for i in range(len(Graph)) ]
    Shortest_paths[start]=0
    Paths_counter[start]=1
    vert_que = queue.Queue()
    vert_que.put(start)
    while not vert_que.empty():                                             #Korzystając z bfs'a mamy pewność, że kolejno odwiedzane wierzchołki
        x=vert_que.get()                                                    #będą końcami kolejno najkrótszych scieżek dł. 1,2,3,... itd
        for i in range(len(Graph)):
            if Graph[x][i] and Shortest_paths[i]>Shortest_paths[x]+1:
                Shortest_paths[i]=Shortest_paths[x]+1                       #Gdy znajde nowa najkrótsza scieżke do wierzchołka, aktualizuje długosc 
                Paths_counter[i]=Paths_counter[x]                           #najdłuższej scieżki oraz liczbe jej scieżek
                vert_que.put(i)
            elif Graph[x][i] and Shortest_paths[i]==(Shortest_paths[x]+1):
                Paths_counter[i]+=Paths_counter[x]                          #Korzystam z faktu, iż jeżeli do wierzchołka k dochodzi n scieżek, do których 
    return Paths_counter[x]                                                 #najkrótsze scieżki są takie same, to łączna ilość scieżek będzie sumą ilości scieżek dla każdego z n


# G = [[False, True, False, False, False, False, False, False, False],
#     [False, False, True, False, True, False, False, False, False],
#     [False, False, False, True, False, True, False, False, False],
#     [False, False, False, False, True, False, True, True, False],
#     [False, False, False, False, False, False, False, True, False],
#     [False, False, False, False, False, False, True, False, False],
#     [False, False, False, False, False, False, False, False, True],
#     [False, False, False, False, False, True, True, False, False],
#     [False, False, False, False, False, False, False, False, False]]
#dla 0 i 8 powinien wypisać 3
G = [[False, True, True, False],
[False, False, True, True ],
[False, False, False, True ],
[False, False, False, False]]
print( count_shortest_paths( G, 0, 8 ) )