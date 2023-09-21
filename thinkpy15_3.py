import copy

class Point(object):
    '''Represents a point in 3d space'''

class Rectangle(object):
    '''Represents a rectangle.
    
    attributes: width, height, corner
    '''

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rect, dx, dy):
    moverect = copy.deepcopy(rect)
    moverect.corner.x +=5
    moverect.corner.y +=5
    return moverect
    #print (rect, dx, dy)

newbox = move_rectangle(box, 5,5)
print(newbox.corner.x, newbox.corner.y)