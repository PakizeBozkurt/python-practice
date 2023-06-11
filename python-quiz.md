Q1. What is an abstract class?
 a) An abstract class is the name for any class from which you can instantiate an object.
 b) Abstract classes must be redefined any time an object is instantiated from them.
 c) Abstract classes must inherit from concrete classes.
 d) An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

 answer = d

 Q2. What happens when you use the build-in function any() on a list?
 a) The any() function will randomly return any item from the list.
 b) The any() function returns True if any item in the list evaluates to True. Otherwise, it returnsFalse.
 c) The any() function takes as arguments the list to check inside, and the item to check for. If "any" of the items in the list match the item to check for, the function returns True.
 d) The any() function returns a Boolean value that answers the question "Are there any items in this list?"
example

if any([True, False, False, False]) == True:
    print('Yes, there is True')
>>> 'Yes, there is True'

answer = b