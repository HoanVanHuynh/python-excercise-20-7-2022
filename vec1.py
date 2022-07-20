class Vector2d:
    typecode = 'd' 

    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))

    
def radian_to_degree(number):
    return number * 180

result = radian_to_degree(2)

print(result)    

while True:
    rad = input('hoan')
    