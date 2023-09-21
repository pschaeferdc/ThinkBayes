from math import sqrt

class Point(object):
    '''Represents a point in 3d space'''

pb = Point()
pb.x = 3.0
pb.y = 4.0

pa = Point()
pa.x = 0.0
pa.y = 0.0

def distance(a,b):
    dist = sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return dist

print(distance(pa,pb))