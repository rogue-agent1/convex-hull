#!/usr/bin/env python3
"""convex_hull: Convex hull algorithms (Graham scan, Jarvis march)."""
import math, sys

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def graham_scan(points):
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
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

def jarvis_march(points):
    pts = list(set(points))
    if len(pts) <= 2: return pts
    start = min(pts, key=lambda p: (p[0], p[1]))
    hull = []
    current = start
    while True:
        hull.append(current)
        candidate = pts[0]
        for p in pts[1:]:
            if candidate == current or cross(current, candidate, p) < 0:
                candidate = p
            elif cross(current, candidate, p) == 0:
                if dist2(current, p) > dist2(current, candidate):
                    candidate = p
        current = candidate
        if current == start: break
    return hull

def dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def area(hull):
    n = len(hull)
    a = sum(hull[i][0]*hull[(i+1)%n][1] - hull[(i+1)%n][0]*hull[i][1] for i in range(n))
    return abs(a) / 2

def test():
    pts = [(0,0),(1,0),(0,1),(1,1),(0.5,0.5)]
    hull = graham_scan(pts)
    assert len(hull) == 4
    assert (0.5,0.5) not in hull
    hull2 = jarvis_march(pts)
    assert len(hull2) == 4
    assert abs(area(hull) - 1.0) < 0.001
    # Collinear
    pts2 = [(0,0),(1,0),(2,0)]
    assert len(graham_scan(pts2)) >= 2
    # Triangle
    pts3 = [(0,0),(4,0),(2,3)]
    h3 = graham_scan(pts3)
    assert len(h3) == 3
    assert abs(area(h3) - 6.0) < 0.001
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Usage: convex_hull.py test")
