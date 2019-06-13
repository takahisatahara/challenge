#1

def f(x):
    return x ** 2

print(f(2))


#2

def string(x):
    print(x)

string("test 1, 2, 3")


#3

def five(a, b, c, d = 4, e = 5):
    return a + b + c + d + e

result = five(1, 2, 3)
print(result)

#4

def f(x):
    return x / 2
        
def g(y):
    return y * 4

z = f(6)
u = g(z)

print(u)

#5

def con(str):
    try:
        return float(str)
    except ValueError:
        print("文字列をfloat型にできません。")

w = con("1245")
print(w)

#6


#6.1

def f(x):
    """
    整数を受け取り、それを２乗する。
    設定値ｘは整数
    ｘを２乗した戻り値を返す。
    """
    return x ** 2

print(f(2))


#6.2

def string(x):
    """
    文字列を出力する。
    設定値ｘは文字列のデータ型。
    """
    print(x)

string("test 1, 2, 3")


#6.3

def five(a, b, c, d = 4, e = 5):
    """
    ３つの必須引数と２つのオプション引数を全て足した戻り値を返す。
    a, b, c, d, e, 戻り値 は全て整数。
    """
    return a + b + c + d + e

result = five(1, 2, 3)
print(result)


#6.4

def f(x):
    return x / 2
        
def g(y):
    return y * 4

z = f(6)
u = g(z)

print(u)


#6.5

def con(str):
    """
    設定値strは文字列のデータ型。
    戻り値は文字列をfloat型に変換したもの。
    """
    try:
        return float(str)
    except ValueError:
        print("文字列をfloat型にできません。")

w = con("1245")
print(w)
