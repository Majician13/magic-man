#Define a class named Rectangle which can be
#constructed by a length and width. The Rectangle
#class has a method which can compute the area.

class rectangle(object):
    def __init__(self, l, w):
        self.area = l * w
        
    def area(self):
        return self.area
    
aRectangle = rectangle(4, 3)
print(aRectangle.area)