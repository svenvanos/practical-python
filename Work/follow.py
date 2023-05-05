# follow.py

import os
import time

def follow(filename):
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line != "":
                yield line
            else:
                time.sleep(0.1) # Sleep briefly and retry if line is empty