# **Introduction**

**Threebe** is a tool for displaying a Hexdump / Disassembly / Strings / Information from/of a (binary) file and (at this time) is fully written in Python3.

# **Screenshots**

![](https://raw.githubusercontent.com/Ernest1338/test_threebe1/master/threebe.png)

# **Installation**

Threebe is a python3 program so to run it, you need to have python3 installed on your system.
On Windows you need to add python3 to your system PATH.

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