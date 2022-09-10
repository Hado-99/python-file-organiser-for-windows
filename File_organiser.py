from genericpath import exists
from posixpath import splitext
from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory

import datetime
import os
os.environ['SETUPTOOLS_USE_DISTUTILS'] = 'stdlib'
import setuptools
import shutil
import time

# request user to select the source directory

source_dir = askdirectory(title='Select Folder') # shows dialog box and return the path
#print(f"{os.path.join(source_dir,'Excel')}")
if source_dir=='':
    exit()


#Check if folders exist and create if they do not

destination_dir_excel = os.path.join(source_dir,'Excel')
if not os.path.exists(destination_dir_excel):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Excel folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_excel)
    else:
        exit()

destination_dir_word = os.path.join(source_dir, 'Word_Other')
if not os.path.exists(destination_dir_word):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Word folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_word)
    else:
        exit()

destination_dir_pdf = os.path.join(source_dir, 'PDF')
if not os.path.exists(destination_dir_pdf):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the PDF folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_pdf)
    else:
        exit()

destination_dir_img = os.path.join(source_dir, 'Images')
if not os.path.exists(destination_dir_img):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Images folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_img)
    else:
        exit()

destination_dir_software = os.path.join(source_dir, 'Software')
if not os.path.exists(destination_dir_software):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Software folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_software)
    else:
        exit()

destination_dir_video = os.path.join(source_dir, 'Video')
if not os.path.exists(destination_dir_video):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Video folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_video)
    else:
        exit()

destination_dir_zip = os.path.join(source_dir,'Zip')
if not os.path.exists(destination_dir_zip):
    create_or_not=messagebox.askquestion('Create folder or Not','Do you want to create the Zip folder?')
    if create_or_not=='yes':
        os.makedirs(destination_dir_zip)
    else:
        exit()


# file types

doc_types_excel=('.xlsx', '.xls','.ods')

doc_types_word=('.doc','.docx','.odt', '.txt', '.ppt', '.pptx')

doc_types_pdf=('.pdf')

img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')

software_types = ('.exe', '.pkg', '.dmg')

video_types = ('.mp4', '.mkv', '.mpg', '.mpeg', '.mov', '.avi')

zip_types= ('.zip', '.7z')

#list of files in source directory

files=[i for i in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir,i))]
#print('Files to move: ',files)

#move files to respective directories based on file extension

for f in files:

    #Excel docs
    if os.path.join(source_dir, f).endswith(doc_types_excel):
        #print("Excel option: ", f )
        filename, extension = os.path.splitext (f)
                
        if os.path.exists(os.path.join(destination_dir_excel, f)):
            date_time= datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
            #print(f"{filename}_{date_time}{extension}")
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_excel, f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_excel))

    #Word and other docs
    elif os.path.join(source_dir, f).endswith(doc_types_word):
        #print("Word files: ", f )
        filename, extension = os.path.splitext (f)

        if os.path.exists(os.path.join(destination_dir_word, f)):
            date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_word, f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_word)

    #PDF docs
    elif os.path.join(source_dir, f).endswith(doc_types_pdf):
        #print("PDF files: ", f )
        filename, extension = os.path.splitext (f)

        if os.path.exists(os.path.join(destination_dir_pdf, f)):
            date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_pdf, f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_pdf)

    #Image files
    elif os.path.join(source_dir, f).endswith(img_types):
        ##print("Image files: ", f )
        filename, extension = os.path.splitext (f)

        if os.path.exists(os.path.join(destination_dir_img, f)):
            date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_img, f"{filename}_({date_time}{extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_img)

    #Software files
    elif os.path.join(source_dir, f).endswith(software_types):
        
        filename, extension = splitext (f)

        if exists(os.path.join(destination_dir_software, f)):
                date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_software, f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_software)

    #Video files
    elif os.path.join(source_dir, f).endswith(video_types):
        
        filename, extension = splitext (f)

        if exists(os.path.join(destination_dir_video, f)):
                date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_video, f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_video)

    #Zip files
    elif os.path.join(source_dir, f).endswith(zip_types):
        
        filename, extension = splitext (f)

        if exists(os.path.join(destination_dir_zip, f)):
                date_time=datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir_zip,f"{filename}_({date_time}){extension}"))
        else:
            shutil.move(os.path.join(source_dir, f), destination_dir_zip)


