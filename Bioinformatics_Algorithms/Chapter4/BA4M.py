### Solve the turnpike problem ###

def Turnpike(points):
    if len(points) == 2:
        return [0, points[1]]
    distances = [abs(points[0] - p) for p in points[1:]]
    max_idx = distances.index(max(distances))
    left_points = [abs(points[0] - p) for p in points[1:max_idx+1]]
    right_points = [abs(points[max_idx] - p) for p in points[max_idx+1:]]
    left_set = Turnpike(left_points)
    right_set = Turnpike(right_points)
    return [x for x in left_set] + [points[0]] + [x + abs(points[max_idx] - points[0]) for x in right_set]

dist_arr = [int(diff) for diff in '-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10'.split()]
print(Turnpike(dist_arr))