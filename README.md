![Threebe Banner](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/threebe_banner.png)

# **Introduction**

<img width="120" height="120" align="left" style="float: left; margin: 0 10px 0 0;" alt="Threebe logo" src="https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/ThreebeLogoCircle.png" />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Threebe</b> is a Libre (FOSS - Free and Open Source) tool for displaying a Hexdump /<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ Disassembly / Strings / Information from/of a (binary) file<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and (at this time) is fully written in Python3.
<br /><br />
<br /><br />
<p align="center">
    <a href="https://gitlab.com/Ernest1337/threebe">
        <img src="https://badges.pufler.dev/updated/Ernest1338/Threebe" alt="Updated Badge" />
    </a>
    <a href="https://gitlab.com/Ernest1337/threebe">
        <img src="https://badges.pufler.dev/created/Ernest1338/Threebe" alt="Created Badge" />
    </a>
</p>
<p align="center">
    <a href="https://gitlab.com/Ernest1337/threebe">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT license" />
    </a>
    <a href="https://gitlab.com/Ernest1337/threebe">
        <img src="https://img.shields.io/github/languages/code-size/Ernest1338/Threebe.svg" alt="Code Size" />
    </a>
    <a href="https://gitlab.com/Ernest1337/threebe">
        <img src="https://img.shields.io/github/repo-size/Ernest1338/Threebe.svg" alt="Repo Size" />
    </a>
</p>

# **Screenshots**

### Hexdump (-h option):

![Hexdump](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/h.png)

### Hexdump - wide (-h32 option):

![Hexdump - wide](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/h32.png)

### Disassembly (-dx86 option):

![Disassembly](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/new_dx86_1.png)

### Color Schemes:

#### Color scheme nr. 2:

![SchemeNR2](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/new_dx86_2.png)

#### Color scheme nr. 3 (Windows CMD mode):

![SchemeNR3](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/new_dx86_3.png)

### Information extracting / Patching a binary (-i, -pb options):

![Info/Patching](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/ipb.png)

### Strings extracting (-sb option):

![Strings](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/sb.png)

# **Installation**

Threebe is written from the ground up in pure Python3 (without any dependencies), so to run it, you only need to have Python3 installed on your system.
(On Windows you may need to add Python3 to your system PATH.)

Link to python website: https://www.python.org/

**Installation:**
```
git clone https://gitlab.com/Ernest1337/Threebe.git
cd Threebe
python3 Threebe.py --help
```

# **Usage**

Make sure you are in the Threebe directory before you begin. (You can also add this directory to your PATH, then you will be able to run Threebe from any place you want.)

***General usage:***
```
python3 Threebe.py [parameter(s)] [file_name/or/path/to/file]   or   ./Threebe.py [parameter(s)] [file_name/or/path/to/file]
```


**You can get a list of all possible parameters by running command:**
```
./Threebe --help
```

# **Features**

**This is a list of current features:**
* Hexdump / Hexdump at a given address
* Information about binary
* Extracting strings
* Binary patching
* x86 disassembly (partially)
* (more in the future)

# **Supported architectures**

**Disassembly:**
- x86 (not fully completed)
- (There will be more in the future)

**Hexdump, strings, pathing:**
- All architectures will "probably" work. (If you have problems with an architecture please open an issue for that.)

# **Operating systems**

Threebe is cross-platform and can be run on any operating system which allows to install python3.

# **Color Schemes**

To change **color scheme** of Threebe, edit the colorScheme variable at the top of the **Colors.py** file inside of Functions directory. (Path: Threebe/Functions/Colors.py)

Color schemes to choose from:
- 1 (Default)
- 2 (Slightly darker)
- 3 (Clean / Windows CMD mode)

# **For Windows users**

If you are using Windows CMD and experiencing weird text rendering, this is because CMD doesn't support using ANSI escape codes which i'm using to make output colorful. To solve this issue you need to set color scheme (see: Color Schemes section) to a value of 3 (windows cmd mode).

# **Links**

- Gitlab repo: https://gitlab.com/Ernest1337/threebe
- Github mirror: https://github.com/Ernest1338/Threebe
- Issues/Bug tracker/Feature request: Github issues (https://github.com/Ernest1338/Threebe/issues) or Gitlab issues (https://gitlab.com/Ernest1337/threebe/-/issues)

# **Contribution**

If you want to contribute to this project, feel free to do that.
Any help is much appreciated.