# implementing master password ( a custom password along with the key file to get correct credentials)
from cryptography.fernet import Fernet

# needed to run this fn only once
'''
def write_key():
   key = Fernet.generate_key()
   with open("key.key","wb") as key_file:  #wb => write in bytes
      key_file.write(key) '''

def load_key():
   file = open("key.key","rb")
   key = file.read()
   file.close()
   return key

key = load_key() 
fer = Fernet(key)  # initializing the Fernet module

# encode() converts it into bytes & decode() does vice versa
# b'jhcdewe'  this is a byte string     
def view():
   with open("passwords.txt","r") as file:
      for account in file.readlines():
        user,passw = account.split("|")
        print(f"Account name: {user}, password:{fer.decrypt(passw.encode()).decode()}")
        # rstrip removes the \n from the word inserted while writing our file from the end of the line
         

def create():
   name = input("Enter account name: ")
   pwd = input("Enter password:")

   with open("passwords.txt","a") as file:
      file.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n") 
    
   print("password created!")

while True:
    mode = input("View existing passwords or create a new one? (view/create/quit): ").lower()
    if mode == "quit":
       exit()

    elif mode == "create":
       create()

    elif mode == "view":
       view()

    else:
       print("Enter a valid option.")
       continue