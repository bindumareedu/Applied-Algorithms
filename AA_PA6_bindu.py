# checking if graph is Bipartite or not
def isBipartite(graph, src):
    color = {}
    explored = {}
    for vertex in graph.keys():
        color[vertex] = "white"
        explored[vertex] = False
    color[root] = "green"
    queue = [root]
    while len(queue) > 0:
        u = queue.pop()
        for x in graph[u]:
            if u in x:
                return False
        if not explored[u]:
            explored[u] = True
            for x in graph[u]:
                queue.insert(0, x)
                if color[u] != 'white' and color[u] == color[x]:
                    return False
                if color[x] == 'white':
                    if color[u] == 'red':
                        color[x] = 'green'
                    else:
                        color[x] = 'red'
    green = []
    red = []
    for x in color:
        if color[x] == "green":
            green.append(x)
        else:
            red.append(x)
    print "Green", green
    print "Red", red
    return True


# making graph(Adjacency List) based on input file
def make_graph(file):
    graph = {}
    root = 0
    with open(file, "r") as f:
        for line in f:
            if len(line) > 2:
                if len(graph) == 2:
                    root = graph.keys()[0]
                if line[1] not in graph:
                    graph[line[1]] = [line[3]]
                else:
                    graph[line[1]].append(line[3])
                if line[3] not in graph:
                    graph[line[3]] = [line[1]]
                else:
                    graph[line[3]].append(line[1])
    return graph, root


file = "bipartite.txt"
graph, root = make_graph(file)

result = str(isBipartite(graph, root))


if result == "True":
    value = "YES"
else:
    value = "NO"

print "Is Bipartite ? " + value
