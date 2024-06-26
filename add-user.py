import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print(f"Use the username  '" + username + "'? (Y/N) ")
        # converts user name to uppercase
        confirm = input().upper()
        # won't run because sudo is for ubuntu and im in windows 
    os.system(f"net user {username} /add")
new_user()
    