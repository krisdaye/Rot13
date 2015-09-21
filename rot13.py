"""
Program: rot13.py
Author:KRis Daye/IGC_TinkTInk
Date: 10/11/2012

this program will encode text using ROT13 method of encryption.
The user will input a line of text, each line will be encoded and added o a string
to be output at end.

Algorithm:
 1. Get line of text from user
 2. For each character in text, if it is not a letter, add it to the encoded text
    If it is a letter, add the letter 13 places from it to the encoded text.
 3. Output the encoded text.

"""

# Get a line of text from user
Cleartext = raw_input("Enter a line to encode: ")

# Create a string with the encoded text
encoded = ""
for ch in Cleartext:
    #check if its uppercase
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        #Check if in first half
        if ord(ch) <= ord('M'):
            next_letter = chr(ord(ch) + 13)
            #add letter to encoded string
            encoded = encoded + next_letter

        else:
            next_letter = chr(ord(ch) -13)
            encoded = encoded + next_letter

    #check if lower case
    elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        if ord(ch) <= ord('m'):
            next_letter = chr(ord(ch) + 13)
            encoded = encoded + next_letter

        else:
            next_letter = chr(ord(ch) -13)
            encoded = encoded + next_letter
                            

    #if neither, add to encoded text unaltered
    else:
        encoded = encoded + ch

#Output the encoded text
print"Encoded text: "
print encoded


#Pause
raw_input("Press enter to exit.")
