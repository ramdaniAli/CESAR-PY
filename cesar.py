import string
alphabet = string.ascii_lowercase 

def decrypt():
    
    encry_msg = input("enter key : ").strip()
    
    key = int(input("enter cesar index: "))
    
    decry_msg = ""

    for c in encry_msg:
        if c in alphabet:
            new_character = alphabet[alphabet.find(c) + key]
            decry_msg  += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()
