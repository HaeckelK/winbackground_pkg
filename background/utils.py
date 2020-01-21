"""
Helper functions
"""
import os

def files_in_folder(folder):
    """
    Return all files in folder.
    """
    contents = os.listdir(folder)
    files = [x for x in contents if os.path.isfile(join(folder, x))]
    return files
