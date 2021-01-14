# Python Notes
This reposatory is simply created for my python Programming practice and 
the README file consists of every notes that i made along the Course.

# section 1 : Introduction


    # Lecture 1 : What to expect from the course
    We are going to build 10 real word Python Programs

    
    # Lecture 2 : What not to expect from the Course
    fixing error is as important as writing codes so the
    errors are not removed from the lectures.

    
    # Lecture 3 : Preview of the 10 Apps
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

    
    # Lecture 4 : How to contact Instructor
    If you have Python questions you want to ask go to below link
    https://www.udemy.com/user/adiune/?src=sac&kw=ardit%20sulce

    If you have a question related to code go to Q&A section 
    make sure to Copy-Pate your code there along with the error messages

    
    # Lecture 5 : The tools you need
    tools we will be needing are:
    1. Python installed on device
    2. IDE to write python codes

    Pyhon is cross-platform so it will work on all operating sytems
    either it be Mac, Linux or windows

    
    # Lecture 6 : Installing Python and the IDE
    To install Python go to python.org
    Hover over to download and download the python version it shows

    
    # Lecture 7 : Important Note
    Section 2 to 12 covers Python basics. If you you have basic Knowledge
    of Python, you can skip to section 13 and start building real world apps.

    If you are unsure whether you should skip the baics or not take assesment
    in next leacture. If you pass (i.e. get at least 60%), that means you know the
    basics, and it's safe to jump to Section 13 right away. If you are an absolute
    beginner, feel free to ignore the test and continue the lectures in the given
    order.

    
    # Practice Test 1 : Check your Current skills
    Practice test to check your Current Skiils.
    Got 63% on first attemt before going through course,
    still going through course for better knowledge
    Try taking the test once you complete first 12 sections of the course.



# Section 2 : The Basics: Small Program
    

    # Lecture 8 : First Python code
    import datetime  --  Imports datetime module
    once module is imported we can use refer another object inside this module.

        datetime.datetime.now()

    here datetime module has datetime object and this object has method now()
    this code will give the current datetime.

    
    # Lecture 9 : First Python program
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

    Output:
    2021-01-13 14:46:50.327237

    Now save the file and give python3 filename in terminal
    it will provide you with the date and time output.

    Now looking at the output it gives the result but to make it look better:
    import datetime
    print("The date and Time is :", datetime.datetime.now())

    Output:
    The date and Time is : 2021-01-13 15:31:00.540913

    
    # Lecture 10 : FAQs

    If, during this section, you encounter an error when you try to execute Python,
    know that it may be due to two common reasons whose solutions are given below.
    If you have an issue that is not included below, feel free to raise a question in the Q&A.

    Question 1. When I run python basics.py on Windows, I get the error:

    'python' is not recognized as an internal or external command operable program or batch file

    Solution 1: If you are using Visual Studio Code, try restarting Visual Studio Code 
    and then try running python basics.py again. If it doesn't work, go to Solution 2 below.

    Solution 2: Try uninstalling Python and then install it again,
    but this time make sure that the option Add Python to Path is 
    marked as checked during the installation process.


    # Lecture 11 : Summary
    
    Here is a summary of what you learned in this section:

    Python 3 and the Visual Studio Code IDE were used in this course, but you can use any IDE.

    The Python interactive shell (shown with >>>) is a quick way to execute Python code to see how it works.

    Python programs are written in .py files.

    You can make a program that shows the current date and time using these lines of code:
    import datetime
    print("The date and time is ", datetime.datetime.now())



# section 3 : The Basics : Data Types


    # Lecture 12 : Variables

    Variables are names that we can create to store values in Python.
    it provides us with more freedom to manipute the date.

    code :
    import datetime
    time = datetime.datetime.now()
    print(time)

    name = "Dhiraj"
    text = "Roll no:"
    roll = 63
    print(name, text, roll)

    Output :
    2021-01-13 17:29:00.152403
    Dhiraj Roll no : 63

    Note : Here print is the function and with it we can use multiple arguments.
           Arguments in the above code are time, name, text and roll.
    

    # Coding Excercise 1 :

    Assignment:

    Assign a value to x in the first line,
    and print out the variable value in the second.

    Solution:

    x = 10
    print(x)

    
    # Coding Excercise 2 :

    Assignment:

    Assign some values to variables x, y, and z and
    then print the values using print function.

    Solution:

    x=10
    y=20
    z=30
    print(x, y, z)


    # Lecture 13 : Simple types : Integers, Strings, and Floats

    Computers are dumb so we have to tell them what type of data we are working with.

    in most of the other programming languages we have explicit declaration, 
    but python works with implicit declaration which means:
    if number is without quotes and decimal it is intiger.
    if number is without quotes and having decimal it is float.
    if anything is under quotes then it is string

    To check the DataType of a value or a vlue stored in variable we use type function
    with value or a variable inside ().

    x = 10
    y = "20"
    z = 10.1

    sum1 = x + x
    sum2 = y + y

    print(sum1, sum2)
    print(type(x), type(y), type(z))

    Output:
    20 2020
    <class 'int'> <class 'str'> <class 'float'>

    Note : In above example as we can see x is int, y is str and z is float.


    # Coding Exercise 3 :

    Assignment:

    Create three variables mood, strength, and rank and assign string to mood,
    a float to strength, and an integer to rank.

    Solution:

    mood = "Happy"
    strength = 10.5
    rank = 6


    # Coding Exercise 4 :

    Assignment:

    Assign numbers to x, y and z. Calculate the sum of x, y and z in s.
    And finally print out the value of s.

    Solution:

    x = 1
    y = 2
    z = 3
    s = (x+y+z)
    print(s)


    # Lecture 14 : List Types

    Besides simple data types we also have compound data types and
    the list is most popular one.

    In a list we can store multiple objects.

    List are store inside [ ] where each element is seperated by a comma.


    # Lecture 15 : Ranges

    You can create a list of numbers automatically using a range. 
    
    For example:        list(range(1, 10))
    That will output:   [1, 2, 3, 4, 5, 6, 7, 8, 9]

    As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. The generated list always runs up to one number before the upper number. In our example, it goes up to 9 since the upper number is 10.

    You can also specify a step as a third argument:

    For example: list(range(1, 10, 2))
    That will output: [1, 3, 5, 7, 9]

    So, the count happens every two items starting from 1 and ending at 9.


    # Coding Excercise 5 :

    Assignment:

    Assign a list to variable temperatures.
    The list should contain three items, a float, an integer, and a string.

    Solution:

    temperatures = [ 1, 2.3, "hello"]


    # Coding Excercise 6 :

    Assignment:

    Assign a list to variable rainfall.
    The list should contain four items, a float, an integer, a string and a list.

    Solution:

    rainfall = [1.1, 2, "hello", [1, 2, 3, 4]]


    # Lecture 16 : Type Attributes using dir( ) and help( )

    dir(type) is a function which will give you all the things you can do
    with a specific type.

    help(type.attribute) will give all the details of the attribute.

    q to quit and go back to shell.


    dir(int) will give us below methods:

    as_integer_ratio : Returns pair of integers, whose ratio is equal to original int
    bit_length : Number of bits necessary to represent self in binary
    conjugate : Returns self, the complex conjugate of any int
    denominator : the denominator of a rational number in lowest terms
    from_bytes : Return the integer represented by the given array of bytes
    imag : the imaginary part of a complex number
    numerator : the numerator of a rational number in lowest terms
    real : the real part of a complex number
    to_bytes : Return an array of bytes representing an integer.


    dir(float) will give us below methods:

    as_integer_ratio : Returns pair of integers, whose ratio is equal to original int
    conjugate : Returns self, the complex conjugate of any int
    fromhex : Create a floating-point number from a hexadecimal string
    hex : Return a hexadecimal representation of a floating-point number.
    imag : the imaginary part of a complex number
    is_integer : Return True if the float is an integer.
    real : the real part of a complex number


    dir(str) will give us below methods:

    capitalize : Return a capitalized version of the string
    casefold : Return a version of the string suitable for caseless comparisons
    center : Return a centered string of length width
    count : Return the number of non-overlapping occurrences of substring
    encode : Encode the string using the codec registered for encoding
    endswith : Return True if S ends with the specified suffix, False otherwise
    expandtabs : Return a copy where all tab characters are expanded using spaces
    find : Return the lowest index in S where substring sub is found
    format : Return a formatted version of S, using substitutions from args and kwargs
    format_map : Return a formatted version of S, using substitutions from mapping
    index : Return the lowest index in S where substring sub is found
    isalnum : Return True if the string is an alpha-numeric string, False otherwise
    isalpha : Return True if the string is an alphabetic string, False otherwise
    isascii : Return True if all characters in the string are ASCII, False otherwise
    isdecimal : Return True if the string is a decimal string, False otherwise
    isdigit : Return True if the string is a digit string, False otherwise
    isidentifier : Return True if the string is a valid Python identifier else False
    islower : Return True if the string is a lowercase string, False otherwise
    isnumeric : Return True if the string is a numeric string, False otherwise
    isprintable : Return True if the string is printable, False otherwise
    isspace : Return True if the string is a whitespace string, False otherwise
    istitle : Return True if the string is a title-cased string, False otherwise
    isupper : Return True if the string is an uppercase string, False otherwise
    join : Concatenate any number of strings
    ljust : Return a left-justified string of length width
    lower : Return a copy of the string converted to lowercase
    lstrip : Return a copy of the string with leading whitespace removed
    maketrans : Return a translation table usable for str.translate()
    partition : Partition the string into three parts using the given separator
    removeprefix : Return a str with the given prefix string removed if present
    removesuffix : Return a str with the given suffix string removed if present
    replace : Return a copy with all occurrences of substring old replaced by new
    rfind : Return the highest index in S where substring sub is found
    rindex : Return the highest index in S where substring sub is found
    rjust : Return a right-justified string of length width
    rpartition : Partition the string into three parts using the given separator
    rsplit :  Return a list of the words in the string, using sep as the delimiter string
    rstrip : Return a copy of the string with trailing whitespace removed
    split : Return a list of the words in the string, using sep as the delimiter string
    splitlines : Return a list of the lines in the string, breaking at line boundaries
    startswith : Return True if S starts with the specified prefix, False otherwise
    strip : Return a copy of the string with leading and trailing whitespace removed
    swapcase : Convert uppercase characters to lowercase and vise-versa
    title : Return a version of the string where each word is titlecased
    translate : Replace each character in the string using the given translation table
    upper : Return a copy of the string converted to uppercase
    zfill : Pad a numeric string with zeros on left, to fill a field of given width.


    dir(list) will give us below methods:

    append : Append object to the end of the list.
    clear: Remove all items from list.
    copy: Return a shallow copy of the list.
    count: Return number of occurrences of value.
    extend: Extend list by appending elements from the iterable.
    index: Return first index of value.
    insert: Insert object before index.
    pop: Remove and return item at index (default last).
    remove: Remove first occurrence of value.
    reverse: (self, /)  Reverse *IN PLACE*.
    sort: Sort the list in ascending order and return None.

    
    dir(tuple) will give us below methods:

    count : Return number of occurrences of value
    index : Return first index of value