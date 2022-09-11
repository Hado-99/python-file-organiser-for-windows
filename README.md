# File-Organiser-for-Windows
> Organise your file based on file types

>This python file allows you to select a folder in which you want to organise different file formats.
>It creates different folders into which it places your different files based on file types.
>For example you pdf files will be places in the PDF folder, Zip files in the Zip folder, etc.


## Installing / Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Python 3 Installed on Windows.
Python Libraries:
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
* What's the main functionality
* You can also do another thing
* If you get really randy, you can even do this


## Contributing

When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

These paragraphs are meant to welcome those kind souls to feel that they are
needed. You should state something like:

"If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."
