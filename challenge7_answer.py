#1

shows = ["ウォーキング・デッド", "アントラージュ",
         "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for show in shows:
    print(show)


#2

for i in range(25,51):
    print(i)


#3

shows = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ",
         "ヴァンパイア・ダイアリーズ"]
for index, show in enumerate(shows):
    print(index)
    print(show)


#4 他に表示


#5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(mult)

print(list3)
