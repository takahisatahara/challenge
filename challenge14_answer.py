#1

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)


#2

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)


#3

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
