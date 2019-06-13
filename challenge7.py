#1

lists = ["ウォーキング・デッド", "アントラージュ",
         "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for show in lists:
    print(show)


#2

for i in range(25, 51):
    print(i)


#3

lists = ["ウォーキング・デッド", "アントラージュ",
         "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for index,show in enumerate(lists):
    print(index)
    print(show)


#4 他で作成

#5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)        


        


