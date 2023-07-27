import sys
from random import randint
from string import maketrans

if(len(sys.argv) > 1):
    #normal alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #randomly create a new ciphernet
    cipherbet = ""
    left = alphabet

    for i in range(0, len(alphabet)):
        x = randint(0, len(left) - 1)
        cipherbet += left[x]
        left = left[:x] + left[x + 1:]

        #get input text to translate
        text = sys.argv[1].lower()
        print("text", text)
        trantab = maketrans(alphabet, cipherbet)
        text = text.translate(trantab)

        #replace unused letters in cipherbet with _'s
        for i in cipherbet:
            if i not in text:
                cipherbet = cipherbet.replace(i, "_")

                #print cipherbet (solution) and the txt cryptogram
                print(cipherbet)
                print(text)