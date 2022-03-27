class Point:
    #Con initialize with x and y just like in java using this.x=x
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("😎😎😎😎😎😎")

point=Point(10,20)
print(point.x)
point.y=30
print(point.y)