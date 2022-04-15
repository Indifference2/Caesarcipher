from art import logo

def caesar(text,shift):
    cipher_text = []
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_positions = (position + shift)%26
            if direction == "decode":
                new_positions = (position - shift)
            cipher_text += alphabet[new_positions]
        else:
            cipher_text += letter        
                           
    print (f"The encoded text is: " + "" + "".join(cipher_text))

alphabet = [
    'a', 'b', 'c', 
    'd', 'e', 'f', 
    'g', 'h', 'i', 
    'j', 'k', 'l', 
    'm', 'n', 'o', 
    'p', 'q', 'r', 
    's', 't', 'u', 
    'v', 'w', 'x', 
    'y', 'z'
    ] 

while True:     
    print (logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
   
    caesar(text, shift)
    quit = input ("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if quit == "yes":
        break
