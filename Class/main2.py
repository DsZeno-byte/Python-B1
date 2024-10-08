class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distance(self,otherpoints):
        x1=self.x
        y1=self.y
        x2=otherpoints.x
        y2=otherpoints.y
        d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
        return d

p1=Point(0,0)
p2=Point(2,4)
p3=Point(3,6)
p4=Point(7,7)

print(p1)
print(p1.x)
print(p1.y)

# distance between p1 and p2

print(p1.distance(p2))