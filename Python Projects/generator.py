import random 
import string

def generator():
     
    # Input management with error cases 
    length = input("Enter the length required : ")
    while(length.isdigit() == False | int(length) < 12):
        if(length.isdigit() == False):
            print("Warning :  Length has to be an integer !\n ")
            length = input("Enter the length required : ")
        else : # if not an integer
            print("Warning :  Length has at least 12 long !\n ")
            length = input("Enter the length required : ")
  
    
    # Conversion type of length
    length = int(length)
    
    # Available string for the password generated including 
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    alphabet = string.ascii_letters + string.digits + string.punctuation - "e"

    # Generates the password by taking random choices in the alphabet length times 
    password = ''.join(random.choice(alphabet) for i in range(length))
    
    print(f"Your password has been successfully created {password}")
    
    return password 
    
new_pass = generator()