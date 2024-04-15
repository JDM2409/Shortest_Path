import sys
import heapq

class MAP:
    def __init__(self):
        self.adjacents = {}

    def generate_edge(self, C1, C2, dist):
        if C1 not in self.adjacents:
            self.adjacents[C1] = {}
        if C2 not in self.adjacents:
            self.adjacents[C2] = {}
        self.adjacents[C1][C2] = dist
        self.adjacents[C2][C1] = dist

def input_reader(input_filename):
    graph = MAP()
    with open(input_filename, 'r') as f:
        for line in f:
            if line.strip() == "END OF INPUT":
                break
            start_point, end_point, dist = line.split()
            graph.generate_edge(start_point, end_point, int(dist))
    return graph

def hueristic_reader(heuristic_filename):
    heuristic = {}
    with open(heuristic_filename, 'r') as f:
        for line in f:
            if line.strip() == "END OF INPUT":
                break
            city, h_value = line.split()
            heuristic[city] = int(h_value)
    return heuristic

def find_route(graph, origin_city, destination_city, heuristic=None):
    if heuristic:
        return informed_search(graph, origin_city, destination_city, heuristic)
    else:
        return uninformed_search(graph, origin_city, destination_city)

def uninformed_search(graph, origin_city, destination_city):
    visited = set()
    popped = 0
    expanded = 0
    generated = 1 
    queue = [(0, [origin_city])]

    while queue:
        popped += 1
        cost, path = heapq.heappop(queue)
        current_city = path[-1]

        if current_city == destination_city:
            return path, cost, popped, expanded, generated

        if current_city not in visited:
            expanded += 1
            visited.add(current_city)
            for neighbor, dist in graph.adjacents[current_city].items():
#                if neighbor not in visited:
                generated += 1
                heapq.heappush(queue, (cost + dist, path + [neighbor]))

    return None, None, popped, expanded, generated

def informed_search(graph, origin_city, destination_city, heuristic):
    visited = set()
    popped = 0
    expanded = 0
    generated = 1
    queue = [(heuristic[origin_city], 0, [origin_city])]

    while queue:
        popped += 1
        _, cost, path = heapq.heappop(queue)
        current_city = path[-1]

        if current_city == destination_city:
            return path, cost, popped, expanded, generated

        if current_city not in visited:
            expanded += 1
            visited.add(current_city)
            for neighbor, dist in graph.adjacents[current_city].items():
#                if neighbor not in visited:
                generated += 1
                heapq.heappush(queue, (heuristic[neighbor] + cost + dist, cost + dist, path + [neighbor]))

    return None, None, popped, expanded, generated

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: find_route input_filename origin_city destination_city [heuristic_filename]")
        sys.exit(1)

    input_filename = sys.argv[1]
    origin_city = sys.argv[2]
    destination_city = sys.argv[3]

    heuristic = None
    if len(sys.argv) == 5:
        heuristic_filename = sys.argv[4]
        heuristic = hueristic_reader(heuristic_filename)

    graph = input_reader(input_filename)
    path, cost, popped, expanded, generated = find_route(graph, origin_city, destination_city, heuristic)

    if path:
        print("Nodes Popped:", popped)
        print("Nodes Expanded:", expanded)
        print("Nodes Generated:", generated)
        print("Distance:", cost, "km")
        print("Route:")
        for i in range(len(path) - 1):
            print(f"{path[i]} to {path[i + 1]}, {graph.adjacents[path[i]][path[i + 1]]} km")
    else:
        print("Nodes Popped:", popped)
        print("Nodes Expanded:", expanded)
        print("Nodes Generated:", generated)
        print("Distance: infinity")
        print("Route:")
        print("None")