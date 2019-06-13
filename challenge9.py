#1

with open("if-elif文2.py","r",encoding="utf-8") as f:
    print(f.read())


#2

answer = input("好きな果物は何？")
with open("質問.txt","w",encoding="utf-8") as f:
    f.write(answer)


#3

import csv
movies = ["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man of Fire", "Flight"]
with open("映画.csv","w",newline='',encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
        

#4



import csv
movies2 = ["トップガン", "卒業白書", "マイノリティ・リポート"],["タイタニック", "レヴェナント: 蘇えりし者", "インセプション"],["トレーニング デイ", "マイ・ボディガード", "フライト"]
with open("映画(日本語).csv","w",newline='',encoding="utf-8") as csvfile2:
    spamwriter2 = csv.writer(csvfile2, delimiter=",")
    for movie_list2 in movies2:
        spamwriter2.writerow(movie_list2)
