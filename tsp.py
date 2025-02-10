import itertools
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
def tsp(cities):
    shortest_distance = float('inf')
    shortest_path = None
    start_city = cities[0]
    other_cities = cities[1:]
    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm)
        current_distance = 0
        for i in range(len(current_path) - 1):
            current_distance += distance(current_path[i], current_path[i + 1])
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = current_path
    return shortest_path, shortest_distance
cities = [(0, 0), (1, 1), (2, 2), (3, 3)]
path, distance = tsp(cities)
print("Shortest path:", path)
print("Shortest distance:", distance)
