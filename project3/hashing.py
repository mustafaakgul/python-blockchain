import uuid
import hashlib

def hash_pass(password):
    # UUID is used to generate number of the specified password
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

def check_pass(hash_password, user_pass):
    password, salt = hash_password.split(':')
    result = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()
    if password == result:
        return True
    else:
        return False
    #return password == hashlib.sha256(salt.encode() + user_pass.encode().hexdigest)

new_pass = input("Enter Password: ")
hash_password = hash_pass(new_pass)

print("The string to store in the db is: " + hash_password)

old_pass = input("Enter password again to check: ")

if check_pass(hash_password, old_pass):
    print("You entered right password.")
else:
    print("Passwords not matched")


# def check_pass(hash_password, user_pass):
#     password, salt = hash_password.split(':')
#     return password == hashlib.sha256(salt.encode() + user_pass.encode().hexdigest)