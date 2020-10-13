import string
alphabet = string.ascii_lowercase 

def decrypt():
    
    encrypted_message = input("enter key : ").strip()
    
    key = int(input("enter cesar index: "))
    
    decrypted_message = ""

    for c in encrypted_message:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key)
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()
