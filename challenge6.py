#1

print("カミュ"[0])
print("カミュ"[1])
print("カミュ"[2])


#2

write = input("何を書いた？：")
place = input("どこに送った？：")

words = "私は昨日{}を書いて、{}に送った！".format(write, place)
print(words)


#3

words = "aldous Huxley was born in 1894.".capitalize()
print(words)


#4

words = "どこで？　だれが？　いつ？"
print(words.split("　"))


#5

words1 = ["The","fox","jumped","over","the","fence","."]
words2 = " ".join(words1)
words3 = words2[:-2] + "."
print(words3)

#5.1 他の解答
words = ["The","fox","jumped","over","the","fence","."]
print((" ".join(words))[:-2] + ".")

#6

print("A screaming comes across the sky.".replace("s","$"))


#7

print("Hemingway".index("m"))


#8

print("ジョルノ・ジョバーナは言う '僕はギャングスターになる！' と・・・")


#9

print(("three " + "three " + "three ")[:-1])

print(("three " * 3)[:-1])


#10

print("四月の晴れた寒い日で、時計がどれも十三時を打っていた。"[:10])




