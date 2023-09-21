class Point(object):
    '''Represents a point in 3d space'''
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    
    #todo:  
    def __str__(self):
        return'%0.2f, %2.2f' %(self.x, self.y)

p1 = Point(.4, 4.4)
print (p1)