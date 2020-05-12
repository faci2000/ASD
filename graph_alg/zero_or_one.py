import queue

def path_cost( Graph, start, end ):
    zeros_que = queue.Queue()                                   # tworzę dwie osobne kolejki, dla wierzchołów, do których prowadzi
    ones_que=queue.Queue()                                      # krawedź o wart 1 lub 0
    ones_cost_que=queue.Queue()
    Cost=[-1 for i in range(len(Graph))]
    Cost[start]=0
    zeros_que.put(start)
    while (not zeros_que.empty()) or (not ones_que.empty()):    # za każdym razem staram się korzystać z kolejki 0, gdyż przechodzenie
        while not zeros_que.empty():                            # po wierzchołkach w niej zawartych nic mnie nie kosztuje
            x=zeros_que.get()                                       
            for i in range(len(Graph[x])):
                if Cost[Graph[x][i][0]]==-1:
                    if Graph[x][i][1]==0:
                        zeros_que.put(Graph[x][i][0])
                        Cost[Graph[x][i][0]]=Cost[x]
                        if Graph[x][i][0]==end:
                            return Cost[x]
                    else:                                       # jezeli trafie na jakas krawedz wart 1 odkladam ja do kolejki 
                        ones_que.put(Graph[x][i][0])            # jedynek, która w razie potrzeby uzyje pozniej
                        ones_cost_que.put(Cost[x]+1)
        else:
            x=ones_que.get()                                    # w sytuacji, gdy wierzchołki z kolejki zer mi się wyczerpia    
            cost=ones_cost_que.get()                            # biore jeden z wierzcholkow ktore odlozylem do kolejki jedynek
            if Cost[x]==-1:                                     # i jesli za pomoca zer jeszcze do niego nie dotarłem
                Cost[x]=cost                                    # zwiekszam koszt dotarcia do wierzcholka i rozpatruje jego krawedzie
                if x==end:                                      # wrzucając je do opowiednich kolejek
                    return Cost[x]
                for i in range(len(Graph[x])):
                    if Cost[Graph[x][i][0]]==-1:
                        if Graph[x][i][1]==0:
                            zeros_que.put(Graph[x][i][0])
                            Cost[Graph[x][i][0]]=Cost[x]
                            if Graph[x][i][0]==end:
                                return Cost[x]
                        else:
                            ones_que.put(Graph[x][i][0])       # cały proces powatarza sie dopóki nie dotre do wierzchołka końcowego
                            ones_cost_que.put(Cost[x]+1)       # A jeśli  dotrę, to bedzie to możliwie "najtańsza" ścieżka

    return "Wierzchołek "+str(end)+" nie jest mozliwy do osiagniecia"


# G = [[(1,0)],
# [(2,1), (4,1)],
# [(5,1), (3,0)],
# [(7,1), (6,1), (4,0)],
# [(7,0)],
# [(6,0)],
# [(8,1)],
# [(6,1), (5,0)],
# []]  
#dla 0 i 8 wynik to 2
G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]

print( path_cost( G, 0, 3 ) ) # wypisze 0
