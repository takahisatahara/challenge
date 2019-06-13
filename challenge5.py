#1

my_misician = ["爆風スランプ", "米米クラブ", "槇原敬之",]
print(my_misician)


#2

my_lists = []

itogahama = (33.365357, 131.595258)
rakutenchi = (33.274173, 131.481575)
suginoi_hotel = (33.284026, 131.475026)

my_lists.append(itogahama)
my_lists.append(rakutenchi)
my_lists.append(suginoi_hotel)

print(my_lists)


#3

my_character = {"身長": "183cm",
                "体重": "83kg",
                "好きな色": "赤",
                "好きな食べ物": "カレーうどん"}

print(my_character)


#4

my_character = {"身長": "183cm",
                "体重": "83kg",
                "好きな色": "赤",
                "好きな食べ物": "カレーうどん"}

a = input("私の聞きたい特徴は？")

if a in my_character:
    chara = my_character[a]
    print(chara)

else:
    print("それは答えられません。")


#5

my_misician_ny = {
    "爆風スランプ":
              ["Runner",
               "大きな玉ねぎの下で",
               "無理だ！！",],
    "米米クラブ":
              ["I can be.",
               "浪漫飛行",
               "君がいるだけで",],
    "槇原敬之":
              ["どんなときも",
               "もう恋なんてしない",
               "No.1",],
    }

print(my_misician_ny)


#6 "set"は辞書のキー部分を抜き出す。リスト、タプルは辞書のキーになる。
#  どちらとも文字列はランダム。整数は数字順に並べ替えられる。

x = set(my_misician_ny)
print(x)
