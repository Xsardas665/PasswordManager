# hashlib is a library that provides secure hash functions,
# including SHA-256, for creating hash values from data,
# often used for password hashing and data integrity verification.
import hashlib
# json is a library for encoding and decoding JSON (JavaScript Object Notation) data,
# commonly used for data serialization and interchange.
import json
# os is a library for interacting with the operating system,
# allowing to perform tasks like file and directory manipulation.
import os
import sys
from datetime import datetime
from datetime import date
# cryptography.fernet it is part of the cryptography library,
# it provides the Fernet symmetric-key encryption method for securely encrypting and decrypting data.
from cryptography.fernet import Fernet


# Function for creating SHA256 hash of master password
def hash_master_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


# Function to generate a secret key. This should be done only one time.
def generate_key():
    return Fernet.generate_key()


# Initialize Fernet cipher with the provided key.
def initialize_cipher(key):
    return Fernet(key)


# Function to encrypt a  password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()


# Function to decrypt a  password.
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()


# Function to register users
def register(username, master_password):
    # Encrypt the master password before storing it
    hashed_master_password = hash_master_password(master_password)
    user_data = {'username': username, 'master_password': hashed_master_password}
    file_name = 'user_data.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as file:
            json.dump(user_data, file)
            print_log(0, "Registration of user: " + username + " completed!")
    else:
        try:
            with open(file_name, 'x') as file:
                json.dump(user_data, file)
                print_log(2, "JSON File Created : " + file_name)
                print_log(0, "Registration of user: " + username + " completed!")
        except Exception as e:
            print_log(1, str(e))


# Function for logging users
def login(username, entered_password):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_master_password(entered_password)
        if entered_password_hash == stored_password_hash and username == user_data.get('username'):
            print_log(0, "Login Successful")
        else:
            print_log(1, "Invalid Login credentials.")
            sys.exit()
    except Exception as e:
        print_log(1, "User not registered" + str(e))
        sys.exit()


# Function to view saved entries.
def view_entries():
    try:
        with open('passwords.json', 'r') as data:
            view = json.load(data)
            print("\nYour Entries :\n")
            for x in view:
                print(x['Entry'])
            print('\n')
    except FileNotFoundError:
        print("\n[-] You have not saved any passwords!\n")


# Custom Function for logging into Console.
def print_log(log_type, text):
    filename = "journal.log"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        with open(filename, 'x') as file:
            file.write("[" + str(date.today()) + " " + current_time + "][INFO] LOG File Created\n")
            if log_type == 0:
                file.write("[" + str(date.today()) + " " + current_time + "][LOG] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][LOG] " + text)
            if log_type == 1:
                file.write("[" + str(date.today()) + " " + current_time + "][ERROR] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][ERROR] " + text)
            if log_type == 2:
                file.write("[" + str(date.today()) + " " + current_time + "][INFO] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][INFO] " + text)
    except FileExistsError:
        with open(filename, 'a') as file:
            if log_type == 0:
                file.write("[" + str(date.today()) + " " + current_time + "][LOG] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][LOG] " + text)
            if log_type == 1:
                file.write("[" + str(date.today()) + " " + current_time + "][ERROR] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][ERROR] " + text)
            if log_type == 2:
                file.write("[" + str(date.today()) + " " + current_time + "][INFO] " + text + "\n")
                print("[" + str(date.today()) + " " + current_time + "][INFO] " + text)


def main():
    print_log(2, "Password Manager Started!")


if __name__ == '__main__':
    main()
