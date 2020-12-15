# This file contains all entries to colors used in this project.

# Here you can change the color scheme.
# Choose a number between 1 and 2
colorScheme = 1

def returnColors(colorS):
    global colorScheme
    if colorS == 1:  # NORMAL
        # NOTES FOR MAKING COLOR SCHEMES:
        # format: \033[<NUMBER>m
        # 30 - black
        # 31 - red/pink
        # 32 - green
        # 33 - gold
        # 34 - blue
        # 35 - pink
        # 36 - light blue
        # 37 - white/gray
        # 90 - gray
        # 91 - red/pink
        # 92 - light green
        # 93 - yellow
        # 94 - blue/purple
        # 95 - pink
        # 96 - light blue
        # 97,98 - white
        if colorScheme == 1:  # COLOR SCHEME NR. 1
            class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                BOLD = '\033[01m'
                UNDERLINE = '\033[04m'
                RESET = '\033[00m'
        elif colorScheme == 2:  # COLOR SCHEME NR. 2
            class bcolors:
                HEADER = '\033[97m'
                OKBLUE = '\033[34m'
                OKGREEN = '\033[32m'
                WARNING = '\033[33m'
                FAIL = '\033[90m'
                BOLD = '\033[01m'
                UNDERLINE = '\033[04m'
                RESET = '\033[00m'
        else:
            print("\033[91mERROR: WRONG COLOR SCHEME SELECTED!'\033[00m")
            quit()
    elif colorS == 2:  # CLEAN
        class bcolors:
            HEADER = ''
            OKBLUE = ''
            OKGREEN = ''
            WARNING = ''
            FAIL = ''
            BOLD = ''
            UNDERLINE = ''
            RESET = ''
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