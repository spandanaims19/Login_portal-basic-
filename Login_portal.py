import json
import os
import hashlib
import re

def validate_email(email):
    pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern,email)

"""
a-zA-Z: Allows lowercase and uppercase letters.

0-9: Allows digits.

_.+-: Allows special characters like underscore (_), dot (.), plus (+), and hyphen (-).

+: Ensures at least one or more of these characters are present.

"""

def register_user():
    username=input("Enter username : ")
    while True:
        email=input("Enter email : ")
        if(validate_email(email)):
            break
        else:
            print("Invalid email format, try again")
    
    while True:
        password=input("Enter password : ")
        confirm_password=input("Confirm password : ")

        if(password==confirm_password):
            break
        else:
            print("Passwords do not match, try again")
    
    encrypted_password=hashlib.sha256(password.encode()).hexdigest()
    user_data={"username":username,"password":encrypted_password,"email":email}

    with open("dataset.json","a") as file:
        json.dump(user_data,file)
        file.write("\n")
        print(f"{username} Registration successful")



def login_user():
    username=input("Enter username : ")
    password=input("Enter password : ")

    while True:
        email=input("Enter email : ")
        if(validate_email(email)):
            break
        else:
            print("Invalid email format, try again")

    encrypted_password=hashlib.sha256(password.encode()).hexdigest()

    with open("dataset.json","r") as file:
        for line in file:
            userdata=json.loads(line)
            if(userdata["username"]==username and userdata["password"]==encrypted_password and userdata["email"]==email):
                print(f"Welcome {username}\nLogin Successful")
                return
        else:
            print("Invalid credentials")


def main():
    while True:
        choice=int(input("1 - Register new user\n2 - Login user\n3 - Exit\nEnter your choice : "))

        if choice==1:
            register_user()
        elif choice==2:
            login_user()
        elif choice==3:
            print("Bye!!!")
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()