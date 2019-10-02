import uuid
import hashlib
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt

print('---------------------------------------------------------------------------------------------------------------------------------------')
print("Rock, Paperr, Scissors account setup")
print('---------------------------------------------------------------------------------------------------------------------------------------')
while True :
    username = input('Pick a username : ')
    password = input('Pick a password : ')
    passwordConfirm = input('Please confirm your password : ')

    if password != passwordConfirm :
        print("your password don't match. please try again")
        
    if password == passwordConfirm :
        print("your account has been setup.")
        accountsFile = open("accounts.txt",'a')
        accountsFile.write(username)
        accountsFile.write(" ")
        accountsFile.write(hash_password(password))
        accountsFile.write("\n")
        accountsFile.close()
        break
