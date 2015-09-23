__author__ = 'alicia.williams'

#Week Three: Star Wars
#CIS-125 FA 2015

# File: StarWarsName.py
# A program to generate my Star Wars Name.

def main():
    print("This program creates your Star Wars Name. \n")
    
    #Prompts to obtain user's first, last, and mother's maiden name as well as
    #the city they were born in.
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    maiden = input("Please enter your mother's maiden name: ")
    city = input("Please enter name of the city you were born in: ")
    
    #Calculation of Star Wars Name.
    #First name is the first 3 letters of user's last name and first 2 letters
    #of user's first name.
    #Last name is the first 2 letters of user's mother's maiden name and first 3
    #letters of the name of the user's city of birth.
    swfirst = last[:4] + first[:3]
    swlast = maiden[:3] + city[:4]
    
    #Printing of Star Wars Name.
    print("Your Star Wars name is: ", swfirst, swlast)

main()