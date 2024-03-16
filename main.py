from datetime import datetime
from datetime import date


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
