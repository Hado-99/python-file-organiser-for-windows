# File-Organiser-for-Windows
> Organise your files based on file types

>This python file allows you to select a folder in which you want to organise different file formats.
>It creates different folders into which it places your different files based on file types.
>For example you pdf files will be places in the PDF folder, Zip files in the Zip folder, etc.


## Installing / Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre-requisites
Python 3 Installed on Windows <br />
Python Libraries:<br />
exists
setuptools
shutil
splitext
tkinter
time

When running the script via the terminal you can use the following command (change the FOLDER PATH to where your file is):

>python -u "[FOLDER PATH]\File_organiser.py"

A window will popup where you can select the folder that you want to run the file organiser on.

Select the folder and click the "Select Folder" button.

The program will then create the necessary folders i.e. Excel, PDF, Images, Software, Video, Word_Other, Zip within the selected directory.

If a folder does not exist you will receive a prompt on whether you want the folder created. NOTE: If you select that you do not want to create the folder then the program will break out of the code.

Here you should say what actually happens when you execute the code above.

### Demo

https://user-images.githubusercontent.com/113255461/189553511-e571d141-fc77-4f50-ab61-c8cee2dde21c.mp4



## Features

What's all the bells and whistles this project can perform?
* Creating folders based on different file types
* Sorting files into folders based on file type
* Allows you to select the folder where the file organising should take place in


## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

You are welcome to contribute to this code. 

Some things I would consider adding functionality for:
- making this compatible with Mac and Linux;
- ability to listen to a folder and when files are added then those files get moved to the applicable file type folder
