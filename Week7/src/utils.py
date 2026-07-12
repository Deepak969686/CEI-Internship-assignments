import os


def ensure_directory(folder):
    """
    Create directory if it doesn't exist.
    """

    if not os.path.exists(folder):
        os.makedirs(folder)