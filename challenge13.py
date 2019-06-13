#1

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(10,20)
a_square = Square(10)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())


#2

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    
    def change_size(self, new_size):
        self.s1 += new_size
        

a_square = Square(100)
print(a_square.s1)

a_square.change_size(300)
print(a_square.s1)


#3

class Shape:
    def what_i_am(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(10, 20)
a_square = Square(10)

a_rectangle.what_i_am()
a_square.what_i_am()


#4

#馬に
class Horse:
    def __init__(self, name):
        self.name = name

#騎手を持つ        
class Rider:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

dipu = Horse("ディープインパクト")
the_rider = Rider("武 豊", dipu)

#馬(Horse)に騎手(Rider)を持つ
print(the_rider.horse.name)
