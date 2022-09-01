#	AS06	VOWEL COUNT	How many vowels does a word have? You are going to find out...
word = input("Word to check: ")
vowelcount = 0
for i in range(len(word)):
    char = word[i]
    if char.lower() in ["a","e","i","o","u"]:
        vowelcount = vowelcount + 1

print("The word,",word, "has", str(vowelcount), "vowel(s).")
