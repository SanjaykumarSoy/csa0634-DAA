import math
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def closest_pair(points):
    min_distance = float('inf')
    closest_points = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_points = (points[i], points[j])
    return closest_points, min_distance
points = [(0, 0), (1, 1), (2, 2), (3, 3), (1, 0)]
closest_points, min_distance = closest_pair(points)
print(f"The closest points are {closest_points} with a distance of {min_distance}.")
