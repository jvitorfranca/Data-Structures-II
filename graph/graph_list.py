class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_adj(self):
        return self.adjacent

class Graph:
    def __init__(self):
        self.__vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.__vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.__vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.__vert_dict:
            return self.__vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.__vert_dict:
            self.add_vertex(frm)
        if to not in self.__vert_dict:
            self.add_vertex(to)

        self.__vert_dict[frm].add_neighbor(self.__vert_dict[to], cost)
        self.__vert_dict[to].add_neighbor(self.__vert_dict[frm], cost)

    def get_vertices(self):
        return self.__vert_dict.keys()

    def bfs(self, start):
        color = {}
        pred = {}
        dist = {}

        for vertex in self.__vert_dict:
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
            x = self.get_vertex(vertex)
            for i in x.get_adj():
                if color[i.id] == 'WHITE':
                    color[i.id] = 'GRAY'
                    dist[i.id] = dist[vertex] + 1
                    pred[i.id] = vertex
                    queue.append(i.id)
            color[vertex] = 'BLACK'

        return dist

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    print("BFS: ")
    print(g.bfs('a'))

    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
    #
    # for v in g:
    #     print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
