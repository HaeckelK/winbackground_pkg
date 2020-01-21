"""
Helper functions
"""
import os
from os.path import join

def files_in_folder(folder, join_folder=False):
    """
    Return all files in folder.
    """
    contents = os.listdir(folder)
    files = [x for x in contents if os.path.isfile(join(folder, x))]
    if join_folder == True:
        files = list(map(lambda x: join(folder, x), files))
    return files
