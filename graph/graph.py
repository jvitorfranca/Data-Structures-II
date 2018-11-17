class Graph:
    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):

        edges = []

        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})

        return edges

    def bfs(self, start):
        color = {}
        pred = {}
        dist = {}

        for vertex in self.__graph_dict:
            color[vertex] = 'WHITE'
            dist[vertex] = 100000
            pred[vertex] = None

        color[start] = 'GRAY'
        dist[start] = 0
        pred[start] = None

        queue = [start]

        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for i in self.__graph_dict[vertex]:
                if color[i] == 'WHITE':
                    color[i] = 'GRAY'
                    dist[i] = dist[vertex] + 1
                    pred[i] = vertex
                    queue.append(i)
            color[vertex] = 'BLACK'

        return dist


    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "

        return res

if __name__ == "__main__":

    # g = { "a" : ["d"],
    #   "b" : ["c"],
    #   "c" : ["b", "c", "d", "e"],
    #   "d" : ["a", "c"],
    #   "e" : ["c"],
    #   "f" : []
    # }

    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'E')

    print('BFS:')
    print(graph.bfs('A'))
