text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())  #is the text all uppercase?

print(text.upper())   #convert the text to uppercase

print(text.upper().isupper())   #is the text all uppercase? YESSSSS

new_text = text.upper()
print(text, new_text)
print("bannannnana".count("n"))
print("bannannnana".index("ana"))
print("bababannanana".replace("ana", "XXYYZZ"))

sentence = "Hello, kind-sir; how many ! I be of service today ?"
print(sentence.replace(",", "").replace("Hello", "Hi"))

#elegant way to do it
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, " ")
print(sentence)


print("this is a sentence and i want the words".split(""))


text = "Bob goes to school. Bob likes to play tennis."
print(text.find("Bob"))
print(text.rfind("Bob", i))

while i < len(text):
    if i == -1:
        break
    print(i)
i += 1

