# 0x0A. Python - Inheritance
---
## Description

Project 10  in High Level Programming series is about:
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use ```isinstance```, ```issubclass```, type and super built-in functions

---
File|Task
---|---
0-lookup.py|Function that returns the list of available attributes and methods of an object
1-my_list.py|A class MyList that inherits from list
2-is_same_class.py|Function that returns True if the object is exactly an instance of the specified class ; otherwise False.
3-is_kind_of_class.py|Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
4-inherits_from.py|Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
5-base_geometry.py|An empty class BaseGeometry.
6-base_geometry.py|* class BaseGeometry (based on 5-base_geometry.py). *Public instance method: def area(self): that raises an Exception with the message area() is not implemented
7-base_geometry.py|*A class BaseGeometry (based on 6-base_geometry.py). * Public instance method: def area(self): that raises an Exception with the message area() is not implemented * Public instance method: def integer_validator(self, name, value): that validates value
8-rectangle.py|* Class Rectangle that inherits from BaseGeometry * Instantiation with width and height: def __init__(self, width, height) 
9-rectangle.py| *class Rectangle that inherits from BaseGeometry *The area() method must be implemented print() should print, and str() should return description.
10-square.py | *class Square that inherits from Rectangle. *Instantiation with size: def __init__(self, size)
11-square.py | * a class Square that inherits from Rectangle * the area() method must be implemented print() should print, and str() should return, the square description: [Square] <width>/<height>

## Author
Vasudha Kalia