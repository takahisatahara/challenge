#1
print("#1")


def f(x):
    return x ** 2

print(f(8))


#2
print("#2")

def print_string(string):
    print(string)

print_string("moziretu,文字列、もじれつ，12345.67890")


#3
print("#3")


def five(a, b, c, d = 4, e = 5):
    return a + b + (c + d) * e

result3 = five(1, 2, 3)
print(result3)


#4
print("#4")


def one(x):
    return x / 2

def two(x):
    return x * 4

v = one(8)
result4 = two(v)

print(result4)


#5
print("#5")


def m(x):
    try:
        return float(x)
    except ValueError:
        print("数字にして下さい。")
    
result5 = m("5h4.45")
print(result5)
    

    

