class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return "(" + str(self.x) + "," + str(self.y) + ")"
class Rectangle:
    def __init__(self, p, q):
        assert isinstance(p,Point), "Bad input!"
        assert isinstance(q,Point), "Bad input!"
        assert p.x<q.x, "Bad input!"
        assert p.y<q.y, "Bad input!"
        self.p = p
        self.q = q
    def __str__(self):
        return "(" + "p = " + str(self.p) + ", q = " + str(self.q) + ")"
    def get_width(self):
        return self.q.x-self.p.x
    def get_height(self):
        return self.q.y-self.p.y
    def perimeter(self):
        return (self.get_width()*2) + (self.get_height()*2)
    def area(self):
        return self.get_width()*self.get_height()
    def contains(self, pt):
        if pt.x<= self.q.x and pt.x>=self.p.x and pt.y<=self.q.y and pt.y>=self.p.y:
            return True
        return False
p1 = Point (1 , 2)
p2 = Point (3.2 , 4)
R = Rectangle ( p1 , p2 )
print(R)
print(R.get_width())
print(R.get_height())
print(R.area())
print(R.perimeter())
print(R.contains(Point(1.5,3)))
print(R.contains(Point(10.5,3)))
print(R.contains(Point(1,2)))
print(R.contains(Point(3.2,4)))
