#1

class Square:
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

s1 = Square(10)
s2 = Square(20)
s3 = Square(30)

print(Square.square_list)


#2

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

square = Square(29)
print(square)


#3

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("ta", "tg"))
