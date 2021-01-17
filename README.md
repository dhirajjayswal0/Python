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


    dir(dict) will give us below methods:

    clear : D.clear() -> None.  Remove all items from D.
    copy : D.copy() -> a shallow copy of D
    fromkeys : Create a new dictionary with keys from iterable and values set to value
    get : Return the value for key if key is in the dictionary, else default
    items : D.items() -> a set-like object providing a view on D's items
    keys : D.keys() -> a set-like object providing a view on D's keys
    pop : D.pop(k[,d]) -> v, remove specified key and return the corresponding value
    popitem : Remove and return a (key, value) pair as a 2-tuple.
    setdefault : Insert key with a value of default if key is not in the dictionary
    update : D.update([E, ]**F) -> None.  Update D from dict/iterable E and F
    values : D.values() -> an object providing a view on D's values


    # Lecture 17 : Fun Fact

    Python got his name not from the snake, but from Monty Python's Flying Circus,
    a favorite comedy series of Guido van Rossum, the creator of Python.


    # Lecture 18 : How to find out what code you need

    Methods needs dot(.) nation to be used, but functions dosent needs it.
    for example :

    function : print("hello)
    method : "hello".upper

    # lecture 19 : Bonus Steps of Learning Python

    Always remember learning Python is about three things :
    Syntax
    Data Structure
    Algorithm


    # Coding Exercise 7 :

    Assignment:

    write a script which prints the max value from a list

    Solution:

    student_grades = [9.1, 8.8, 7.5]
    max_value = max(student_grades)
    print(max_value)


    # Coding Exercise 8 :

    Assignment:

    write a script to count number of occurence of 10.0 in the list

    Solution:

    student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
    print(student_grades.count(10.0))


    # Coding Exercise 9 :

    Assignment:

    write a script to convert string to lowercase text.

    Solution:

    username = "Python3"
    print(username.lower())


    # Lecture 20 : Dictionary Types

    when we have array of items with some identity the dictionary data types are used.
    For dictionary data types {"Key":value, "key":value} are used.


    # Lecture 21 : Fun Fact

    Did you know that Python was first released in 1991?
    Python 2 was released in 2000, and Python 3 (the current version) in 2008.


    # Coding Exercise 10 :

    Assignment:

    Assign a dictionary to variable day_temperatures.
    The dictionary should contain three keys, "morning", "noon", and "evening"
    Each key should have a float as value.

    Solution:

    day_temperatures = {"morning":6.5, "evening":7.6, "noon":8.6}


    # Lecture 22 : Tuple Types :

    Tuple is just like a list but with ( ) .
    Tuples are a bit faster as compared to list.
    Tuples are immutable while list are mutable.
    
    i.e : We can add or delete values from a list but not from tuple.
          as a reference append method will work with list but not with tuple.


    # Coding Exercise 11 :

    Assignment:

    Create a color_codes variable and assign a tuple to it.
    The tuple should contain three tuples as items.

    Solution:

    color_codes = ((1,2,3),(4,5,6),(7,8,9))


    # Coding Exercise 12 :

    Assignment:

    Assign a dictionary to variable day_temperatures.
    The dictionary should contain three keys: "morning","noon", and "evening"
    and each key should contain three float values.

    Solution:

    day_temperatures = {"morning":(1.1,2.2,3.3),"noon":(4.4,5.5,6.6),
                       "evening":(7.7,8.8,9.9)}
    

    # Lecture 23 : How to use datatypes in real world

    All these datatypes are rarely created manually in the program file,
    rather we usally import the data from a file and implement the datatype over it.


    # Lecture 24 : Fun Facts
    
    Python is mainly used for automation purposes, web apps, and data science.
    Many big companies, like Instagram, Facebook, and Amazon, use Python 
    in different parts of their products. For example, Facebook uses Python 
    to process images.


    # Lecture 25 : Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help

    In this section, you learned that:

    Integers are for representing whole numbers:
    rank = 10
    eggs = 12
    people = 3

    Floats represent continuous values:
    temperature = 10.2
    rainfall = 5.98
    elevation = 1031.88

    Strings represent any text:
    message = "Welcome"
    name = "John"
    serial = "R001991981SW"

    Lists represent arrays of values that may change during the course of the program:
    members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
    pixel_values = [252, 251, 251, 253, 250, 248, 247]

    Dictionaries represent pairs of keys and values:
    phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
    volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

    Keys of a dictionary can be extracted with:
    phone_numbers.keys()

    Values of a dictionary can be extracted with:
    phone_numbers.values()

    Tuples represent arrays of values that are not to be changed during the course of the program:
    vowels = ('a', 'e', 'i', 'o', 'u')
    one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    To find out what attributes a type has:
    dir(str)
    dir(list)
    dir(dict)

    To find out what Python builtin functions there are:
    dir(__builtins__)

    Documentation for a Python command can be found with:
    help(str)
    help(str.replace)
    help(dict.values)



# Section 4 : The Basics: Operations with Data Types


    # Lecture 26 : Python Shell and Terminal Tip

    Terminal :

    clear command clears the terminal.


    Python shell :

    ctr + l  will clear the python shell.
    exit() command will exit the python shell and return to commnad line
    python3 command will get you yo python shell from command line


    # Lecture 27 : List Reminder

    In the next lecture, you will learn more about lists. Here's a reminder of how a list looks like in case you forgot:

    search_engines = ["google", "bing", "duck duck go"]

    That's a list made of three values, which in this example happen to be all strings.


    # lecture 28 : More operations with Lists

    while using dir(type) function most of the outputs which begins and ends with __ are used by python itself and are rarely used by us.


    Coding excercise 13 :

    Assignment :

    Append the value of current to the end of the list seconds Please use the
    list.append() method to do that.

    Solution : 

    seconds = [1.2323442655, 1.4534345567, 1.023458894]
    current = 1.10001399445
    seconds.append(current)


    Coding excercise 14 :

    Assignment:

    remove item 1.4534345567 from seconds

    Solution :

    seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
    seconds.remove(index(1))


    Coding excercise 15 :

    Assignment:

    remove item 1.4534345567, 1.023458894, 1.10001399445 from seconds

    Solution :

    seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
    seconds.remove(1.4534345567)
    seconds.remove(1.023458894)
    seconds.remove(1.10001399445)


    # lecture 29 : Accessing List Items

    to acess an item from a list we use __getitem__ function.
    but instead of using it we can also give [index of item] to get that item.

    for example :

    monday_temperatures = [9.1, 7.2, 8.5]
    monday_temperatures.__getiteam__(1)
    monday_temperatures[1]

    Outputs :

    for both methods we will get same output that is 7.2


    # Coding excercise 16 :

    Assignment :

    Complete the script so that it prints out the 3rd iteam of the list serials.

    Solution :

    serials = ["RH80810A", "AA899819A", "XYSA9099400",
              "OOP8988459", "EEO8904882", "KOC9889482"]
    print(serials[2])


    # Coding excercise 17 :

    Assignment :

    Complete the script so that it prints out the 1st, the 3rd and the 6th 
    iteam of the list serials.

    Solution :

    serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459",
    "EEO8904882", "KOC9889482"]
    print(serials[0], serials[2], serials[5])


    # Coding excercise 18 :

    Assignment :

    Append the first item of weekend to workdays.

    Solution :

    workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    weekend = ["Sat", "Sun"]
    workdays.append(weekend[0])

    # Lecture 30 : Acessing List Slices

    We can also acess a slice of the given list.
    we will acess the list slice by using [start indes:ending index + 1]

    For example :

    monday_temperatures = [9.1, 8.8, 7.5]
    print(monday_temperatures[0:2])

    will give us output of [9.1, 8.8]

    Also to access elements from the beging or till end we can leave empty space,
    instead of giving vlue.

    For example :

    monday_temperatures = [9.1, 8.8, 7.5]
    print(monday_temperatures[:2])
    print(monday_temperatures[1:])

    Here in above exaple the first function will give us output 9.1, 8.8
    and the second function will give us 8.8, 7.5


    # Lecture 31 : Accessing Items and Slices with Negative Indexes

    every index in Python has two indexes one positive that starts from begining
    and one negative that begings from the end.

    For example :

    monday_temperatures = [9.1, 8.8, 7.5]
    print(monday_temperatures[-3:-1])

    will give us output of [9.1, 8.8]

    Also to access elements from the beging or till end we can leave empty space,
    instead of giving vlue.

    For example :

    monday_temperatures = [9.1, 8.8, 7.5]
    print(monday_temperatures[:-1])
    print(monday_temperatures[-2:])

    Here in above exaple the first function will give us output 9.1, 8.8
    and the second function will give us 8.8, 7.5


    # Lecture 32 : Acessing Characters and Slices in Strings

    Strings has index too and it works same as in the case of list.

    For example :

    mystring = "Hello"
    Print(mystring[1])
    Print(mystring[-1])
    Print(mystring[:3])

    will give us output e , o and hel

    we can also use cahane of iteams to acess specific character inside a list.

    For example :

    mylist = ["hello", 1 ,2, 3]
    Print(mylist[0])
    print(mylist[0][1])

    will give us output hello and e


    # Quiz 1 :

    Quiz complete all right answers.


    # Coding excercise 19 :

    Assignment :

    Print out the slice ["b", "c", "d"] of the letters list

    Solution :

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[1:4])


    # Coding excercise 20 :

    Assignment :

    Print out the slice ["a", "b", "c"] of the letters list

    Solution :

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[:3])


    # Coding excercise 21 :

    Assignment :

    Print out the slice ["e", "f", "g"] of the letters list

    Solution :

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[-3:])


    # Lecture 33 : Dictionary Reminder

    In the next lecture, you will learn more about dictionaries,
    so here's an example of a dictionary in case you forgot about them:

    search_engines_users = {"google": 1000000000, "bing": 127000000,
                           "duck duck go":12000000}

    A dictionary is made of pairs of keys and values. For example,
    the first pair is "google": 1000000000 where "google" is the key 
    and 1000000000 is the value of that key.


    # Lecture 34 : Acessing Items in Dictionaries

    Dictionaries has a bit different indexing than that of a list or strings.
    here we can get the values or iteams by using its key.

    For Example :

    student_grades = {"Marry":9.1, "Sim":8.8, "John":7.5}
    print(student_grades[sim])

    here in the above exaple i have given sim as the key and thus for the output,
    we will get 8.8


    # Lecture 35 : Converting Between Datatypes

    Sometimes you might need to convert between different data types in Python
    for one reason or another. That is very easy to do:


    From tuple to list:

    >>> data = (1, 2, 3)
    >>> list(data)
    [1, 2, 3]


    From list to tuple:

    >>> data = [1, 2, 3]
    >>> tuple(data)
    (1, 2, 3)


    From list to dictionary:

    >>> data = [["name", "John"], ["surname", "smith"]]
    >>> dict(data)
    {'name': 'John', 'surname': 'smith'}


    Note that the original data type needs to have the data structured in a way
    that can be understood by the new data type. For example, the following 
    would not work:

    >>> data = [1, 2, 3]
    >>> dict(data)
    
    TypeError: cannot convert dictionary update sequence element #0 to a sequence
    That's because a dictionary is made of key and value pairs, but the list was
    not constructed that way, so the above would generate an error.


    # Lecture 36 : Summary: Positive/Negative Indexes, Slicing

    In this section, you learned that:

    Lists, strings, and tuples have a positive index system:

    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
       0      1      2      3      4      5      6
    

    And a negative index system:

    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
      -7     -6     -5     -4     -3     -2     -1
    

    In a list, the 2nd, 3rd, and 4th items can be accessed with:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days[1:4]
    Output: ['Tue', 'Wed', 'Thu']


    First three items of a list:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days[:3]
    Output:['Mon', 'Tue', 'Wed'] 


    Last three items of a list:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days[-3:]
    Output: ['Fri', 'Sat', 'Sun']


    Everything but the last:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days[:-1] 
    Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 


    Everything but the last two:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days[:-2] 
    Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 


    A single in a dictionary can be accessed using its key:

    phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
    phone_numbers["Marry Simpsons"]
    Output: '+423998200919'



# Section 5 : The Basics: Functions and Conditionals


    # lecture 37 : Creating Your Own Functions

    In previous lectures we were trying to get the mean.
    But as there were no mean function we ended up calculating the sum and
    then divided it with length using len function.

    But the fact that Python does not have mean function does not mean we cant use it.
    we can create our own fuction which will give us the mean as the output.

    To create function in Python we use def keyword and pick a name for the function.
    The name has to follow the same naming rule as for the variables.

    After the function name we use ( ) inside which
    we can input some parameter/input of the function and finally end the line with :

    Point to remember is that once the line gets completed.
    The next line should be indented with four spaces.

    for Example :

    def mean(mylist):
        the_mean = sum(mylist) / len(mylist)
        return the_mean

    print(mean([1, 4, 5]))


    Output :

    3.3333333333333335

    Here in above example we can see that we have created a mean function
    with the hep of def keyword. we have given the algorithm it has to process when called
    and what to return as an output.

    Now below it when the function is called upon with the list as an input the function,
    process the given input and return the output value.

    Now the beauty of creating a function is that we can use it
    without writing the same code again and again, by just giving a 
    input value with the function name.


    # Coding Excercise 22 :

    Assignment :

    Complete the lengther function definition so that it returns
    the number of items for every input lst.


    Solution :

    def lengther(lst):
        the_length = len(lst)
        return the_length
    

    # Coding Excercise 23 :

    Assignment :

    Define a function that calculates the area of a square.


    Solution :

    def foo(length):
        area_square = length*length
        return area_square
    

    # Coding Excercises 24 :

    Assignment :

    Define a function that converts fluid ounces to milliliters
    knowing that 1 fluid ounce is equal to 29.57353 milliliters.


    Solution :

    def foo(fluid_ounces):
        milliliters = fluid_ounces * 29.57353
        return milliliters
    

    # Lecture 38 : Print or return

    When we define a function in Python and dont provide a return statement,
    it will give us none as the output.

    none here simply means nothing. it has no value or a type.

    Also make sure whenever you are creating a function it has a return statement,
    else even if you try to get the output with print function
    inside the function itself it will return the print output along with none.

    Another down side of using print inside of function insted of return is that
    you wont be able to perform any mnipulation later on it.


    # Lecture 39 : Intro to Conditionals

    When defining a function which takes an input
    if we give some input other than it supports, it will throw an error
    Unsupported operand type(s)

    We can make function support more data types by using conditionals.


    # Lecture 40 : If conditional Examples

    if - else conditionals are one of the simplest conditionals in the Python.

    here one condition is given with if function,
    and if the condition gets satisfied it will run the block below it.

    and if it is not satisfied the function will move on to the else function
    and run the code bloack bnelow it.

    for example :

    def mean(value):
        if type(value) == dict:
            the_mean = sum(value.values()) / len(value)
        else:
            the_mean = sum(value) / len(value)
        
        return the_mean

    monday_temperature = [8.8, 9.1, 9.9]
    student_grades = {"sam":8.8, "john":9.1, "sid":9.9}
    print(mean(monday_temperature))
    print(mean(student_grades))


    Here in above code we can see that the if else statements are used
    to check the type of data that is given for the input values.

    once it does so it directs the input to the algorithm it should run through.


    # Lecture 41 : Using "and" and "or" in a Conditional

    You learned to check for one single condition:

    x = 1
    
    if x == 1:
        print("Yes")
    else:
        print("No")
    

    You can also check if two conditions are met at the same time using an and operator:

    x = 1
    y = 1
    
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")
    
    That will return Yes since x == 1 and y ==1 are both True.


    You can also check if one of two conditions are met using an or operator:

    x = 1
    y = 1
    
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")

    That will return Yes since at least one of the conditions is True.
    In this case x == 1 is True.

    
    # Lecture 42 : Conditional Explained Line by Line

    Whenever we are running a if - else conditional operator
    it will check for the conditions until and unless a condition is satisfied.
    And once a condition is satisfied it will ignore rest of the code blocks.


    # Quiz 2 :

    Quiz complete all right answers.


    # Lecture 43 : More on Conditionals

    While using a conditional we can can also use
    isinstance(value, dict) with if function.

    for example :

    def mean(value):
        if isinstance(value, dict):
            the_mean = sum(value.values()) / len(value)
        else:
            the_mean = sum(value) / len(value)
        
        return the_mean

    monday_temperature = [8.8, 9.1, 9.9]
    student_grades = {"sam":8.7, "john":9.0, "sid":9.8}
    print(mean(monday_temperature))
    print(mean(student_grades))

    In above exaple we can see that isinstance is used to check the type of value.
    and the if else conditionals will direct the value to the specific algorithm
    based on its type.


    # Coding Excercise 25 :

    Assignment :

    Define a function that takes string as parameter.
    returns False if the string contains less than 8 characters
    return True is the string contains 8 or more characters

    
    Solution :

    def password(string):
        if len(string) < 8:
            return False
        else:
            return True
    

    # Coding Excercise 26 :

    Assignment :

    Define a function that takes a temperature as parameter.
    return Warm if the temperature is greater than 7
    return cold if the temperature is equal or less than 7

    
    Solution :
    
    def foo(temp):
        if temp > 7:
            return "Warm"
        else:
            return "Cold"
    

    # Lecture 44 : Elif Conditionals

    When there are more than 2 conditions to be checked for a function
    we use elif function to check for those cases.

    x = 3
    y = 1
    if x > y:
        print("x is greater than y")
    elif x==y:
        print("x is equal to y")
    else:
        print("x is less than y")
    

    # Lecture 45 : White Space

    extra spaces will work but to make your code more redable
    dont use more than one.

    it is good practice to keep one space in begining and end of operators.

    also it is a good practice to keep a line of gap between conditional
    paragraph and logical paragraph.


    # Coding Exercise 27 :

    Assignment :

    Define a function that takes a temperature as parameter.
    it should return Hot if the temperature is greater than 25
    return Warm if the temperature is between 15 and 25, including 15 and 25
    return cold if the temperature is less than 15


    Solution :

    def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:
        return "Cold"
    

    # Lecture 46 : Summary: Functions and Conditionals

    In this section, you learned to:

    Define a function:

    def cube_volume(a):
        return a * a * a
    

    Write a conditional block:

    message = "hello there"

    if "hello" in message:
        print("hi")
    else:
        print("I don't understand")
    

    Write a conditional block of multiple conditions:

    message = "hello there"
    
    if "hello" in message:
        print("hi")
    elif "hi" in message:
        print("hi")
    elif "hey" in message:
        print("hi")
    else:
        print("I don't understand")
    

    Use the and operator to check if both conditions are True at the same time:

    x = 1
    y = 1
    
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")
    
    Output is Yes since both x and y are 1.


    Use the or operator to check if at least one condition is True:

    x = 1
    y = 2
    
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")
    
    Output is Yes since x is 1.


    Check if a value is of a particular type with:

    isinstance("abc", str)
    isinstance([1, 2, 3], list)

    or

    type("abc") == str
    type([1, 2, 3]) == lst



# Section 6 : The Basics: Processing User Input


    # Lecture 47 : User Input

    