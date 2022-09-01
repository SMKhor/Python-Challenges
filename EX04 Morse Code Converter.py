#	EX04	MORSE CODE CONVERTER	Can you create a text to morse code converter with a menu, and also convert morse code to text
print("Morse Code Converter")
print("Dots will be represented as . and dashes will be represented as -")
print("Separate letters by spaces and words by /")
print("Convert text to morse code (1)")
print("Convert morse code to text (2)")
mode = input("Which mode would you like to use? ")

char_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"," ",".", ",","?","!","'","(",")","&",":",";","/","_","=","+","-","$","@"]
morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.","....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-","-.--", "--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----.","/",".-.-.-","--..--","..--..","-.-.--",".----.","-.--.","-.--.-",".-...","---...","-.-.-.","-..-.","..--.-","-...-",".-.-.","-....-","...-..-",".--.-."]

if mode == "1":
    print("\nMode - Text to Morse Code")
    morseoutput = ""
    textinput = input("Text to convert: ")
    for i in range(len(textinput)):
        char = textinput[i].upper()
        place = char_list.index(char)
        morseoutput = morseoutput + morse_list[place] + " "
    print("Morse code:",morseoutput)

if mode == "2":
    print("\nMode - Morse Code to Text")
    textoutput = ""
    morsecodeinput= input("Morse Code to convert: ").split()
    for i in range(len(morsecodeinput)):
        element = morsecodeinput[i]
        place = morse_list.index(element)
        textoutput = textoutput + char_list[place]
    print("Text:",textoutput)
