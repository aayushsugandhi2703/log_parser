import os

if os.path.exists("log_file") and os.path.isdir("log_file"):
    with open("log_file/logs.txt", "r") as file:
        for line in file:
            print(line, end="")