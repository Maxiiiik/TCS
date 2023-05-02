import os
import time

def check_directory():
    while True:
        files = os.listdir("screen/")
        if files:
            for file in files:
                with open(os.path.join("screen/", file), "r") as f:
                    content = f.read()
                print(f"File: {file}, Content: {content}")
        time.sleep(5)

check_directory()

