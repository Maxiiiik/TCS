import os
import time

def create_file():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        filename = f"screen/time_{current_time}.txt"
        with open(filename, "w") as file:
            file.write(current_time)
        time.sleep(10)

create_file()
