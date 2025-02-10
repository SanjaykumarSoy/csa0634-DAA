def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
def convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if k != i and k != j:
                        if orientation(points[i], points[j], points[k]) < 0:
                            break
                else:
                    hull.append(points[i])
                    hull.append(points[j])
                    break
    return list(set(hull))
points = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2)]
print(convex_hull(points))


