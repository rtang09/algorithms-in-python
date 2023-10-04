def bfs(graph, start, end):
    #given two points of a graph, find the minimum distance between the points
    queue = [start]
    distances = {start:0}
    while queue:
        front = queue.pop()
        neighbors = graph[front]
        for neighbor in neighbors:
            if not neighbor in distances:
                queue.append(neighbor)
                distances[neighbor] = distances[front]+1
            if neighbor == end:
                return distances[end]
                break

if __name__ == "__main__":
    graph = {0: [2, 4, 5], 1: [4, 5], 2: [3, 4], 3: [], 4: [5], 5: [0]}
    print(bfs(graph, 1, 3))
