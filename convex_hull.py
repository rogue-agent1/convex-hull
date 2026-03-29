#!/usr/bin/env python3
"""Convex hull algorithms. Zero dependencies."""
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1: return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def hull_area(hull):
    n = len(hull)
    if n < 3: return 0
    area = 0
    for i in range(n):
        j = (i+1) % n
        area += hull[i][0]*hull[j][1] - hull[j][0]*hull[i][1]
    return abs(area) / 2

def hull_perimeter(hull):
    import math
    n = len(hull); p = 0
    for i in range(n):
        j = (i+1) % n
        p += math.hypot(hull[j][0]-hull[i][0], hull[j][1]-hull[i][1])
    return p

def point_in_hull(point, hull):
    n = len(hull)
    for i in range(n):
        if cross(hull[i], hull[(i+1)%n], point) < 0: return False
    return True

if __name__ == "__main__":
    pts = [(0,0),(1,0),(0,1),(1,1),(0.5,0.5)]
    h = convex_hull(pts)
    print(f"Hull: {h}, Area: {hull_area(h):.2f}")
