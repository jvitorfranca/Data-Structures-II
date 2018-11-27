import sys
import graph_list as graph


def main(argv):

    if len(argv) == 1:
        print("You insert at least a file")

    else:
        file_name = argv[1:].pop()

        print("File name: ")
        print(file_name + "\n")

        with(open(file_name)) as f:
            lines = f.readlines()

            g = graph.Graph()

            for i in range(1, len(lines)):
                vertex1 = lines[i].rstrip("\n").split(" ").pop(0)
                vertex2 = lines[i].rstrip("\n").split(" ").pop(1)
                weight = lines[i].rstrip("\n").split(" ").pop(2)
                g.add_edge(int(vertex1), int(vertex2), int(weight))


        print("BFS: ")
        print(g.bfs(0))

        print("DFS: ")
        print(g.dfs(0))

        print("Dijkstra: ")
        graph.dijkstra(g, g.get_vertex(0), g.get_vertex(13))

        target = g.get_vertex(13)
        path = [target.get_id()]
        graph.shortest(target, path)
        print('The shortest path : %s' %(path[::-1]))

if __name__ == "__main__":
    main(sys.argv)
