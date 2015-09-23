__author__ = 'alicia.williams'

#Week Three: Pig Latin
#CIS-125 FA 2015

# File: PigLatinAssignment.py
# This program takes English words and translates them to Pig Latin.

def main():
    print("This program translates an English word to Pig Latin. \n")
    
    #Prompting the user to enter an English word to translate.
    #To compensate for the case sensitivity, I created another variable with the
    #lower string method and attached that to the eng variable to make the
    #outputs all lowercase.
    eng = input("Please enter an Engilsh word to translate: ")
    pig = eng.lower()
    vowel = "aeiouAEIOU"
    
    #Translate the word into Pig Latin.
    #Printing the translated word.
    if pig[0] in vowel:
        print(pig + "yay")
    else:
        print(pig[1:] + pig[0] + "ay")
    
main()