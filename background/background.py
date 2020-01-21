import ctypes
import os
from random import choice

from . import utils

SPI_SETDESKWALLPAPER = 20


class Background():
    def __init__(self):
        self.filetypes = ['jpg']
        self.verbose = True
        return

    def change(self, file):
        """
        Change desktop wallpaper to image located at file.
        Parameters
        ----------
        file : str
            Full file path (not relative) to image file.
        """

        if os.path.isabs(file) is False:
            file = str(os.path.join(os.getcwd(), file))

        # Check that file exists and is absolute path
        check_passed = self._check_file(file)
        if check_passed is False:
            return False

        self._change_background(file)
        return True

    def random_from_folder(self, folder):
        """
        Change desktop wallpaper to an image selected at random from files
        in folder.
        
        Parameters
        ----------
        folder : str
            Full path to folder (not relative) to image file.
        """
        self._print('\nSelecting random file from folder:')
        self._print(folder)
        
        # Get files in folder
        files = utils.files_in_folder(folder, join_folder=True)

        self._print('Files found: ', len(files))
        
        # Select random from list and change background
        self.random_from_list(files)
        return

    def random_from_list(self, files):
        """
        Change desktop wallpaper to an image selected at random from list of
        files.
        
        Parameters
        ----------
        files : list
            List of str full file paths to images files.
        """
        self._print('\nSelecting random file from list:')
        self._print('Files in list: ', len(files))
        
        temp = []
        for file in files:
            output = ''
            if file.lower().endswith('.jpg') is False:
                continue
            if os.path.isabs(file) is False:
                output = os.path.join(os.getcwd(), file)
            temp.append(output)
        assert temp
        
        selection = choice(temp)
        self._print('File selected: ', os.path.basename(selection))
        self.change(selection)
        return

    def _check_file(self, file):
        self._print('\nFile checks')
        
        if not isinstance(file, str):
            print('file must be a string')
            return False
        else:
            self._print('File is string')

        if os.path.isfile(file) is False:
            print('file does not exist', file)
            return False
        else:
            self._print('File exists')

        if os.path.isabs(file) is False:
            print('file path must be absolute not relative', file)
            return False
        else:
            self._print('File path is absolute')

        assert file.lower().endswith('.jpg')
        
        return True

    def _change_background(self, file):
        """
        Parameters
        ----------
        file : str
            Full file path (not relative) to image file.
        """
        self._print('\nChanging background...', end='')
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,
                                                   file, 3)
        self._print('DONE')
        print('original called')
        return

    def _print(self, *args, **kwargs):
        if self.verbose == True:
            print(*args, **kwargs)
        return
