# This file contains all entries to colors used in this project.

colorScheme = 1

def returnColors(colorScheme):
    if colorScheme == 1:  # NORMAL
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            BOLD = '\033[01m'
            UNDERLINE = '\033[04m'
            RESET = '\033[00m'
    elif colorScheme == 2:  # CLEAN
        class bcolors:
            HEADER = '\033[00m'
            OKBLUE = '\033[00m'
            OKGREEN = '\033[00m'
            WARNING = '\033[00m'
            FAIL = '\033[00m'
            BOLD = '\033[00m'
            UNDERLINE = '\033[00m'
            RESET = '\033[00m'
    else:
        class bcolors:
            HEADER = '\033[91m'
            OKBLUE = '\033[91m'
            OKGREEN = '\033[91m'
            WARNING = '\033[91m'
            FAIL = '\033[91m'
            BOLD = '\033[91m'
            UNDERLINE = '\033[91m'
            RESET = '\033[91m'
    return bcolors