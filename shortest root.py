import itertools
distances = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25},
    'B': {'A': 10, 'C': 35, 'D': 25, 'E': 30},
    'C': {'A': 15, 'B': 35, 'D': 30, 'E': 20},
    'D': {'A': 20, 'B': 25, 'C': 30, 'E': 15},
    'E': {'A': 25, 'B': 30, 'C': 20, 'D': 15}
}
def tsp(cities):
    return min(itertools.permutations(cities), key=lambda route: sum(distances[route[i]][route[i+1]] for i in range(len(route)-1)))
cities = ['A', 'B', 'C', 'D', 'E']
shortest_route = tsp(cities)
print("Shortest route:", shortest_route)
