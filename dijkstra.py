


def dijkstra(graph, root, dest, visited=[], distances={}, predecessors={}):
    
    if root == dest:
        path = []
        pred = dest

        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)

        print("path:", path)

    else:
        if not visisted:
            distances[root] = 0

        for n in graph[root]:
            if n not in visited:
                new_d = distances[root] + graph[root][n]
                print(new_d)
                if new_d <= distances.get(n, float('inf')):
                    distances[n] = new_d
                    predecessors[n] = root
        
        visited.append(root)

        unvisited = {}
        
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))

        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)

