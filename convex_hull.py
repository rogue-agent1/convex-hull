#!/usr/bin/env python3
"""Convex hull using Graham scan."""
import math

def _cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 2: return points
    lower = []
    for p in points:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def hull_area(hull):
    n = len(hull)
    if n < 3: return 0
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    return abs(area) / 2

def hull_perimeter(hull):
    n = len(hull)
    p = 0
    for i in range(n):
        j = (i + 1) % n
        p += math.sqrt((hull[j][0]-hull[i][0])**2 + (hull[j][1]-hull[i][1])**2)
    return p

def point_in_hull(point, hull):
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        if _cross(hull[i], hull[j], point) < 0:
            return False
    return True

if __name__ == "__main__":
    pts = [(0,0),(1,0),(0,1),(1,1),(0.5,0.5)]
    hull = convex_hull(pts)
    print(f"Hull: {hull}\nArea: {hull_area(hull)}")

def test():
    pts = [(0,0),(1,0),(0,1),(1,1),(0.5,0.5),(0.3,0.7)]
    hull = convex_hull(pts)
    assert len(hull) == 4  # square corners
    assert (0,0) in hull and (1,1) in hull
    assert (0.5,0.5) not in hull
    assert abs(hull_area(hull) - 1.0) < 1e-10
    assert abs(hull_perimeter(hull) - 4.0) < 1e-10
    # Triangle
    tri = convex_hull([(0,0),(2,0),(1,1)])
    assert len(tri) == 3
    assert abs(hull_area(tri) - 1.0) < 1e-10
    # Collinear
    assert len(convex_hull([(0,0),(1,1),(2,2)])) == 2
    # Point in hull
    hull = convex_hull([(0,0),(4,0),(4,4),(0,4)])
    assert point_in_hull((2,2), hull)
    print("  convex_hull: ALL TESTS PASSED")
