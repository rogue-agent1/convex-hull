from convex_hull import convex_hull, hull_area, hull_perimeter, point_in_hull
pts = [(0,0),(1,0),(0,1),(1,1),(0.5,0.5)]
h = convex_hull(pts)
assert len(h) == 4
assert abs(hull_area(h) - 1.0) < 0.01
assert hull_perimeter(h) > 0
assert point_in_hull((0.5,0.5), h)
assert convex_hull([(0,0)]) == [(0,0)]
assert convex_hull([]) == []
print("convex_hull tests passed")
