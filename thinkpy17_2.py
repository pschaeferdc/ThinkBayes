class Point(object):
    '''Represents a point in 3d space'''
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
     
    def __str__(self):
        return'%0.2f, %2.2f' %(self.x, self.y)
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return'%0.2f, %2.2f' %(new_x, new_y)


p1 = Point(.4, 4.4)
p2 = Point(.3, 3.3)
print (p1 + p2)