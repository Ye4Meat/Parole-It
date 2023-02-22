import random

print("This is a password generator.")

new_parole_length = int(input("Enter a length of your new password: "))

if new_parole_length < 8:           
    print("Your password will be too easy. Try again.")             
elif new_parole_length > 12:        
    print("It's not necessary to set up such long password. Try again.")        
else:        
    print("OK, let's do it!")
            
    password_length = 0
    symbols = ""
    while password_length != new_parole_length:
        new_pass = random.randrange(33, 127)
        new_pass = chr(new_pass)
        symbols += new_pass
        password_length +=1
            
    print("Your new password is: ", symbols)