# Class Inheritance

## Mandatory

### 0-lookup.py
- Returns attributes and methods of given object
    - Prototype: def lookup(obj):
    - Used with: 0main.py

### 1-my_list.py
- Creates list subclass and prints int values
    - Used with: 1main.py
    - Tests: tests/1-my_list.txt

### 2-is_same_class.py
- Checks if given object is instance of given class
    - Prototype: def is_same_class(obj, a_class):
    - Used with: 2main.py

### 3-is_kind_of_class.py
- Checks if given object is either instance of given class or inherits from class
    - Prototype: def is_kind_of_class(obj, a_class):
    - Used with: 3main.py

### 4-inherits_from.py
- Checks if given object inherits from given class (either directly or indirectly)
    - Prototype: def inherits_from(obj, a_class):
    - Used with: 4main.py

### 5-base_geometry.py
- Defines empty BaseGeometry class
    - Used with: 5main.py

### 6-base_geometry.py
- Defines public area attribute
    - New method prototype: def area(self):
    - Used with: 6main.py
    - Adds onto: 5-base_geometry.py

### 7-base_geometry.py
- Defines public integer_validator attribute with exceptions (and tests)
    - New method prototype: def integer_validator(self, name, value):
    - Used with: 7main.py
    - Adds onto: 6-base_geometry.py
    - Tests: tests/7-base_geometry.txt

### 8-rectangle.py
- Defines Rectangle class that inherits from BaseGeometry parent class (with private width and height attributes)
    - New instantiation: def __init__(self, width, height):
    - Used with: 8main.py
    - Adds onto: 7-base_geometry.py
    - Inherits from: 7-base_geometry.py

### 9-rectangle.py
- Implements inherited area method and defines str() method to print
    - Used with: 9main.py
    - Adds onto: 8-rectangle.py
    - Inherits from: 7-base_geometry.py

### 10-square.py
- Defines Square class that inherits from Rectangle parent class (with private size attribute)
    - New instantiation: size: def __init__(self, size):
    - Used with: 10main.py
    - Adds onto: 9-rectangle.py
    - Inherits from: 9-rectangle.py, 7-base_geometry.py

### 11-square.py
- References str() method from 9-rectangle to print
    - Used with: 11main.py
    - Adds onto: 10-square.py
    - Inherits from: 9-rectangle.py, 7-base_geometry.py

## Learning Objectives
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use: isinstance, issubclass, type and super built-in functions
