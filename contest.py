alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"

f = open("secret.txt")
text = f.read()
print(text)


for line in lines:
    n_vowels = 0
    for v in vowel:
        n_vowels += line.count(v)
    print(alphabet[n_vowels], end="")

