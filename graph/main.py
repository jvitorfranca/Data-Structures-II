import sys
import graph_list as graph


def main(argv):

    if len(argv) == 1:
        print("You insert at least a file")

    else:
        file_name = argv[1:].pop()

        with(open(file_name)) as f:
            lines = f.readlines()

            g = graph.Graph()

            for i in range(1, len(lines)):
                vertex1 = lines[i].rstrip("\n").split(" ").pop(0)
                vertex2 = lines[i].rstrip("\n").split(" ").pop(1)
                weight = lines[i].rstrip("\n").split(" ").pop(2)
                g.add_edge(int(vertex1), int(vertex2), int(weight))

        while True:

            option = int(input("\n1.BFS\n2.DFS\n3.Dijkstra\nPress other to exit\n"))

            if option == 1:

                vertex = int(input("Insert the vertex you want to start\n"))

                print("\nBFS: ")
                print(g.bfs(vertex))

            elif option == 2:

                vertex = int(input("Insert the vertex you want to start\n"))

                print("\nDFS: ")
                print(g.dfs(vertex))

            elif option == 3:

                frm = int(input("Insert the vertex you want to start\n"))
                to = int(input("Insert the vertex you want to get\n"))

                print("\nDijkstra: ")
                graph.dijkstra(g, g.get_vertex(frm), g.get_vertex(to))

                target = g.get_vertex(to)
                path = [target.get_id()]
                graph.shortest(target, path)
                print('The shortest path : %s' %(path[::-1]))

            else:
                break

if __name__ == "__main__":
    main(sys.argv)
