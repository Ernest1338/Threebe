# This file contains all entries to colors used in this project.

# Here you can change the color scheme.
# Choose a number between 1 and 3
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
        # 90 - gray         # colors 90-97 are a lighter version of colors 30-37
        # 91 - red/pink
        # 92 - light green
        # 93 - yellow
        # 94 - blue/purple
        # 95 - pink
        # 96 - light blue
        # 97 - white
        if colorScheme == 1:  # COLOR SCHEME NR. 1 - DEFAULT
            class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                BOLD = '\033[01m'
                UNDERLINE = '\033[04m'
                RESET = '\033[00m'
        elif colorScheme == 2:  # COLOR SCHEME NR. 2 - SLIGHTLY DARKER
            class bcolors:
                HEADER = '\033[97m'
                OKBLUE = '\033[34m'
                OKGREEN = '\033[32m'
                WARNING = '\033[33m'
                FAIL = '\033[90m'
                BOLD = '\033[01m'
                UNDERLINE = '\033[04m'
                RESET = '\033[00m'
        elif colorScheme == 3:  # COLOR SCHEME NR. 3 - CLEAN - WINDOWS CMD MODE
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
    elif colorS == 3:  # CLEAN - RESET
        class bcolors:
            HEADER = '\033[91m'
            OKBLUE = '\033[91m'
            OKGREEN = '\033[91m'
            WARNING = '\033[91m'
            FAIL = '\033[91m'
            BOLD = '\033[91m'
            UNDERLINE = '\033[91m'
            RESET = '\033[91m'
    else:
        print("\033[91mERROR: WRONG COLOR SCHEME SELECTED! - DEV'\033[00m")
        quit()
    return bcolors
