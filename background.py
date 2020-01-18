import ctypes
import os
from random import randrange

import config

IMAGE_FOLDER = config.OUTPUT_FOLDER

def main():
    photos = os.listdir(IMAGE_FOLDER)
    photos = [os.path.join(IMAGE_FOLDER, photo) for photo in photos]
    file = photos[randrange(len(photos))]
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file, 3)
    return

if __name__ == '__main__':
    # main()
    pass
