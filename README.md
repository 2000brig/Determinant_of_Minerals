# Determinant_of_Minerals

I am happy to announce that I officially present the demo version of my **Determinant_of_Minerals** program to the public!  
**Determinant_of_Minerals** is a console program developed entirely in _Python 3_ and using classification methods such as _RandomTree_ and _Naive Bayes_.

The essence of the app is painfully simple: You just enter the properties of a mineral one by one, and then the program tells You which mineral You are exploring. It's like an ordinary electronic guide for determining minerals, but with powerful and modern algorithms inside. Of course, the algorithm can be wrong (the accuracy of the demo version is _about 70%_), so when You get the final result, You can see two links to authoritative sources, where You can clarify and compare all the characteristics of the mineral under study and see pictures. The program also saves previous search results to a file history.txt in the root directory of the program, so You will never lose the results of previous searchs and can always view them and use links to auxiliary resources.

# Files

- Main.py - Main project file;
- Table.csv - Minerals database;
- Main.spec - Required file for using Pyinstaller;
To use Pyinstaller correctly on the command line, use the command: pyinstaller Main.spec Main.py")

# Building .exe file from source files

In order to build an .exe file and run the application without a programming environment, You will need to download the project from GitHub, open the project in the programming environment (for example, PyCharm from JetBrains), and import the necessary libraries (described at the beginning Main.py 'import'), install the PyInstaller library via the terminal 'pip install pyinstaller'.

This completes the preparation. 
Creating an .exe file! 
Print it in the terminal 'pyinstaller Main.spec Main.py'

# Extension Table.csv rules

If You need to update the mineral database, edit the file Table.csv according to **applications for matching attributes and numeric values**:

**Appendix 1**  (Hardness)
The test version is fully compliant.
Note: Hardness 1 = digit 1 in the table

**Appendix 2**  (Color)
The color in the test version is split according to the table below:
Black - 1
Grey - 2
White - 3
Red - 4
Orange - 5
Yellow - 6
Blue - 7
Green - 8
Brown - 9

**Appendix 3** (Streak color)
The streak color in the test version is split according to the table shown:
Black - 1
Grey - 2
White - 3
Red - 4
Orange - 5
Yellow - 6
Blue - 7
Green - 8
Brown - 9

**Appendix 4** (Lustre)
The lustre in the test version is split according to the table below:
Vitreous (like a glass) - 1
Adamantine - 2
Semi-metallic - 3
Metal - 4
Waxy - 5
Dull (no lustre) - 6
Grease (resemble fat) - 7

**Appendix** **5**  (Transparency)
Transparency in the test version is split according to the table below:
Transparent - 1
Semitransparent - 2
Non-Transparent - 3
