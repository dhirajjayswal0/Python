# Python
This reposatory is simply created for my python Programming practice

# section 1
Introduction

    # Lecture 1
    We are going to build 10 real word Python Programs

    # Lecture 2
    fixing error is as important as writing codes

    # Lecture 3
    10 python applications that we will build are :
    1.  Command-line-based Interactive English Thesaurus
    2.  Web Maps on the Browser
    3.  Portfolio Website
    4.  Desktop BookStore App
    5.  Feel Good Mobile App
    6.  Webcam Motion Detector and Plotter
    7.  Web scrapping Program
    8.  Data Vixualizer on the Browser
    9.  Web App with Database Backend and Email Sending
    10. Web App with Download and Upload Features

    # Lecture 4
    If you have Python questions you want to ask go to below link
    https://www.udemy.com/user/adiune/?src=sac&kw=ardit%20sulce

    If you have a question related to code go to Q&A section 
    make sure to Copy-Pate your code there along with the error messages

    # Lecture 5
    tools we will be needing are:
    1. Python installed on device
    2. IDE to write python codes

    Pyhon is cross-platform so it will work on all operating sytems
    either it be Mac, Linux or windows

    # Lecture 6
    To install Python go to python.org
    Hover over to download and download the python version it shows

    # Lecture 7
    Section 2 to 12 covers Python basics. If you you have basic Knowledge
    of Python, you can skip to section 13 and start building real world apps.

    If you are unsure whether you should skip the baics or not take assesment
    in next leacture. If you pass (i.e. get at least 60%), that means you know the
    basics, and it's safe to jump to Section 13 right away. If you are an absolute
    beginner, feel free to ignore the test and continue the lectures in the given
    order.

    # Lecture 8
    Practice test to check your Current Skiils.
    Got 63% on first attemt before going through course,
    still going through course for better knowledge
    Try taking the test once you complete first 12 sections of the course.


# Section 2
The Basics: Small Program

    # Lecture 8
    import datetime  --  Imports datetime module
    once module is imported we can use refer another object inside this module.

        datetime.datetime.now()

    here datetime module has datetime object and this object has method now()
    this code will give the current datetime.

    # lecture 9
    python interactive shell we used before is usefull for testing but
    it dosent lets you store your code for your future uses.

    so what we can do is create a file and write our python code in that file,
    and everytime we execute the file it will run our code.

    create a specific folder where you want to keep all your python files and
    come back to visual studio code and go to File > Add Folder to Workspace

    this will load the folder in side menue.
    if you have files in that folder it will show all of those and if there 
    is none simply ceate a new file with .py extemtion.
    
    Now for writing code:
    import datetime
    datetime.datetime.now()

    give the code in file and come to terminal
    now exit python session if it is running on terminal and 
    give python3 filename and hit enter

    Note : you will notice that it is not providing output as it did
           previously in the interactive shell that is beacuse we need to give
           explicit print command to print output while writing codes in file.
    
    new code:
    import datetime
    print(datetime.datetime.now())

    Now save the file and give python3 filename in terminal
    it will provide you with the date and time output.