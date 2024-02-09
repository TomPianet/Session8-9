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