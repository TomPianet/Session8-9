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
# Removing punctuation from a sentence
sentence = "This is a sentence, with some punctuation! And a question mark?"
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, " ")

# Split the cleaned sentence into words
words = sentence.split()  # Split method without arguments splits on any whitespace

# Find the occurrences of "Bob" in the text
text = "Bob goes to school. Bob likes to play tennis."
first_bob = text.find("Bob")  # Finds the first occurrence of "Bob"
i = len(text)  # Set 'i' to the length of text for rfind
last_bob = text.rfind("Bob", 0, i)  # Finds the last occurrence of "Bob"

# Loop to find all occurrences of "Bob"
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1  # Increment 'i' to avoid an infinite loop
