#This is a SUPER-SECRET language.
#Rövarspråket is not very complicated: you take an ordinary word and replace the consonants with the consonant doubled and with an "o" in between.
#So the consonant "b" is replaced by "bob", "r" is replaced with "ror", "s" is replaced with "sos", and so on. Vowels are left intact.
#It's made for Swedish, but it works just as well in English.

def encode(string):
    output = ""
    for i in range(len(string)):
        char = string[i]
        if char.lower() not in ["a", "e", "i", "o", "u", " "]:
            output = output + char + "o" + char.lower()
        else:
            output = output + char
    return print(output)

encode("robber language")
