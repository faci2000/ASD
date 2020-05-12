# idea rozwiązania:
#   dla każdego przedziału u znaleźć optymalnego następnika v i stworzyć krawędź skierowaną (v, u)
#   (jeżeli optymalny następnik nie istnieje, to pomijamy)
#   następnie pełzając dfsem po stworzonym drzewie należy minimalizować
#   zmienną przechowującą długość ścieżki o k wierzchołkach


def dfs(i, k, stack, predecessors, invervals):
    # w stosie przechowywane są indeksy poprzednich wierzchołków (przedziałów) w ścieżce

    m = float("inf")
    stack.append(i)

    if len(stack) >= k:
        # jeżeli ścieżka jest długości przynajmniej k, to sprawdzamy czy
        # stworzona z k ostatnich przedziałów nie jest aktualnie najkrótsza
        m = min(m, intervals[stack[-k]][1] - intervals[i][0])

    for p in predecessors[i]:
        m = min(m, dfs(p, k, stack, predecessors, intervals))

    stack.pop()
    return m


intervals = [(0, 10), (3, 10), (7, 9), (3, 4), (1, 2), (0, 5), (6, 8), (8, 9)]
k = 2

if k == 1:
    print(min([interval[1] - interval[0] for interval in intervals]))
    exit(0)

n = len(intervals)

# sortujemy po końcach przedziałów
intervals.sort(key=lambda interval: interval[1])

root = 0  # indeks korzenia drzewa
predecessors = [[] for _ in range(n)]
i, j = 0, 0
while i < n and j < n:
    if i == j or intervals[j][0] < intervals[i][1]:
        # warunek 1:
        #   przedział nie może być następnikiem samego siebie
        #   można z tego warunku zrezygnować jeżeli przedziały mają długość > 0
        # warunek 2:
        #   j-ty zaczyna się wcześniej niż i-ty się kończy (zazębienie)
        j += 1
        continue

    # w tym momencie mamy pewność, że j-ty zaczyna się nie wcześniej niż i-ty się kończy
    root = j
    predecessors[j].append(i)
    i += 1

# każdy wierzchołek ma jednego następnika, ale może mieć więcej niż jednego poprzednika
# zatem stworzone drzewo może mieć rozwidlenia jedynie idąc od prawej do lewej
# pojedyncze wierzchołki nas nie interesują, poza nimi drzewo jest spójne

m = float("inf")
if predecessors[root]:
    stack = []
    m = min(m, dfs(root, k, stack, predecessors, intervals))

if m == float("inf"):
    print("NIE")
else:
    print(m)
