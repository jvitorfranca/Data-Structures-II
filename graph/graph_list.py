import sys
import heapq


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

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

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

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
        # self.__vert_dict[to].add_neighbor(self.__vert_dict[frm], cost)

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

    def dfs(self, start):
        stack, path = [start], []

        while stack:
            vertex = stack.pop()

            if vertex in path:
                continue
            path.append(vertex)

            x = self.get_vertex(vertex)

            for neighbor in x.get_adj():
                stack.append(neighbor.id)

        return path

    def dfs_time(self):
        color = {}
        pred = {}
        d = {}
        f = {}

        for vertex in self.__vert_dict:
            color[vertex] = 'WHITE'
            pred[vertex] = None

        time = 0

        for vertex in self.__vert_dict:
            if color[vertex] == 'WHITE':
                time, color = self.__dfs_visit(vertex, time, color, pred, d, f)

        return color, time

    def __dfs_visit(self, vertex, time, color, pred, d, f):

        time = time + 1
        color[vertex] = 'GRAY'
        d[vertex] = time

        x = self.get_vertex(vertex)

        for v in x.get_adj():
            if color[v.id] == 'WHITE':
                pred[v.id] = vertex
                self.__dfs_visit(v.id,  time, color, pred, d, f)

        color[vertex] = 'BLACK'
        time = time + 1
        f[vertex] = time

        # print(d[vertex], f[vertex])

        return time, color

    def minimal(self, unvisited_queue):

        max = sys.maxsize

        for v in unvisited_queue:
            if v.get_distance() < max:
                min_vertex = v

        return min_vertex

def shortest(v, path):
    # Make shortest path from v.previous
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start, target):
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v) for v in aGraph]

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        current = aGraph.minimal(unvisited_queue)
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            unvisited_queue.pop()
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v) for v in aGraph if not v.visited]

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

    print("DFS: ")
    print(g.dfs('a'))

    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' %(path[::-1]))
