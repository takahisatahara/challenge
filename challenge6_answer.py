#1

author = "Camus"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])


#2

answer1 = input("What did you write yesterday?")
answer2 = input("Where did you go yesterday?")

new_string = "Yesterday I wrote a {}. I sent it to {}.".format(answer1, answer2)

print(new_string)


#3

x = "aldous huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)


#4

lst = "Where now? Who now? When now?".split("?")
print(lst)


#5

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)


#6

sentence = "A screaming comes across the sky."
sentence = sentence.replace("s", "$")
print(sentence)


#7

first_index = "Hemingway".index("H")
print(first_index)


#8

quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"


#9

concat = "three" + "three" + "three"
mult = "three" * 3

print(concat)
print(mult)


#10

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)
