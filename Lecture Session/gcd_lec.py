# Line segments intersect

def orientation(p, q, r):
    d = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])

    if d > 0:
        return 1 # clockwise
    elif d < 0:
        return 2 # anti-clockwise
    else:
        return 0 # collinear


def isColl(p, q, r):
    return (r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0])
            and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]))

def isIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)

    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and isColl(p1, q1, p2):
        return True

    if o2 == 0 and isColl(p1, q1, q2):
        return True

    if o3 == 0 and isColl(p2, q2, p1):
        return True

    if o4 == 0 and isColl(p2, q2, q1):
        return True

    return False


p1 = [-2, 0]
q1 = [2, 0]

p2 = [3, 2]
q2 = [3, -2]

print(isIntersect(p1, q1, p2, q2))