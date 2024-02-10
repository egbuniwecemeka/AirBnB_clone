# 0x00. AirBnB clone - The console

* Packages(A collection of modules)
These are ways of structuring Python modules namespaces using 'dotted modules names'. Eg module name A.B indicates a submodule B in a package named A. An advantage of module is that it saves the authors of different modules from worrying about global variable names.
Eg Design a collection of modules('a package) for the correct handling of sound files and sound data.

1. Firstly we will need a module to handle the conversion operation between file types
2. Secondly, we will need to create a collection of modules that handle the various sound operations

When importing packages, Python searches directories of sys.path for sub-directories

__init__.py are required to help python treat directories as packages, this helps prevents directories wth common names(eg strings) from unintentionally hiding valid modules that occur later in the search path.
In simple terms, __init__.py can be an empty file, but it can also execute initialization code

Users of packages can import individual modules.
eg import sound.filter.echo

Loads the submodule sound.effects.echo(Must be referenced with its full name)
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

Another alternative of importing the submodule is:
from sound.effects import echo
The above code loads the submodule echo, makinging it available without its package prefix. This can now be used
sound.effects.echo.echofilter(input, output, delay=0.7 ,atten=4)

Another method is to import the function/variable of the submodule directly,eg:
from sound.effect.echo import echofilter
Likewise, this loads the submodule echo and makes ite function echofilter directly available.

Note: When using __from package import item__, __item has to be a subpackage/submodule, class, variable or function of the package. The import statement tests whether item is defined in package, if not it defines it as a package and trys to load it. If it fails it throws an **ImportError* exception

Also, using __import item.subitem.subsubitem__, each item except the last must be a package. The last can be a module or package but cannot br a variable, class, fuction defined in the previous item.

## Importing * From a Package

In a situation where (*) imports all sub-modules from a packagae, this could take a long time having unwarranted side effects. A common fix  is for the package author to define an __explicit index__ of the package. The import statement the usess the following convection: if the packages __init__.py defines a list __all___, this should contain all the list of modules name that should be imported when __from package import__ occurs. It is up to the package author to keep the list up-to-date or not support it if author does not see a need for importing*.
If __all__ is not defined, the statement "from package import *" does not import all submodules from the package into the current namespace. Although it ensures the package has been successfully imported(as well as initialization code) as wel as importing names defined in the package
Eg import sound.effects.echo
import sound.effects.surround
from sound.effects import*
In the above, echo and surround modules are imported in the current namespace because they are defined in the sound.effects package. When the from...import statement is executed. (This also works when __all__ is defined.)
Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practise in production code.

## Intra-package References

When packages are structured into subpackages, you can use absolute imports to refer to submodules of siblings packages.
Eg if the sound.filters.vocode module needs to use the sound.effects.echo module it can use from sound.effects import echo

Also, relative imports can be used  hence 'from module import name'. Although these imports uses (.)dots to indicate current and parent packages involved in the relative import.
Note: Relative imports are always based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module always use absolute imports

Question: What are the differences between absolute and relative imports of modules/packages.

## Packages in Multiple Directories

Packages support the special attribute (__path__). This is initialized to contain the list of directories holding the packages's (__init__.py) before the code in that file is executed

## Packages

A python file can be a module, but when the file is in a folder, it becomes a package
In C: #include "abs.h"
In Python: "import abs"
abs.my_abs(98)
or
"from abs import my.abs"
my_abs(98)

In C: #include my_maths/abs.h
In Python:
from my_maths.abs import my_abs
my_abs(98)

import my_maths.abs
my_math.abs.my_abs(98)

## Dotted modules == Path

my_script.py and my_math/abs.py was used for this example. How can i make use of a function abs(a, b) in abs.py from my_script.py
"from my_math.abs import abs" (Write in my_script.py)
Note: Although this is not complete without the magic file: (*__init___.py* file). Each folder must contain an empty *__init___.py* file as this makes it a package. This file should be empty except when * is used.

## import * is dangerous

Using * is considered bad practice in programming. In that case, *__init.py___* should not be empty but contain all the list of modules to load.

## Relative versus absolute import

Eg:
from my_func.abs import my_abs (Absolute import)
from abs import my_abs (Relative import)

## Unittest

Important concepts include;

1. Test fixture - preparation needed to perform one or more test or an associative clean up action
2. Test case - condition to test for. A test for a required response to an input. Unittest may provide a base class __TestCase__ which may be used to test for new cases
3. Test suite - A collection of test cases. It aggregates tests that should be executed together.s
4. Test runner - orchestrates the execution of test cases and provides the outcome to the user. A graphical, textual or special cases may be used to display result of test.
Note: The script Tools/unittestgui/unittestgui.py is apython source distribution GUI tool for easy use of test discovery and execution

## Command line Interface

The unittest can be used from the command line to test for modules, classes or individual test methods
python -m unittest test_module test_module1
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

The unittest can speceified by path also:
python -m unittest test_folder/test_module.py
Note: Specified path must be importable as a module, specified path is converted to a path by removing '.py' and converting '/' seperators to '.'. Also, if a test file is not importable as a module, it must be run directly.
Test are run with -v flag for higher verbosity
python -m unittest -v test_module
Use: python -m unittest -h

## Command line options

-b --buffer
-c --catch(Control-C)Interupts test and gives report up to tested module. If done again, it raises the KeyboardInterrupt exception
-f --failfast - Stops test run on first error or failure

## Test Discovery

Firstly, in order to be compatible with test discovery, all test files must be modules or packas
Basic command line usuage:
cd project_directory
python -m unittest discover
Note As a shortcut, python -m unittest is the equivalent of python -m unittest discover. If you want to pass arguments to test discovery the discover sub-command must be used explicitly.
Below are discover sub-command options
-v --verbose(Verbose output)
-s --start-directory(Directory to begin test. Default is '.')
-p --pattern(Pattern to match test files. Default is 'test*.py')
-t --top-level-dirctory(top level directory of project)
The -s, -p, -t flags can be passed in as positional arguments in that order.Eg below(From what i understand, they can be represented by what they represent)
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
The above two lines are equivalent.

## Organizing test code

Test cases are the basic building blocks. In unittest, test cases are represented by unittest.TestCase instances. To create personal test cases, you must write TestCase or use FunctionTestCase.

## AirBnB Project

* Frontend(console cmd Module)
* Backend(OOP)
* Database(File Storage)->(json module)
* Testing(unittest)

Analysis->AirBnB
User Account(Fields, unique_id, create_date)
Review
Place
Amenity->classes(attributes and methods)
CRUD.
where: C - Create - To create user acct, review, Place, Amenity using classes(attr and methods)
R - Read - To read stored data
U - Udpate - To update stored data
D - Delete - To delete stored data
In the course of building the project, some unique attributes will be used all through the different classes also CRUD methods. As a result of the presence of attributes and meethods in each class, a genreal class can be created to be a backbone of all other classes to be created.

**BaseClass** definition

* define common attributes among all classes
* define common methods among all classes
When other classes are then created, they inherit from the BaseClass ie.

**OtherClasses(BaseClass)** definition

* inherits all BaseClass attribute
* inherits all BaseClass methods
* defines unique attributes to individual class
* define unique method of the individual class

After the above processes are done, the next step involves how we store our data,
Note: Remember "Everything in Python is an OBJECT". Therefore, unless specified otherwise, we will be storing our data as an object. The drawback of this method is that object stored in a file as a string which is not advisable because of difficulty in usability.
Beacause of this, object needs to be prepared for storage(Convert to JSON string and store as file)

* prepare object for storage->JSON

ADVANTAGEES OF STORING JSON OBJECTS AS JSON STRINGS

1. With the help of a Json Module, JSON strings can be easily converted to JSON objects
2. JSON data stored as JSON string can be used by any other programming language

The process of converting python objects into JSON string, is called serialization. An additional advantage is, JSON strings are usable by other programming languages
The reverse process of converting JSON string to python object is know as deserialization(This is not connected to ealier classes or BaseClass). It will have its own class eg FileStorageClass. Therefore, FIleStorageClass will contain attributes and methods used for both serialization and deserialization
FileStorageClass: contains attributes and methods related to file  

## Summary

1. BaseModel - backbone of all other class
2. FileStorageClass - handles storage aspect of the file(A major advantage of OOP is that it cn be sed to create reusable codes. Therefore anytime we want to store a file, d same class can be reused. Hence, the reason why d fileStorageClass is in a seperate class)
Challenge: Linking BaseClass to FileStorageClass. Steps

1.In BaseClass(Create a method eg save method) - saving an instance of a class(calls the fileStorageClass) so it saves whatever is passed to it. attributes are passed into method using "self". eg id, create_at, updated_at. time representation uses the "module datetime". In a nutshell, if the save method is called, it is expected to save an instance of these attributes, provided it is called by a class or subclass that inherits from the parent class.
Example of previous explanations
from filestorage import FileStorageClass
class BaseClass():
def save(self):(saving an instance of the class)
id, create_at, update_at
storage.save(self)

A module - is a python script that can be imported and used by another script.
A package - collection of modules in a given directory.(A package should contain the magic "__init___.py". Also, the magic file can contain functionality to run anytime a module is used). Therefore if fileStorageClass is instantiated in it, anytime the filstorage module is called, an instance is created for it, this means we have access to storage. Therefore, importing storage in another module makes its instance usable with other methods and attributes.

__init___.py

storage = FileStorageClass()
