# hashlib is a library that provides secure hash functions,
# including SHA-256, for creating hash values from data,
# often used for password hashing and data integrity verification.
import hashlib
from datetime import datetime
from datetime import date


# Function for creating SHA256 hash of master password
def hash_master_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


# Custom Function for logging into Console.
# TODO: Add logging into logfile
def print_log(log_type, text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if log_type == 0:
        print("[" + str(date.today()) + " " + current_time + "][LOG] " + text)
    if log_type == 1:
        print("[" + str(date.today()) + " " + current_time + "][ERROR] " + text)
    if log_type == 2:
        print("[" + str(date.today()) + " " + current_time + "][INFO] " + text)


def main():
    print_log(2, "Password Manager Started!")


if __name__ == '__main__':
    main()
