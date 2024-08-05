import os

def remove(path):
    if os.path.isfile(path):
        os.remove(path)