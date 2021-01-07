# **Introduction**

<img width="120" height="120" align="left" style="float: left; margin: 0 10px 0 0;" alt="Threebe logo" src="https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/ThreebeLogoCircle.png" />
<br /><br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Threebe</b> is a Libre (FOSS - Free and Open Source) tool for displaying a Hexdump / Disassembly / Strings / <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ Information from/of a (binary) file and (at this time) is fully written in Python3.
<br /><br />
<br /><br />
![Updated Badge](https://badges.pufler.dev/updated/Ernest1338/Threebe) ![Created Badge](https://badges.pufler.dev/created/Ernest1338/Threebe) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg) ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg) ![Code Size](https://img.shields.io/github/languages/code-size/Ernest1338/Threebe.svg) ![Repo Size](https://img.shields.io/github/repo-size/Ernest1338/Threebe.svg)

# **Screenshots**

### Hexdump:

![Hexdump](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/threebe.png)

### Disassembly:

![Disassembly](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/threebeDisassembly.png)

# **Installation**

Threebe is written in Python3, so to run it, you need to have Python3 installed on your system. 
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

# **Color Schemes**

To change **color scheme** of Threebe, edit the colorScheme variable at the top of the **Colors.py** file inside of Functions directory. (Path: Threebe/Functions/Colors.py)

Color schemes to choose from:
- 1 (Default)
- 2 (Slightly darker)
- 3 (Clean / Windows CMD mode)

# **For Windows users**

If you are using Windows CMD and experiencing weird text rendering, this is because CMD doesn't support using ANSI escape codes which i'm using to make output colorful. To solve this issue you need to set color scheme (see: Color Schemes section) to a value of 3 (windows cmd mode).

# **Links**

- Github mirror: https://github.com/Ernest1338/Threebe
- Issues/Bug tracker/Feature request: https://gitlab.com/Ernest1337/threebe/-/issues

# **Operating systems**

Threebe is cross-platform and can be run on any operating system which allows to install python3.

# **Supported architectures**

**Disassembly:**
- x86 (not fully completed)
- (There will be more in the future)

**Hexdump, strings, pathing:**
- All architectures will "probably" work. (If you have problems with an architecture please open an issue for that.)

# **Features**

**This is a list of current features:**
* Hexdump / Hexdump at a given address
* Information about binary
* Extracting strings
* x86 disassembly (partially)
* Binary patching
* (more in the future)

# **Contribution**

If you want to contribute to this project, feel free to do that.
Any help is much appreciated.