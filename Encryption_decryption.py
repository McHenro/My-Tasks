alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(your_message, key):
    encrypted_word = ""
    for member in your_message:
        if not member.islower():
            encrypted_word += member
        else:
            find_position = alphabet.find(member)
            new_position =(find_position + int(key)) % 26
            sliced_letter= alphabet[new_position]
            encrypted_word += sliced_letter
    print("Here is your encoded result:",encrypted_word)
         
def decode(your_message,key):
    decrypted_word = ""
    for element in your_message:
        if not element.islower():
            decrypted_word += element
        else:
            find_position = alphabet.find(element)
            new_position =(find_position - int(key)) % 26
            sliced_letter= alphabet[new_position]
            decrypted_word += sliced_letter
    print("Here is your decoded result:",decrypted_word)
    
def my_main():
    encript_or_decrypt = input("type 'encode' to encrypt, type 'decode' to decrypt: ")
    while  not (  encript_or_decrypt == "encode" or encript_or_decrypt == "decode"): 
        encript_or_decrypt = input(" you must type 'encode' to encrypt or 'decode' to decrypt: ")
    message = input("please enter your message: ")
   
    while True:
        try:
            key = input("Enter key,digit should be between 1 to 10: ")
            if key == "" or key.isspace():
                key = "0"         
            elif  not key.isdigit():
                raise ValueError
            elif int(key ) > 10 or int(key) < 1:
                raise Exception
        except ValueError:
            print("Key must be a digit, enter key again")
        except Exception:
            print("Key must not be less that 1 or greater than 10, try again")
        else:
            break     
            
    if encript_or_decrypt == 'encode':
        encode(message, key)
    elif encript_or_decrypt == 'decode':
        decode(message,key)
    proceed = input("Do u want to continue? yes or  no: ")
    if proceed =="yes":
        my_main()
    elif proceed == "no":
        return       
my_main()
