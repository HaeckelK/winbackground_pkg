import ctypes
import os
from random import randrange


# IMAGE_FOLDER = config.OUTPUT_FOLDER

SPI_SETDESKWALLPAPER = 20

class Background():
    def __init__(self):
        self.filetypes = ['jpg']
        return

    def change(self, file):
        """
        Change desktop wallpaper to image located at file.
        
        Parameters
        ----------
        file : str
            Full file path (not relative) to image file.
        """

        # TODO : insist on type of image
        
        # Check that file exists and is absolute path
        check_passed = self._check_file(file)
        if check_passed == False:
            return False

        self._change_background(file)
        return True

    def _check_file(self, file):
        if not isinstance(file, str):
            print('file must be a string')
            return False

        if os.path.isfile(file) is False:
            print('file does not exist', file)
            return False

        if os.path.isabs(file) is False:
            print('file path must be absolute not relative', file)
            return False

        return True

    def _change_background(self, file):
        """
        Parameters
        ----------
        file : str
            Full file path (not relative) to image file.
        """
        """
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,
                                                   file, 0)
        """
        print('original called')
        return

def change_function(file):
    """
    Parameters
    ----------
    file : str
        Full file path (not relative) to image file.
    """
    # TODO File must be full file path?
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                                        0, file, 0)
    if not result:
        print('File doesnt exist')
    return result

def main():
    photos = os.listdir(IMAGE_FOLDER)
    photos = [os.path.join(IMAGE_FOLDER, photo) for photo in photos]
    file = photos[randrange(len(photos))]
    
    return