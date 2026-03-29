#!/usr/bin/env python3
"""convex_hull - Convex hull computation using Graham scan and Andrew's monotone chain."""
import sys

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def monotone_chain(points):
    pts = sorted(set(points))
    if len(pts) <= 1: return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
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

def point_in_hull(point, hull):
    n = len(hull)
    for i in range(n):
        if cross(hull[i], hull[(i+1)%n], point) < 0:
            return False
    return True

def test():
    pts = [(0,0), (1,0), (0,1), (1,1), (0.5, 0.5)]
    hull = monotone_chain(pts)
    assert len(hull) == 4
    assert (0.5, 0.5) not in hull
    assert abs(hull_area(hull) - 1.0) < 1e-9
    assert point_in_hull((0.5, 0.5), hull)
    assert not point_in_hull((2, 2), hull)
    tri = monotone_chain([(0,0), (4,0), (0,3)])
    assert abs(hull_area(tri) - 6.0) < 1e-9
    print("convex_hull: all tests passed")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("Usage: convex_hull.py --test")
