class Vector2d:
    typecode = 'd' 

    def __init__(self, x, y):
        self.__x = float(x) 
        self.__y = float(y) 

    
    def y(self):
        return self.__y 
    
    def y(self):
        return self.__y 

    def __iter__(self):
        return (i for i in (self.x, self.y))

        