import requests
import hashlib
import sys

def password_to_hash(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return hashed_password

def hash_split(hashed_password):
    return hashed_password[:5],hashed_password[5:]

def api_data(first5):
    url = "https://api.pwnedpasswords.com/range/" + first5
    res = requests.get(url) 
    return res.text

def list_splitter(list_of_hashes,reference):
    hashes = (line.split(":") for line in list_of_hashes.splitlines())
    for tail,count in hashes:
        if tail == reference:
            return(f"This password has been found {count} times!")
    return("Password is safe to use!")


def main_function():
    password = input("Please input your password: ")
    hashed_password = password_to_hash(password)
    first5,tail = hash_split(hashed_password)
    list_of_hashes = api_data(first5)
    print(list_splitter(list_of_hashes,tail))

if __name__ == "__main__":
    main_function()


