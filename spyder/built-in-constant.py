# -*- coding: utf-8 -*-

class BuiltInConstant:
    """
    A small number of constants live in the built-in namespace. They are:
    False:
        The false value of the bool type. Assignments to False are illegal and 
        raise a SyntaxError.
    True:
        The true value of the bool type. Assignments to True are illegal and 
        raise a SyntaxError.
    None:
        The sole value of the type NoneType. None is frequently used to 
        represent the absence of a value, as when default arguments are not 
        passed to a function. Assignments to None are illegal and raise a 
        SyntaxError.
    NotImplemented:
        Special value which should be returned by the binary special methods 
        (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate 
        that the operation is not implemented with respect to the other type; 
        may be returned by the in-place binary special methods 
        (e.g. __imul__(), __iand__(), etc.) for the same purpose. Its truth 
        value is true.
    Ellipsis:
        The same as the ellipsis literal “...”. Special value used mostly in 
        conjunction with extended slicing syntax for user-defined container 
        data types.
    __debug__:
        This constant is true if Python was not started with an -O option. See 
        also the assert statement.
        
    The site module (which is imported automatically during startup, except if 
    the -S command-line option is given) adds several constants to the 
    built-in namespace. They are useful for the interactive interpreter shell 
    and should not be used in programs.
    quit(code=None):
    exit(code=None):
        Objects that when printed, print a message like “Use quit() or Ctrl-D 
        (i.e. EOF) to exit”, and when called, raise SystemExit with the 
        specified exit code.
    copyright:
    credits:
        Objects that when printed or called, print the text of copyright or 
        credits, respectively.
    license:
        Object that when printed, prints the message “Type license() to see 
        the full license text”, and when called, displays the full license 
        text in a pager-like fashion (one screen at a time).
    """
    def __init__(self):
        pass
    
    def constant_test(self, *args, **kwargs):
        """
        In Python, constants are usually declared and assigned on a module. 
        Here, the module means a new file containing variables, functions etc 
        which is imported to main file. Inside the module, constants are 
        written in all capital letters and underscores separating the words.
        """
        import constant
        print(constant.PI)
        print(constant.GRAVITY)
    
    
if __name__ == '__main__':
    bic = BuiltInConstant()
    
    # constant
    print('\n# constant')
    bic.constant_test()

