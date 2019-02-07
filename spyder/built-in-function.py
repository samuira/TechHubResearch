#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:58:51 2019

@author: Rajesh Samui
"""

class BuiltInFunctions():
    def __init__(self, *args, **kwargs):
        pass
    
    def abs_test(self, *args, **kwargs):
        """
        Return the absolute value of a number. The argument may be an integer 
        or a floating point number. If the argument is a complex number, its 
        magnitude is returned. If x defines __abs__(), abs(x) returns 
        x.__abs__().
        """
        print('-4:',abs(-4))
        print('-3.5:',abs(-3.5))
        print('3-4j:',abs(3-4j))
        print('3+4j:',abs(3+4j))
        return
        
    def all_test(self,*args,**kwargs):
        """
        Return True if all elements of the iterable are true (or if the 
        iterable is empty)
        """
        print('[]:',all([]))
        print('[3,4]:',all([3,4]))
        print('[True,False]:',all([True,False]))
        print('[-3,""]:',all([-3,""]))
        print('[None,9]:',all([None,9]))
        print('[0,8]:',all([0,8]))
        print('[False,"",0,None]:',all([False,"",0,None]))
        return
        
    def any_test(self,*args, **kwargs):
        """
        Return True if any element of the iterable is true. If the iterable 
        is empty, return False.
        """
        print('[]:',any([]))
        print('[3,4]:',any([3,4]))
        print('[True,False]:',any([True,False]))
        print('[-3,""]:',any([-3,""]))
        print('[None,9]:',any([None,9]))
        print('[0,8]:',any([0,8]))
        print('[False,"",0,None]:',any([False,"",0,None]))
        return
        
    def ascii_test(self,*args, **kwargs):
        """
        As repr(), return a string containing a printable representation of 
        an object, but escape the non-ASCII characters in the string returned 
        by repr() using \\x, \\u or \\U escapes. This generates a string 
        similar to that returned by repr() in Python 2.
        """
        normalText = 'Python is interesting'
        print(ascii(normalText))
        otherText = 'Pythön is interesting'
        print(ascii(otherText))
        print('Pyth\xf6n is interesting')
        return
        
    def bin_test(self, *args, **kwargs):
        """
        Convert an integer number to a binary string prefixed with “0b”. The 
        result is a valid Python expression. If x is not a Python int object, 
        it has to define an __index__() method that returns an integer.
        """
        print('3:',bin(3))
        print('-10:',bin(-10))
        print('14:',format(14,'#b'))
        print('14:',format(14,'b'))
        #print('14:',f'{14:#b}')
        #print('14:',f'{14:b}')
        
        class Quantity:
            apple = 1
            orange = 2
            grapes = 2
            
            def __index__(self):
                return self.apple + self.orange + self.grapes
            
        print('The binary equivalent of quantity is:', bin(Quantity()))
        
    def bool_test(self, *args, **kwargs):
        """
        Return a Boolean value, i.e. one of True or False. x is converted 
        using the standard truth testing procedure. If x is false or omitted, 
        this returns False; otherwise it returns True. The bool class is a 
        subclass of int. It cannot be subclassed further. Its only instances 
        are False and True.
        
        The following values are considered false in Python:
        None
        False
        Zero of any numeric type. For example, 0, 0.0, 0j
        Empty sequence. For example, (), [], ''.
        Empty mapping. For example, {}
        objects of Classes which has __bool__() or __len()__ method which 
        returns 0 or False
        """
        print('test:',bool('test'))
        print(':',bool(''))
        print('[]:',bool([]))
        print('["abc"]:',bool(["abc"]))
        
        test = []
        print(test,'is',bool(test))
        
        test = [0]
        print(test,'is',bool(test))
        
        test = 0.0
        print(test,'is',bool(test))
        
        test = None
        print(test,'is',bool(test))
        
        test = True
        print(test,'is',bool(test))
        
        test = 'Easy string'
        print(test,'is',bool(test))
        return
        
    def breakpoint_test(self, *args, **kwargs):
        """
        This function drops you into the debugger at the call site. 
        Specifically, it calls sys.breakpointhook(), passing args and kws 
        straight through. By default, sys.breakpointhook() calls 
        pdb.set_trace() expecting no arguments. In this case, it is purely a 
        convenience function so you don’t have to explicitly import pdb or 
        type as much code to enter the debugger. However, 
        sys.breakpointhook() can be set to some other function and 
        breakpoint() will automatically call that, allowing you to drop into 
        the debugger of choice.
        """
        print('New in version 3.7')
        
    def bytearray_test(self, *args, **kwargs):
        """
        Return a new array of bytes. The bytearray class is a mutable 
        sequence of integers in the range 0 <= x < 256. It has most of the 
        usual methods of mutable sequences, described in Mutable Sequence 
        Types, as well as most methods that the bytes type has, see Bytes and 
        Bytearray Operations.
        The optional source parameter can be used to initialize the array in 
        a few different ways:
        If it is a string, you must also give the encoding (and optionally, 
        errors) parameters; bytearray() then converts the string to bytes 
        using str.encode().
        If it is an integer, the array will have that size and will be 
        initialized with null bytes.
        If it is an object conforming to the buffer interface, a read-only 
        buffer of the object will be used to initialize the bytes array.
        If it is an iterable, it must be an iterable of integers in the range 
        0 <= x < 256, which are used as the initial contents of the array.
        Without an argument, an array of size 0 is created.
        """
        string = "Python is interesting."
        # string with encoding 'utf-8'
        arr = bytearray(string, 'utf-8')
        print(arr)
        
        size = 5
        arr = bytearray(size)
        print(arr)
        
        rList = [1, 2, 3, 4, 5]
        #for i in range(300):
        #    rList.append(i)
        arr = bytearray(rList)
        print(arr)
        return
        
    def bytes_test(self, *args, **kwargs):
        """
        Return a new “bytes” object, which is an immutable sequence of 
        integers in the range 0 <= x < 256. bytes is an immutable version of 
        bytearray – it has the same non-mutating methods and the same 
        indexing and slicing behavior.
        Accordingly, constructor arguments are interpreted as for bytearray().
        Bytes objects can also be created with literals.
        """
        string = "Python is interesting."
        # string with encoding 'utf-8'
        arr = bytes(string, 'utf-8')
        print(arr)
        
        size = 5
        arr = bytes(size)
        print(arr)
        
        rList = [1, 2, 3, 4, 5]
        arr = bytes(rList)
        print(arr)
        return
        
    def callable_test(self, *args, **kwargs):
        """
        Return True if the object argument appears callable, False if not. If 
        this returns true, it is still possible that a call fails, but if it 
        is false, calling object will never succeed. Note that classes are 
        callable (calling a class returns a new instance); instances are 
        callable if their class has a __call__() method.
        """
        x = 5
        print(callable(x))
        def testFunction():
          print("Test")
        y = testFunction
        print(callable(y))
        
        class Foo:
          def __call__(self):
            print('Print Something')
        print(callable(Foo))
        
        class Foo:
          def __call__(self):
            print('Print Something')
        InstanceOfFoo = Foo()
        # Prints 'Print Something'
        InstanceOfFoo()
        
        class Foo:
          def printLine(self):
            print('Print Something')
        print(callable(Foo))
        
        class Foo:
          def printLine(self):
            print('Print Something')
        print(callable(Foo))
        InstanceOfFoo = Foo()
        # Raises an Error
        # 'Foo' object is not callable
        try:
            InstanceOfFoo()
        except Exception as e:
            print(e)
        return
        
    def chr_test(self, *args, **kwargs):
        """
        Return the string representing a character whose Unicode code point 
        is the integer i. For example, chr(97) returns the string 'a', while 
        chr(8364) returns the string '€'. This is the inverse of ord().
        The valid range for the argument is from 0 through 1,114,
        111 (0x10FFFF in base 16). ValueError will be raised if i is outside 
        that range.
        """
        print(chr(97))
        print(chr(65))
        print(chr(1200))
        try:
            print(chr(-1))
        except Exception as e:
            print(e)
        return
        
    def classmethod_test(self, *args, **kwargs):
        """
        A class method is a method that is bound to a class rather than its 
        object. It doesn't require creation of a class instance, much like 
        staticmethod.
        The difference between a static method and a class method is:
        Static method knows nothing about the class and just deals with the 
        parameters
        Class method works with the class since its parameter is always the 
        class itself.
        The class method can be called both by the class and its object.
        Class.classmethod()
        Or even
        Class().classmethod()
        But no matter what, the class method is always attached to a class 
        with first argument as the class itself cls.
        def classMethod(cls, args...)
        """
        print('\nExample1:')
        class Person:
            age = 25
            def printAge(cls):
                print('The age is:', cls.age)
        # create printAge class method
        Person.printAge = classmethod(Person.printAge)
        Person.printAge()
        ###############################################
        print('\nExample2:')
        from datetime import date
        # random Person
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
            @classmethod
            def fromBirthYear(cls, name, birthYear):
                return cls(name, date.today().year - birthYear)
        
            def display(self):
                print(self.name + "'s age is: " + str(self.age))
        
        person = Person('Adam', 19)
        person.display()

        person1 = Person.fromBirthYear('John',  1985)
        person1.display()
        ###############################################
        print('\nExample3:')
        # random Person
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
            @staticmethod
            def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
                return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)
        
            @classmethod
            def fromBirthYear(cls, name, birthYear):
                return cls(name, date.today().year - birthYear)
        
            def display(self):
                print(self.name + "'s age is: " + str(self.age))
        
        class Man(Person):
            sex = 'Male'
        
        man = Man.fromBirthYear('John', 1985)
        print(isinstance(man, Man))
        
        man1 = Man.fromFathersAge('John', 1965, 20)
        print(isinstance(man1, Man))
        return
        
    def compile_test(self, *args, **kwargs):
        """
        The compile() method returns a Python code object from the source 
        (normal string, a byte string, or an AST object).
        The syntax of compile() is:
        compile(source, filename, mode, flags=0, dont_inherit=False, 
        optimize=-1)
        The compile() method is used if the Python code is in string form or 
        is an AST object, and you want to change it to a code object.
        The code object returned by the compile() method can later be called 
        using methods like: exec() and eval() which will execute dynamically 
        generated Python code.
        compile() Parameters
        source - a normal string, a byte string, or an AST object
        filename - file from which the code was read. If it wasn't read from a file, you can give a name yourself
        mode - Either exec or eval or single.
        eval - accepts only a single expression.
        exec - It can take a code block that has Python statements, class and 
        functions and so on.
        single - if it consists of a single interactive statement
        flags (optional) and dont_inherit (optional) - controls which future 
        statements affect the compilation of the source. Default Value: 0
        optimize (optional) - optimization level of the compiler. Default 
        value -1.
        """
        codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
        codeObejct = compile(codeInString, 'sumstring', 'exec')
        exec(codeObejct)
        return
        
    def complex_test(self, *args, **kwargs):
        """
        Return a complex number with the value real + imag*1j or convert 
        a string or number to a complex number. If the first parameter 
        is a string, it will be interpreted as a complex number and the 
        function must be called without a second parameter. The second 
        parameter can never be a string. Each argument may be any numeric 
        type (including complex). If imag is omitted, it defaults to zero 
        and the constructor serves as a numeric conversion like int and 
        float. If both arguments are omitted, returns 0j.
        Note:
        When converting from a string, the string must not contain whitespace 
        around the central + or - operator. For example, complex('1+2j') is 
        fine, but complex('1 + 2j') raises ValueError.
        The complex type is described in Numeric Types — int, float, complex.
        Changed in version 3.6: Grouping digits with underscores as in code 
        literals is allowed.
        """
        z = complex(2, -3)
        print(z)
        z = complex(1)
        print(z)
        z = complex()
        print(z)
        z = complex('5-9j')
        print(z)
        
        a = 2+3j
        print('a =',a)
        print('Type of a is',type(a))
        
        b = -2j
        print('b =',b)
        print('Type of b is',type(a))
        
        c = 0j
        print('c =',c)
        print('Type of c is',type(c))
        return
        
    def delattr_test(self, *args, **kwargs):
        """
        This is a relative of setattr(). The arguments are an object and a 
        string. The string must be the name of one of the object’s attributes. 
        The function deletes the named attribute, provided the object allows 
        it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.
        """
        class Coordinate:
          x = 10
          y = -5
          z = 0
        point1 = Coordinate() 
        print('x = ',point1.x)
        print('y = ',point1.y)
        print('z = ',point1.z)
        delattr(Coordinate, 'z')
        print('--After deleting z attribute--')
        print('x = ',point1.x)
        print('y = ',point1.y)
        # Raises Error
        try:
            print('z = ',point1.z)
        except Exception as e:
            print(e)
        ####################################
        class Coordinate:
          x = 10
          y = -5
          z = 0
        point1 = Coordinate() 
        print('x = ',point1.x)
        print('y = ',point1.y)
        print('z = ',point1.z)
        # Deleting attribute z
        del Coordinate.z
        print('--After deleting z attribute--')
        print('x = ',point1.x)
        print('y = ',point1.y)
        # Raises Attribute Error
        try:
            print('z = ',point1.z)
        except Exception as e:
            print(e)
        return
        
    def dict_test(self, *args, **kwargs):
        """
        Create a new dictionary. The dict object is the dictionary class. 
        See dict and Mapping Types — dict for documentation about this 
        class.
        For other containers see the built-in list, set, and tuple classes, 
        as well as the collections module.
        """
        numbers = dict(x=5, y=0)
        print('numbers = ',numbers)
        print(type(numbers))
        
        empty = dict()
        print('empty = ',empty)
        print(type(empty))
        # keyword argument is not passed
        numbers1 = dict([('x', 5), ('y', -5)])
        print('numbers1 =',numbers1)
        # keyword argument is also passed
        numbers2 = dict([('x', 5), ('y', -5)], z=8)
        print('numbers2 =',numbers2)
        # zip() creates an iterable in Python 3
        numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
        print('numbers3 =',numbers3)
        
        numbers1 = dict({'x': 4, 'y': 5})
        print('numbers1 =',numbers1)
        # you don't need to use dict() in above code
        numbers2 = {'x': 4, 'y': 5}
        print('numbers2 =',numbers2)
        # keyword argument is also passed
        numbers3 = dict({'x': 4, 'y': 5}, z=8)
        print('numbers3 =',numbers3)
        return
        
    def dir_test(self, *args, **kwargs):
        """
        Without arguments, return the list of names in the current local 
        scope. With an argument, attempt to return a list of valid attributes 
        for that object.
        If the object has a method named __dir__(), this method will be 
        called and must return the list of attributes. This allows objects 
        that implement a custom __getattr__() or __getattribute__() function 
        to customize the way dir() reports their attributes.
        If the object does not provide __dir__(), the function tries its best 
        to gather information from the object’s __dict__ attribute, if 
        defined, and from its type object. The resulting list is not 
        necessarily complete, and may be inaccurate when the object has a 
        custom __getattr__().
        The default dir() mechanism behaves differently with different types 
        of objects, as it attempts to produce the most relevant, rather than 
        complete, information:
        If the object is a module object, the list contains the names of the 
        module’s attributes.
        If the object is a type or class object, the list contains the names 
        of its attributes, and recursively of the attributes of its bases.
        Otherwise, the list contains the object’s attributes’ names, the 
        names of its class’s attributes, and recursively of the attributes 
        of its class’s base classes.
        Note:
        Because dir() is supplied primarily as a convenience for use at an 
        interactive prompt, it tries to supply an interesting set of names 
        more than it tries to supply a rigorously or consistently defined set 
        of names, and its detailed behavior may change across releases. For 
        example, metaclass attributes are not in the result list when the 
        argument is a class. 
        """
        number = [1, 2, 3]
        print(dir(number))
        print('\nReturn Value from empty dir()')
        print(dir())
        ##########################################
        class Person:
          def __dir__(self):
            return ['age', 'name', 'salary']
        teacher = Person()
        print(dir(teacher))
        return
        
    def divmod_test(self, *args, **kwargs):
        """
        Take two (non complex) numbers as arguments and return a pair of 
        numbers consisting of their quotient and remainder when using integer 
        division. With mixed operand types, the rules for binary arithmetic 
        operators apply. For integers, the result is the same as 
        (a // b, a % b). For floating point numbers the result is (q, a % b), 
        where q is usually math.floor(a / b) but may be 1 less than that. In 
        any case q * b + a % b is very close to a, if a % b is non-zero it 
        has the same sign as b, and 0 <= abs(a % b) < abs(b).
        """
        print('divmod(8, 3) = ', divmod(8, 3))
        print('divmod(3, 8) = ', divmod(3, 8))
        print('divmod(5, 5) = ', divmod(5, 5))
        # divmod() with Floats
        print('divmod(8.0, 3) = ', divmod(8.0, 3))
        print('divmod(3, 8.0) = ', divmod(3, 8.0))
        print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
        print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
        return
        
    def enumerate_test(self, *args, **kwargs):
        """
        Return an enumerate object. iterable must be a sequence, an iterator, 
        or some other object which supports iteration. The __next__() method 
        of the iterator returned by enumerate() returns a tuple containing a 
        count (from start which defaults to 0) and the values obtained from 
        iterating over iterable.
        """
        grocery = ['bread', 'milk', 'butter']
        enumerateGrocery = enumerate(grocery)
        print(type(enumerateGrocery))
        # converting to list
        print(list(enumerateGrocery))
        # changing the default counter
        enumerateGrocery = enumerate(grocery, 10)
        print(list(enumerateGrocery))
        #######################################
        grocery = ['bread', 'milk', 'butter']
        for item in enumerate(grocery):
          print(item)
        print('\n')
        for count, item in enumerate(grocery):
          print(count, item)
        print('\n')
        # changing default start value
        for count, item in enumerate(grocery, 100):
          print(count, item)
        return
        
    def eval_test(self, *args, **kwargs):
        """
        The arguments are a string and optional globals and locals. If 
        provided, globals must be a dictionary. If provided, locals can be 
        any mapping object.
        The expression argument is parsed and evaluated as a Python 
        expression (technically speaking, a condition list) using the globals 
        and locals dictionaries as global and local namespace. If the globals 
        dictionary is present and does not contain a value for the key 
        __builtins__, a reference to the dictionary of the built-in module 
        builtins is inserted under that key before expression is parsed. This 
        means that expression normally has full access to the standard 
        builtins module and restricted environments are propagated. If the 
        locals dictionary is omitted it defaults to the globals dictionary. 
        If both dictionaries are omitted, the expression is executed in the 
        environment where eval() is called. The return value is the result of 
        the evaluated expression.
        """
        x = 1
        print(eval('x + 1'))
        # Perimeter of Square
        def calculatePerimeter(l):
          return 4*l
        # Area of Square
        def calculateArea(l):
          return l*1
        # property = 'calculateArea(l)'
        property = 'calculatePerimeter(l)'
        for l in range(1, 5):
            if (property == 'calculatePerimeter(l)'):
                print("If length is ", l , ", Perimeter = ", eval(property))
            elif (property == 'calculateArea(l)'):
                print("If length is ", l , ", Area = ", eval(property))
            else:
              print('Wrong Function')
              break
        return
        
    def exec_test(self, *args, **kwargs):
        """
        This function supports dynamic execution of Python code. object must 
        be either a string or a code object. If it is a string, the string is 
        parsed as a suite of Python statements which is then executed 
        (unless a syntax error occurs). If it is a code object, it is 
        simply executed. In all cases, the code that’s executed is expected 
        to be valid as file input (see the section “File input” in the 
        Reference Manual). Be aware that the return and yield statements may 
        not be used outside of function definitions even within the context 
        of code passed to the exec() function. The return value is None.
        In all cases, if the optional parts are omitted, the code is executed 
        in the current scope. If only globals is provided, it must be a 
        dictionary, which will be used for both the global and the local 
        variables. If globals and locals are given, they are used for the 
        global and local variables, respectively. If provided, locals can 
        be any mapping object. Remember that at module level, globals and 
        locals are the same dictionary. If exec gets two separate objects as 
        globals and locals, the code will be executed as if it were embedded 
        in a class definition.
        If the globals dictionary does not contain a value for the key 
        __builtins__, a reference to the dictionary of the built-in module 
        builtins is inserted under that key. That way you can control what 
        builtins are available to the executed code by inserting your own 
        __builtins__ dictionary into globals before passing it to exec().
        Note:
        The built-in functions globals() and locals() return the current 
        global and local dictionary, respectively, which may be useful to 
        pass around for use as the second and third argument to exec().
        Note:
        The default locals act as described for function locals() below: 
        modifications to the default locals dictionary should not be 
        attempted. Pass an explicit locals dictionary if you need to see 
        effects of the code on locals after function exec() returns.
        """
        program = 'a = 5\nb=10\nprint("Sum =", a+b)'
        exec(program)
        program = '[print(item) for item in [1, 2, 3]]'
        exec(program)
        from math import pow, sqrt
        exec('print(dir())')
        exec('print(dir())', {})
        exec('print(dir())', {'sqrt': sqrt, 'pow': pow})
        # object can have sqrt() module
        exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})
        exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})
        # object can have squareRoot() module
        exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})
        globalsParameter = {'__builtins__' : None}
        localsParameter = {'print': print, 'dir': dir}
        exec('print(dir())', globalsParameter, localsParameter)
        return
        
    def filter_test(self, *args, **kwargs):
        """
        Construct an iterator from those elements of iterable for which 
        function returns true. iterable may be either a sequence, a container 
        which supports iteration, or an iterator. If function is None, the 
        identity function is assumed, that is, all elements of iterable that 
        are false are removed.
        Note that filter(function, iterable) is equivalent to the generator 
        expression (item for item in iterable if function(item)) if function 
        is not None and (item for item in iterable if item) if function is 
        None.
        """
        # list of alphabets
        alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
        # function that filters vowels
        def filterVowels(alphabet):
            vowels = ['a', 'e', 'i', 'o', 'u']
            if(alphabet in vowels):
                return True
            else:
                return False
        filteredVowels = filter(filterVowels, alphabets)
        print('The filtered vowels are:')
        for vowel in filteredVowels:
            print(vowel)
        ################################################
        # random list
        randomList = [1, 'a', 0, False, True, '0']
        filteredList = filter(None, randomList)
        print('The filtered elements are:')
        for element in filteredList:
            print(element)
        return
        
    def float_test(self, *args, **kwargs):
        """
        Return a floating point number constructed from a number or string x.
        If the argument is a string, it should contain a decimal number, 
        optionally preceded by a sign, and optionally embedded in whitespace. 
        The optional sign may be '+' or '-'; a '+' sign has no effect on the 
        value produced. The argument may also be a string representing a NaN 
        (not-a-number), or a positive or negative infinity. More precisely, 
        the input must conform to the following grammar after leading and 
        trailing whitespace characters are removed:
        sign           ::=  "+" | "-"
        infinity       ::=  "Infinity" | "inf"
        nan            ::=  "nan"
        numeric_value  ::=  floatnumber | infinity | nan
        numeric_string ::=  [sign] numeric_value
        Here floatnumber is the form of a Python floating-point literal, 
        described in Floating point literals. Case is not significant, so, 
        for example, “inf”, “Inf”, “INFINITY” and “iNfINity” are all 
        acceptable spellings for positive infinity.
        Otherwise, if the argument is an integer or a floating point number, 
        a floating point number with the same value (within Python’s floating 
        point precision) is returned. If the argument is outside the range of 
        a Python float, an OverflowError will be raised.
        For a general Python object x, float(x) delegates to x.__float__().
        If no argument is given, 0.0 is returned.
        """
        # for integers
        print(float(10))
        # for floats
        print(float(11.22))
        # for string floats
        print(float("-13.33"))
        # for string floats with whitespaces
        print(float("     -24.45\n"))
        try:
            # string float error
            print(float("abc"))
        except Exception as e:
            print(e)
        # for NaN
        print(float("nan"))
        print(float("NaN"))
        
        # for inf/infinity
        print(float("inf"))
        print(float("InF"))
        print(float("InFiNiTy"))
        print(float("infinity"))
        return
        
    def format_test(self, *args, **kwargs):
        """
        Convert a value to a “formatted” representation, as controlled by 
        format_spec. The interpretation of format_spec will depend on the 
        type of the value argument, however there is a standard formatting 
        syntax that is used by most built-in types: Format Specification 
        Mini-Language.
        The default format_spec is an empty string which usually gives the 
        same effect as calling str(value).
        A call to format(value, format_spec) is translated to 
        type(value).__format__(value, format_spec) which bypasses the 
        instance dictionary when searching for the value’s __format__() 
        method. A TypeError exception is raised if the method search reaches 
        object and the format_spec is non-empty, or if either the format_spec 
        or the return value are not strings.
        [[fill]align][sign][#][0][width][,][.precision][type]
        where, the options are
        fill        ::=  any character
        align       ::=  "<" | ">" | "=" | "^"
        sign        ::=  "+" | "-" | " "
        width       ::=  integer
        precision   ::=  integer
        type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" |
                        "G" | "n" | "o" | "s" | "x" | "X" | "%"
        Here, when formatting the integer 1234, we've specified the 
        formatting specifier *<+7,d. Let's get to each option:
        * - It is the fill character that fills up the empty spaces after 
            formatting
        > - It is the right alignment option that aligns the output string to 
            the right
        + - It is the sign option that forces the number to be signed 
            (having a sign on its left)
        7 - It is the width option that forces the number to take a minimum 
            width of 7, other spaces will be filled by fill character
        , - It is the thousands operator that places a comma between all 
            thousands.
        d - It is the type option that specifies the number is an integer.

        When formatting the floating point number 123.4567, we've specified 
        the format specifier ^-09.3f. These are:
        ^ - It is the center alignment option that aligns the output string 
            to the center of the remaining space
        - - It is the sign option that forces only negative numbers to show 
            the sign
        0 - It is the character that is placed in place of the empty spaces.
        9 - It is the width option that sets the minimum width of the number 
            to 9 (including decimal point, thousands comma and sign)
        .3 - It is the precision operator that sets the precision of the 
            given floating number to 3 places
        f - It is the type option that specifies the number is a float.

        """
        # d, f and b are type
        # integer
        print(format(123, "d"))
        # float arguments
        print(format(123.4567898, "f"))
        # binary format
        print(format(12, "b"))
        # integer 
        print(format(1234, "*>+7,d"))
        # float number
        print(format(123.4567, "^-09.3f"))
        # custom __format__() method
        class Person:
            def __format__(self, abcd):
                if(abcd == 'age'):
                    return '23'
                return 'None'
        print(format(Person(), "age"))
        
    def frozenset_test(self, *args, **kwargs):
        """
        The frozenset() method returns an immutable frozenset object 
        initialized with elements from the given iterable.
        Frozen set is just an immutable version of a Python set object. While 
        elements of a set can be modified at any time, elements of frozen set 
        remains the same after creation.
        Due to this, frozen sets can be used as key in Dictionary or as 
        element of another set. But like sets, it is not ordered (the 
        elements can be set at any index).
        """
        # tuple of vowels
        vowels = ('a', 'e', 'i', 'o', 'u')
        fSet = frozenset(vowels)
        print('The frozen set is:', fSet)
        print('The empty frozen set is:', frozenset())
        # random dictionary
        person = {"name": "John", "age": 23, "sex": "male"}
        fSet = frozenset(person)
        print('The frozen set is:', fSet)
        return
        
    def getattr_test(self, *args, **kwargs):
        """
        Return the value of the named attribute of object. name must be a 
        string. If the string is the name of one of the object’s attributes, 
        the result is the value of that attribute. For example, 
        getattr(x, 'foobar') is equivalent to x.foobar. If the named 
        attribute does not exist, default is returned if provided, otherwise 
        AttributeError is raised.
        """
        class Person:
            age = 23
            name = "Adam"
        person = Person()
        print('The age is:', getattr(person, "age"))
        print('The age is:', person.age)
        # when default value is provided
        print('The sex is:', getattr(person, 'sex', 'Male'))
        try:
            # when no default value is provided
            print('The sex is:', getattr(person, 'sex'))
        except Exception as e:
            print(e)
        return
        
    def globals_test(self, *args, **kwargs):
        """
        Return a dictionary representing the current global symbol table. 
        This is always the dictionary of the current module (inside a 
        function or method, this is the module where it is defined, not the 
        module from which it is called).
        A symbol table is a data structure maintained by a compiler which 
        contains all necessary information about the program.
        These include variable names, methods, classes, etc.
        There are mainly two kinds of symbol table.
            Local symbol table
            Global symbol table
        Local symbol table stores all information related to the local scope 
        of the program, and is accessed in Python using locals() method.
        The local scope could be within a function, within a class, etc.
        Likewise, a Global symbol table stores all information related to 
        the global scope of the program, and is accessed in Python using 
        globals() method.
        The global scope contains all functions, variables which are not 
        associated to any class or function.
        """
        globals()
        age = 23
        globals()['age'] = 25
        print('The age is:', age)
        return
        
    def hasattr_test(self, *args, **kwargs):
        """
        The arguments are an object and a string. The result is True if the 
        string is the name of one of the object’s attributes, False if not. 
        (This is implemented by calling getattr(object, name) and seeing 
        whether it raises an AttributeError or not.)
        """
        class Person:
            age = 23
            name = 'Adam'
        person = Person()
        print('Person has age?:', hasattr(person, 'age'))
        print('Person has salary?:', hasattr(person, 'salary'))
        return
        
    def hash_test(self, *args, **kwargs):
        """
        Return the hash value of the object (if it has one). Hash values are 
        integers. They are used to quickly compare dictionary keys during a 
        dictionary lookup. Numeric values that compare equal have the same 
        hash value (even if they are of different types, as is the case for 
        1 and 1.0).
        Note:
        For objects with custom __hash__() methods, note that hash() 
        truncates the return value based on the bit width of the host 
        machine. See __hash__() for details.
        """
        # hash for integer unchanged
        print('Hash for 181 is:', hash(181))
        # hash for decimal
        print('Hash for 181.23 is:',hash(181.23))
        # hash for string
        print('Hash for Python is:', hash('Python'))
        # tuple of vowels
        vowels = ('a', 'e', 'i', 'o', 'u')
        print('The hash is:', hash(vowels))
        class Person:
            def __init__(self, age, name):
                self.age = age
                self.name = name
            def __eq__(self, other):
                return self.age == other.age and self.name == other.name
            def __hash__(self):
                print('The hash is:')
                return hash((self.age, self.name))
        person = Person(23, 'Adam')
        print(hash(person))
        return
        
    def help_test(self, *args, **kwargs):
        """
        Invoke the built-in help system. (This function is intended for 
        interactive use.) If no argument is given, the interactive help 
        system starts on the interpreter console. If the argument is a 
        string, then the string is looked up as the name of a module, 
        function, class, method, keyword, or documentation topic, and a help 
        page is printed on the console. If the argument is any other kind of 
        object, a help page on the object is generated.
        This function is added to the built-in namespace by the site module.
        """
        help(list)
        help(dict)
        help(print)
        help([1, 2, 3])
        help('random thing')
        help('print')
        help('def')
        from math import pow
        help('math.pow')
        # If no argument is passed, Python's help utility (interactive help 
        # system) starts on the console.
        # help()
        return
        
    def hex_test(self, *args, **kwargs):
        """
        Convert an integer number to a lowercase hexadecimal string prefixed 
        with “0x”. If x is not a Python int object, it has to define an 
        __index__() method that returns an integer.
        If you want to convert an integer number to an uppercase or lower 
        hexadecimal string with prefix or not, you can use either of the ways.
        """
        number = 435
        print(number, 'in hex =', hex(number))
        number = 0
        print(number, 'in hex =', hex(number))
        number = -34
        print(number, 'in hex =', hex(number))
        returnType = type(hex(number))
        print('Return type from hex() is', returnType)
        number = 2.5
        print(number, 'in hex =', float.hex(number))
        number = 0.0
        print(number, 'in hex =', float.hex(number))
        number = 10.5
        print(number, 'in hex =', float.hex(number))
        return
        
    def id_test(self, *args, **kwargs):
        """
        Return the “identity” of an object. This is an integer which is 
        guaranteed to be unique and constant for this object during its 
        lifetime. Two objects with non-overlapping lifetimes may have the 
        same id() value.
        CPython implementation detail: This is the address of the object in 
        memory.
        """
        class Foo:
            b = 5
        dummyFoo = Foo()
        print('id of dummyFoo =',id(dummyFoo))
        print('id of dummyFoo.b =',id(dummyFoo.b))
        print('id of 5 =',id(5))
        a = 5
        print('id of a =',id(a))
        b = a
        print('id of b =',id(b))
        c = 5.0
        print('id of c =',id(c))
        return
        
    def input_test(self, *args, **kwargs):
        """
        If the prompt argument is present, it is written to standard output 
        without a trailing newline. The function then reads a line from 
        input, converts it to a string (stripping a trailing newline), and 
        returns that. When EOF is read, EOFError is raised.
        """
        print('Uncomment the code to test.')
        # get input from user
        # inputString = input()
        # print('The inputted string is:', inputString)
        # get input from user
        # inputString = input('Enter a string:')
        # print('The inputted string is:', inputString)
        return
        
    def int_test(self, *args, **kwargs):
        """
        Return an integer object constructed from a number or string x, or 
        return 0 if no arguments are given. If x defines __int__(), int(x) 
        returns x.__int__(). If x defines __trunc__(), it returns 
        x.__trunc__(). For floating point numbers, this truncates towards 
        zero.
        If x is not a number or if base is given, then x must be a string, 
        bytes, or bytearray instance representing an integer literal in 
        radix base. Optionally, the literal can be preceded by + or - (with 
        no space in between) and surrounded by whitespace. A base-n literal 
        consists of the digits 0 to n-1, with a to z (or A to Z) having 
        values 10 to 35. The default base is 10. The allowed values are 0 
        and 2–36. Base-2, -8, and -16 literals can be optionally prefixed 
        with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 
        0 means to interpret exactly as a code literal, so that the actual 
        base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, 
        while int('010') is, as well as int('010', 8).
        The integer type is described in Numeric Types — int, float, complex.
        Changed in version 3.4: If base is not an instance of int and the 
        base object has a base.__index__ method, that method is called to 
        obtain an integer for the base. Previous versions used base.__int__ 
        instead of base.__index__.
        """
        # integer
        print("int(123) is:", int(123))
        # float
        print("int(123.23) is:", int(123.23))
        # string
        print("int('123') is:", int('123'))
        # binary 0b or 0B
        print("For 1010, int is:", int('1010', 2))
        print("For 0b1010, int is:", int('0b1010', 2))
        # octal 0o or 0O
        print("For 12, int is:", int('12', 8))
        print("For 0o12, int is:", int('0o12', 8))
        # hexadecimal
        print("For A, int is:", int('A', 16))
        print("For 0xA, int is:", int('0xA', 16))
        class Person:
            age = 23
            def __index__(self):
                print('index')
                return self.age
            def __int__(self):
                print('int')
                return self.age
        person = Person()
        print('int(person) is:', int(person))
        return
    
    def isinstance_test(self, *args, **kwargs):
        """
        Return true if the object argument is an instance of the classinfo 
        argument, or of a (direct, indirect or virtual) subclass thereof. 
        If object is not an object of the given type, the function always 
        returns false. If classinfo is a tuple of type objects (or 
        recursively, other such tuples), return true if object is an 
        instance of any of the types. If classinfo is not a type or tuple of 
        types and such tuples, a TypeError exception is raised.
        """
        class Foo:
          a = 5
        fooInstance = Foo()
        print(isinstance(fooInstance, Foo))
        print(isinstance(fooInstance, (list, tuple)))
        print(isinstance(fooInstance, (list, tuple, Foo)))
        numbers = [1, 2, 3]
        result = isinstance(numbers, list)
        print(numbers,'instance of list?', result)
        result = isinstance(numbers, dict)
        print(numbers,'instance of dict?', result)
        result = isinstance(numbers, (dict, list))
        print(numbers,'instance of dict or list?', result)
        number = 5
        result = isinstance(number, list)
        print(number,'instance of list?', result)
        result = isinstance(number, int)
        print(number,'instance of int?', result)
        return
        
    def issubclass_test(self, *args, **kwargs):
        """
        Return true if class is a subclass (direct, indirect or virtual) of 
        classinfo. A class is considered a subclass of itself. classinfo may 
        be a tuple of class objects, in which case every entry in classinfo 
        will be checked. In any other case, a TypeError exception is raised.
        """
        class Polygon:
          def __init__(polygonType):
            print('Polygon is a ', polygonType)
        class Triangle(Polygon):
          def __init__(self):
            Polygon.__init__('triangle')
        print(issubclass(Triangle, Polygon))
        print(issubclass(Triangle, list))
        print(issubclass(Triangle, (list, Polygon)))
        print(issubclass(Polygon, (list, Polygon)))
        return
        
    def iter_test(self, *args, **kwargs):
        """
        Return an iterator object. The first argument is interpreted very 
        differently depending on the presence of the second argument. 
        Without a second argument, object must be a collection object which 
        supports the iteration protocol (the __iter__() method), or it must 
        support the sequence protocol (the __getitem__() method with integer 
        arguments starting at 0). If it does not support either of those 
        protocols, TypeError is raised. If the second argument, sentinel, 
        is given, then object must be a callable object. The iterator 
        created in this case will call object with no arguments for each 
        call to its __next__() method; if the value returned is equal to 
        sentinel, StopIteration will be raised, otherwise the value will be 
        returned.
        One useful application of the second form of iter() is to build a 
        block-reader.
        """
        # list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelsIter = iter(vowels)
        # prints 'a'
        print(next(vowelsIter))
        # prints 'e'
        print(next(vowelsIter))
        # prints 'i'
        print(next(vowelsIter))
        # prints 'o'
        print(next(vowelsIter))
        # prints 'u'
        print(next(vowelsIter))
        class PrintNumber:
            def __init__(self, max):
                self.max = max
            def __iter__(self):
                self.num = 0
                return self
            def __next__(self):
                if(self.num >= self.max):
                    raise StopIteration('No more element remained.')
                self.num += 1
                return self.num
        printNum = PrintNumber(3)
        printNumIter = iter(printNum)
        # prints '1'
        print(next(printNumIter))
        # prints '2'
        print(next(printNumIter))
        # prints '3'
        print(next(printNumIter))
        try:
            # raises StopIteration
            print(next(printNumIter))
        except Exception as e:
            print(e)
        with open('mydata.txt') as fp:
            for line in iter(fp.readline, ''):
                print(line)
        return
        
    def len_test(self, *args, **kwargs):
        """
        Return the length (the number of items) of an object. The argument 
        may be a sequence (such as a string, bytes, tuple, list, or range) 
        or a collection (such as a dictionary, set, or frozen set).
        """
        testList = []
        print(testList, 'length is', len(testList))
        testList = [1, 2, 3]
        print(testList, 'length is', len(testList))
        testTuple = (1, 2, 3)
        print(testTuple, 'length is', len(testTuple))
        testRange = range(1, 10)
        print('Length of', testRange, 'is', len(testRange))
        testString = ''
        print('Length of', testString, 'is', len(testString))
        testString = 'Python'
        print('Length of', testString, 'is', len(testString))
        # byte object
        testByte = b'Python'
        print('Length of', testByte, 'is', len(testByte))
        testList = [1, 2, 3]
        # converting to bytes object
        testByte = bytes(testList)
        print('Length of', testByte, 'is', len(testByte))
        testSet = {1, 2, 3}
        print(testSet, 'length is', len(testSet))
        # Empty Set
        testSet = set()
        print(testSet, 'length is', len(testSet))
        testDict = {1: 'one', 2: 'two'}
        print(testDict, 'length is', len(testDict))
        testDict = {}
        print(testDict, 'length is', len(testDict))
        testSet = {1, 2}
        # frozenSet
        frozenTestSet = frozenset(testSet)
        print(frozenTestSet, 'length is', len(frozenTestSet))
        class Session:
            def __init__(self, number = 0):
              self.number = number
            def __len__(self):
              return self.number
        # default length is 0
        s1 = Session()
        print(len(s1))
        # giving custom length
        s2 = Session(6)
        print(len(s2))
        return
        
    def list_test(self, *args, **kwargs):
        """
        The list() constructor creates a list in Python.
        Python list() constructor takes a single argument:
        iterable (Optional) - an object that could be a sequence 
                            (string, tuples) or collection (set, dictionary) 
                            or iterator object.
        """
        # empty list
        print(list())
        # vowel string
        vowelString = 'aeiou'
        print(list(vowelString))
        # vowel tuple
        vowelTuple = ('a', 'e', 'i', 'o', 'u')
        print(list(vowelTuple))
        # vowel list
        vowelList = ['a', 'e', 'i', 'o', 'u']
        print(list(vowelList))
        # vowel set
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        print(list(vowelSet))
        # vowel dictionary
        vowelDictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
        print(list(vowelDictionary))
        class PowTwo:
            def __init__(self, max):
                self.max = max
            def __iter__(self):
                self.num = 0
                return self
            def __next__(self):
                if(self.num >= self.max):
                    raise StopIteration
                result = 2 ** self.num
                self.num += 1
                return result
        powTwo = PowTwo(5)
        powTwoIter = iter(powTwo)
        print(list(powTwoIter))
        return
        
    def locals_test(self, *args, **kwargs):
        """
        Update and return a dictionary representing the current local symbol 
        table. Free variables are returned by locals() when it is called in 
        function blocks, but not in class blocks.
        Note:
        The contents of this dictionary should not be modified; changes may 
        not affect the values of local and free variables used by the 
        interpreter.
        """
        locals()
        def localsNotPresent():
            return locals()
        def localsPresent():
            present = True
            return locals()
        print('localsNotPresent:', localsNotPresent())
        print('localsPresent:', localsPresent())
        def localsPresent():
            present = True
            print(present)
            locals()['present'] = False;
            print(present)
        localsPresent()
        return
        
    def map_test(self, *args, **kwargs):
        """
        Return an iterator that applies function to every item of iterable, 
        yielding the results. If additional iterable arguments are passed, 
        function must take that many arguments and is applied to the items 
        from all iterables in parallel. With multiple iterables, the 
        iterator stops when the shortest iterable is exhausted. For cases 
        where the function inputs are already arranged into argument tuples.
        """
        def calculateSquare(n):
          return n*n
        numbers = (1, 2, 3, 4)
        result = map(calculateSquare, numbers)
        print(result)
        # converting map object to set
        numbersSquare = set(result)
        print(numbersSquare)
        numbers = (1, 2, 3, 4)
        result = map(lambda x: x*x, numbers)
        print(result)
        # converting map object to set
        numbersSquare = set(result)
        print(numbersSquare)
        num1 = [4, 5, 6]
        num2 = [5, 6, 7]
        result = map(lambda n1, n2: n1+n2, num1, num2)
        print(list(result))
        return
        
    def max_test(self, *args, **kwargs):
        """
        Return the largest item in an iterable or the largest of two or more 
        arguments.
        If one positional argument is provided, it should be an iterable. 
        The largest item in the iterable is returned. If two or more 
        positional arguments are provided, the largest of the positional 
        arguments is returned.
        There are two optional keyword-only arguments. The key argument 
        specifies a one-argument ordering function like that used for 
        list.sort(). The default argument specifies an object to return if 
        the provided iterable is empty. If the iterable is empty and default 
        is not provided, a ValueError is raised.
        If multiple items are maximal, the function returns the first one 
        encountered. This is consistent with other sort-stability preserving 
        tools such as sorted(iterable, key=keyfunc, reverse=True)[0] and 
        heapq.nlargest(1, iterable, key=keyfunc).
        """
        # using max(arg1, arg2, *args)
        print('Maximum is:', max(1, 3, 2, 5, 4))
        # using max(iterable)
        num = [1, 3, 2, 8, 5, 10, 6]
        print('Maximum is:', max(num))
        def sumDigit(num):
            sum = 0
            while(num):
                sum += num % 10
                num = int(num / 10)
            return sum
        # using max(arg1, arg2, *args, key)
        print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))
        # using max(iterable, key)
        num = [15, 300, 2700, 821, 52, 10, 6]
        print('Maximum is:', max(num, key=sumDigit))
        num = [15, 300, 2700, 821]
        num1 = [12, 2]
        num2 = [34, 567, 78]
        # using max(iterable, *iterables, key)
        print('Maximum is:', max(num, num1, num2, key=len))
        return
        
    def  memoryview_test(self, *args, **kwargs):
        """
        The memoryview() method returns a memory view object of the given 
        argument.
        Before we get into what memory views are, we need to first 
        understand about Python's Buffer Protocol.
        What is a Buffer Protocol?
        Simply said, buffer protocol provides a way to access the internal 
        data of an object. This internal data is a memory array or a buffer.        
        Buffer protocol allows one object to expose its internal data 
        (buffers) and the other to access those buffers without intermediate 
        copying.
        This protocol is only accessible to us at the C-API level and not 
        using our normal code base.
        So, in order to expose the same protocol to normal Python code base, 
        memory views are present.
        What is a memory view?
        Memory view is a safe way to expose the buffer protocol in Python.        
        It allows you to access the internal buffers of an object by 
        creating a memory view object.
        Why buffer protocol and memory views are important?
        We need to remember that whenever we perform some action on an 
        object (call a function of an object, slice an array), we (or 
        Python) need to create a copy of the object.
        If we have a large data to work with (eg. binary data of an image), 
        we would unnecessarily create copies of huge chunks of data, which 
        serves almost no use.
        Using buffer protocol, we can give another object access to 
        use/modify the large data without copying it. This makes the program 
        use less memory and increases the execution speed.
        """
        #random bytearray
        randomByteArray = bytearray('ABC', 'utf-8')
        mv = memoryview(randomByteArray)
        # access memory view's zeroth index
        print(mv[0])
        # create byte from memory view
        print(bytes(mv[0:2]))
        # create list from memory view
        print(list(mv[0:3]))
        #random bytearray
        randomByteArray = bytearray('ABC', 'utf-8')
        print('Before updation:', randomByteArray)
        mv = memoryview(randomByteArray)
        # update 1st index of mv to Z
        mv[1] = 90
        print('After updation:', randomByteArray)
        return
        
    def min_test(self, *args, **kwargs):
        """
        Return the smallest item in an iterable or the smallest of two or 
        more arguments.
        If one positional argument is provided, it should be an iterable. 
        The smallest item in the iterable is returned. If two or more 
        positional arguments are provided, the smallest of the positional 
        arguments is returned.
        There are two optional keyword-only arguments. The key argument 
        specifies a one-argument ordering function like that used for 
        list.sort(). The default argument specifies an object to return if 
        the provided iterable is empty. If the iterable is empty and default 
        is not provided, a ValueError is raised.
        If multiple items are minimal, the function returns the first one 
        encountered. This is consistent with other sort-stability preserving 
        tools such as sorted(iterable, key=keyfunc)[0] and 
        heapq.nsmallest(1, iterable, key=keyfunc).
        """
        # using min(arg1, arg2, *args)
        print('Minimum is:', min(1, 3, 2, 5, 4))
        # using min(iterable)
        num = [3, 2, 8, 5, 10, 6]
        print('Minimum is:', min(num))
        def sumDigit(num):
            sum = 0
            while(num):
                sum += num % 10
                num = int(num / 10)
            return sum
        # using min(arg1, arg2, *args, key)
        print('Minimum is:', min(100, 321, 267, 59, 40, key=sumDigit))
        # using min(iterable, key)
        num = [15, 300, 2700, 821, 52, 10, 6]
        print('Minimum is:', min(num, key=sumDigit))
        num = [15, 300, 2700, 821]
        num1 = [12, 2]
        num2 = [34, 567, 78]
        # using min(iterable, *iterables, key)
        print('Minimum is:', min(num, num1, num2, key=len))
        return
        
    def next_test(self, *args, **kwargs):
        """
        Retrieve the next item from the iterator by calling its __next__() 
        method. If default is given, it is returned if the iterator is 
        exhausted, otherwise StopIteration is raised.
        """
        random = [5, 9, 'cat']
        # converting list to iterator
        randomIterator = iter(random)
        print(randomIterator)
        # Output: 5
        print(next(randomIterator))
        # Output: 9
        print(next(randomIterator))
        # Output: 'cat'
        print(next(randomIterator))
        try:
            # This will raise Error
            # iterator is exhausted
            print(next(randomIterator))
        except Exception as e:
            print('StopIteration Exception',e)
        random = [5, 9]
        # converting list to iterator
        randomIterator = iter(random)
        # Output: 5
        print(next(randomIterator, '-1'))
        # Output: 9
        print(next(randomIterator, '-1'))
        # randomIterator is exhausted
        # Output: '-1'
        print(next(randomIterator, '-1'))
        print(next(randomIterator, '-1'))
        print(next(randomIterator, '-1'))
        return
        
    def object_test(self, *args, **kwargs):
        """
        Return a new featureless object. object is a base for all classes. 
        It has the methods that are common to all instances of Python 
        classes. This function does not accept any arguments.
        Note:
        object does not have a __dict__, so you can’t assign arbitrary 
        attributes to an instance of the object class.
        """
        test = object()
        print(type(test))
        print(dir(test))
        return
        
    def oct_test(self, *args, **kwargs):
        """
        Convert an integer number to an octal string prefixed with “0o”. The 
        result is a valid Python expression. If x is not a Python int 
        object, it has to define an __index__() method that returns an 
        integer.
        """
        # decimal number
        print('oct(10) is:', oct(10))
        # binary number
        print('oct(0b101) is:', oct(0b101))
        # hexadecimal number
        print('oct(0XA) is:', oct(0XA))
        class Person:
            age = 23
            def __index__(self):
                return self.age
            def __int__(self):
                return self.age
        person = Person()
        print('The oct is:', oct(person))
        return
        
    def open_test(self, *args, **kwargs):
        """
        Open file and return a corresponding file object. If the file cannot 
        be opened, an OSError is raised.
        file is a path-like object giving the pathname (absolute or relative 
        to the current working directory) of the file to be opened or an 
        integer file descriptor of the file to be wrapped. (If a file 
        descriptor is given, it is closed when the returned I/O object is 
        closed, unless closefd is set to False.)
        mode is an optional string that specifies the mode in which the file 
        is opened. It defaults to 'r' which means open for reading in text 
        mode. Other common values are 'w' for writing (truncating the file if 
        it already exists), 'x' for exclusive creation and 'a' for appending 
        (which on some Unix systems, means that all writes append to the end 
        of the file regardless of the current seek position). In text mode, if 
        encoding is not specified the encoding used is platform dependent: 
            locale.getpreferredencoding(False) is called to get the current 
            locale encoding. (For reading and writing raw bytes use binary 
            mode and leave encoding unspecified.) 
        The available modes are:
        Character 	Meaning
        'r' 	open for reading (default)
        'w' 	open for writing, truncating the file first
        'x' 	open for exclusive creation, failing if the file already exists
        'a' 	open for writing, appending to the end of the file if it exists
        'b' 	binary mode
        't' 	text mode (default)
        '+' 	open a disk file for updating (reading and writing)
        
        The default mode is 'r' (open for reading text, synonym of 'rt'). For 
        binary read-write access, the mode 'w+b' opens and truncates the file 
        to 0 bytes. 'r+b' opens the file without truncation.
        As mentioned in the Overview, Python distinguishes between binary and 
        text I/O. Files opened in binary mode (including 'b' in the mode 
        argument) return contents as bytes objects without any decoding. In 
        text mode (the default, or when 't' is included in the mode argument), 
        the contents of the file are returned as str, the bytes having been 
        first decoded using a platform-dependent encoding or using the 
        specified encoding if given.
        There is an additional mode character permitted, 'U', which no longer 
        has any effect, and is considered deprecated. It previously enabled 
        universal newlines in text mode, which became the default behaviour in 
        Python 3.0. Refer to the documentation of the newline parameter for 
        further details.
        Note:
        Python doesn’t depend on the underlying operating system’s notion of 
        text files; all the processing is done by Python itself, and is 
        therefore platform-independent.
        buffering is an optional integer used to set the buffering policy. 
        Pass 0 to switch buffering off (only allowed in binary mode), 1 to 
        select line buffering (only usable in text mode), and an integer > 1 
        to indicate the size in bytes of a fixed-size chunk buffer. When no 
        buffering argument is given, the default buffering policy works as 
        follows:
            Binary files are buffered in fixed-size chunks; the size of the 
            buffer is chosen using a heuristic trying to determine the 
            underlying device’s “block size” and falling back on 
            io.DEFAULT_BUFFER_SIZE. On many systems, the buffer will typically 
            be 4096 or 8192 bytes long.
            “Interactive” text files (files for which isatty() returns True) 
            use line buffering. Other text files use the policy described 
            above for binary files.
        encoding is the name of the encoding used to decode or encode the file.
        This should only be used in text mode. The default encoding is 
        platform dependent (whatever locale.getpreferredencoding() returns), 
        but any text encoding supported by Python can be used. See the codecs 
        module for the list of supported encodings.
        errors is an optional string that specifies how encoding and decoding 
        errors are to be handled—this cannot be used in binary mode. A variety 
        of standard error handlers are available (listed under Error Handlers),
        though any error handling name that has been registered with 
        codecs.register_error() is also valid. The standard names include:
            'strict' to raise a ValueError exception if there is an encoding 
            error. The default value of None has the same effect.
            'ignore' ignores errors. Note that ignoring encoding errors can 
            lead to data loss.
            'replace' causes a replacement marker (such as '?') to be inserted 
            where there is malformed data.
            'surrogateescape' will represent any incorrect bytes as code 
            points in the Unicode Private Use Area ranging from U+DC80 to 
            U+DCFF. These private code points will then be turned back into 
            the same bytes when the surrogateescape error handler is used when 
            writing data. This is useful for processing files in an unknown 
            encoding.
            'xmlcharrefreplace' is only supported when writing to a file. 
            Characters not supported by the encoding are replaced with the 
            appropriate XML character reference &#nnn;.
            'backslashreplace' replaces malformed data by Python’s backslashed 
            escape sequences.
            'namereplace' (also only supported when writing) replaces 
            unsupported characters with \\N{...} escape sequences.
        newline controls how universal newlines mode works (it only applies to 
        text mode). It can be None, '', '\\n', '\\r', and '\\r\\n'. It works as 
        follows:
            When reading input from the stream, if newline is None, universal 
            newlines mode is enabled. Lines in the input can end in '\\n', 
            '\\r', or '\\r\\n', and these are translated into '\\n' before being 
            returned to the caller. If it is '', universal newlines mode is 
            enabled, but line endings are returned to the caller untranslated. 
            If it has any of the other legal values, input lines are only 
            terminated by the given string, and the line ending is returned to 
            the caller untranslated.
            When writing output to the stream, if newline is None, any '\\n' 
            characters written are translated to the system default line 
            separator, os.linesep. If newline is '' or '\\n', no translation 
            takes place. If newline is any of the other legal values, any '\\n' 
            characters written are translated to the given string.
        If closefd is False and a file descriptor rather than a filename was 
        given, the underlying file descriptor will be kept open when the file 
        is closed. If a filename is given closefd must be True (the default) 
        otherwise an error will be raised.
        A custom opener can be used by passing a callable as opener. The 
        underlying file descriptor for the file object is then obtained by 
        calling opener with (file, flags). opener must return an open file 
        descriptor (passing os.open as opener results in functionality similar 
        to passing None).
        The newly created file is non-inheritable.
        """
        # opens test.text file of the current directory
        f = open("mydata.txt")
        
        # specifying full path
        f = open("/home/dat-asset-36/Spyder/mydata.txt")
        
        # opens for read
        f = open("/home/dat-asset-36/Spyder/mydata.txt", mode='r')
        
        # opens for write 
        f = open("/home/dat-asset-36/Spyder/mydata.txt", mode = 'w')
        
        # opens for writing to the end 
        f = open("/home/dat-asset-36/Spyder/mydata.txt", mode = 'a')
        
        f = open("/home/dat-asset-36/Spyder/mydata.txt", mode = 'r', encoding='utf-8')
        return
        
    def ord_test(self, *args, **kwargs):
        """
        Given a string representing one Unicode character, return an integer 
        representing the Unicode code point of that character. For example, 
        ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 
        This is the inverse of chr().
        """
        # code point of integer
        print(ord('5'))
        
        # code point of alphabet 
        print(ord('A'))
        
        # code point of character
        print(ord('$'))
        return
        
    def pow_test(self, *args, **kwargs):
        """
        Return x to the power y; if z is present, return x to the power y, 
        modulo z (computed more efficiently than pow(x, y) % z). The 
        two-argument form pow(x, y) is equivalent to using the power 
        operator: x**y.
        The arguments must have numeric types. With mixed operand types, the 
        coercion rules for binary arithmetic operators apply. For int 
        operands, the result has the same type as the operands (after 
        coercion) unless the second argument is negative; in that case, all 
        arguments are converted to float and a float result is delivered. For 
        example, 10**2 returns 100, but 10**-2 returns 0.01. If the second 
        argument is negative, the third argument must be omitted. If z is 
        present, x and y must be of integer types, and y must be non-negative.
        """
        # positive x, positive y (x**y)
        print(pow(2, 2))
        
        # negative x, positive y
        print(pow(-2, 2))
        
        # positive x, negative y (x**-y)
        print(pow(2, -2))
        
        # negative x, negative y
        print(pow(-2, -2))
        
        x = 7
        y = 2
        z = 5
        
        print(pow(x, y, z)) # (x**y)%z
        return
        
    def print_test(self, *args, **kwargs):
        """
        Print objects to the text stream file, separated by sep and followed 
        by end. sep, end, file and flush, if present, must be given as keyword 
        arguments.
        All non-keyword arguments are converted to strings like str() does and 
        written to the stream, separated by sep and followed by end. Both sep 
        and end must be strings; they can also be None, which means to use the 
        default values. If no objects are given, print() will just write end.
        The file argument must be an object with a write(string) method; if it 
        is not present or None, sys.stdout will be used. Since printed 
        arguments are converted to text strings, print() cannot be used with 
        binary mode file objects. For these, use file.write(...) instead.
        Whether output is buffered is usually determined by file, but if the 
        flush keyword argument is true, the stream is forcibly flushed.
        """
        print("Python is fun.")

        a = 5
        # Two objects are passed
        print("a =", a)
        
        b = a
        # Three objects are passed
        print('a =', a, '= b')
        
        a = 5
        print("a =", a, sep='00000', end='\n\n\n')
        print("a =", a, sep='0', end='')
        print('end')
        
        sourceFile = open('/home/dat-asset-36/Spyder/mydata.txt', 'w')
        print('Pretty cool, huh!', file = sourceFile)
        sourceFile.close()
        return
        
    def property_test(self, *args, **kwargs):
        """
        Return a property attribute.
        fget is a function for getting an attribute value. fset is a function 
        for setting an attribute value. fdel is a function for deleting an 
        attribute value. And doc creates a docstring for the attribute.
        If given, doc will be the docstring of the property attribute. 
        Otherwise, the property will copy fget’s docstring (if it exists). 
        This makes it possible to create read-only properties easily using 
        property() as a decorator.
        """
        class Person:
            def __init__(self, name):
                self._name = name
        
            def getName(self):
                print('Getting name')
                return self._name
        
            def setName(self, value):
                print('Setting name to ' + value)
                self._name = value
        
            def delName(self):
                print('Deleting name')
                del self._name
        
            # Set property to use getName, setName
            # and delName methods
            name = property(getName, setName, delName, 'Name property')
        
        p = Person('Adam')
        print(p.name)
        p.name = 'John'
        del p.name
        
        class Person:
            def __init__(self, name):
                self._name = name
        
            @property
            def name(self):
                print('Getting name')
                return self._name
        
            @name.setter
            def name(self, value):
                print('Setting name to ' + value)
                self._name = value
        
            @name.deleter
            def name(self):
                print('Deleting name')
                del self._name
        
        p = Person('Adam')
        print('The name is:', p.name)
        p.name = 'John'
        del p.name
        return
        
    def  range_test(self, *args, **kwargs):
        """
        Rather than being a function, range is actually an immutable sequence 
        type, as documented in Ranges and Sequence Types — list, tuple, range.
        """
        # empty range
        print(list(range(0)))
        # using range(stop)
        print(list(range(10)))
        # using range(start, stop)
        print(list(range(1, 10)))
        start = 2
        stop = 14
        step = 2
        print(list(range(start, stop, step)))
        start = 2
        stop = -14
        step = -2
        print(list(range(start, stop, step)))
        # value constraint not met
        print(list(range(start, 14, step)))
        return
        
    def repr_test(self, *args, **kwargs):
        """
        Return a string containing a printable representation of an object. 
        For many types, this function makes an attempt to return a string that 
        would yield an object with the same value when passed to eval(), 
        otherwise the representation is a string enclosed in angle brackets 
        that contains the name of the type of the object together with 
        additional information often including the name and address of the 
        object. A class can control what this function returns for its 
        instances by defining a __repr__() method.
        """
        var = 'foo'
        print(repr(var))
        class Person:
            name = 'Adam'
        
            def __repr__(self):
                return repr(self.name)
        
        print(repr(Person()))
        return
        
    def reversed_test(self, *args, **kwargs):
        """
        Return a reverse iterator. seq must be an object which has a 
        __reversed__() method or supports the sequence protocol (the __len__() 
        method and the __getitem__() method with integer arguments starting at 
        0).
        """
        # for string
        seqString = 'Python'
        print(list(reversed(seqString)))
        # for tuple
        seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
        print(list(reversed(seqTuple)))
        # for range
        seqRange = range(5, 9)
        print(list(reversed(seqRange)))
        # for list
        seqList = [1, 2, 4, 3, 5]
        print(list(reversed(seqList)))
        
        class Vowels:
            vowels = ['a', 'e', 'i', 'o', 'u']
        
            def __reversed__(self):
                return reversed(self.vowels)
        
        v = Vowels()
        print(list(reversed(v)))
        return
        
    def round_test(self, *args, **kwargs):
        """
        Return number rounded to ndigits precision after the decimal point. If 
        ndigits is omitted or is None, it returns the nearest integer to its 
        input.
        For the built-in types supporting round(), values are rounded to the 
        closest multiple of 10 to the power minus ndigits; if two multiples 
        are equally close, rounding is done toward the even choice (so, for 
        example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). 
        Any integer value is valid for ndigits (positive, zero, or negative). 
        The return value is an integer if ndigits is omitted or None. 
        Otherwise the return value has the same type as number.
        For a general Python object number, round delegates to 
        number.__round__.
        Note:
        The behavior of round() for floats can be surprising: for example, 
        round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a 
        bug: it’s a result of the fact that most decimal fractions can’t be 
        represented exactly as a float.
        """
        # for integers
        print(round(10))
        # for floating point
        print(round(10.7))
        # even choice
        print(round(5.5))
        print(round(2.665, 2))
        # cannot be represented exactly as float
        print(round(2.675, 2))
        return
        
    def set_test(self, *args, **kwargs):
        """
        Return a new set object, optionally with elements taken from iterable. 
        set is a built-in class. See set and Set Types — set, frozenset for 
        documentation about this class.
        """
        # empty set
        print(set())
        # from string
        print(set('Python'))
        # from tuple
        print(set(('a', 'e', 'i', 'o', 'u')))
        # from list
        print(set(['a', 'e', 'i', 'o', 'u']))
        # from range
        print(set(range(5)))
        # for set
        print(set({'a', 'e', 'i', 'o', 'u'}))
        # from dictionary
        print(set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}))
        # from frozen set
        frozenSet = frozenset(('a', 'e', 'i', 'o', 'u'))
        print(set(frozenSet))
        class PrintNumber:
            def __init__(self, max):
                self.max = max
            def __iter__(self):
                self.num = 0
                return self
            def __next__(self):
                if(self.num >= self.max):
                    raise StopIteration
                self.num += 1
                return self.num
        printNum = PrintNumber(5)
        # creating a set
        print(set(printNum))
        return
        
    def setattr_test(self, *args, **kwargs):
        """
        This is the counterpart of getattr(). The arguments are an object, a 
        string and an arbitrary value. The string may name an existing 
        attribute or a new attribute. The function assigns the value to the 
        attribute, provided the object allows it. For example, 
        setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
        """
        class Person:
            name = 'Adam'
        p = Person()
        print('Before modification:', p.name)
        # setting name to 'John'
        setattr(p, 'name', 'John')
        print('After modification:', p.name)
        class Person:
            name = 'Adam'
        p = Person()
        # setting attribute name to None
        setattr(p, 'name', None)
        print('Name is:', p.name)
        # setting an attribute not present
        # in Person
        setattr(p, 'age', 23)
        print('Age is:', p.age)
        return
        
    def slice_test(self, *args, **kwargs):
        """
        Return a slice object representing the set of indices specified by 
        range(start, stop, step). The start and step arguments default to 
        None. Slice objects have read-only data attributes start, stop and 
        step which merely return the argument values (or their default). They 
        have no other explicit functionality; however they are used by 
        Numerical Python and other third party extensions. Slice objects are 
        also generated when extended indexing syntax is used. For example: 
            a[start:stop:step] or a[start:stop, i]. 
        See itertools.islice() for an alternate version that returns an 
        iterator.
        """
        # contains indices (0, 1, 2)
        print(slice(3))
        # contains indices (1, 3)
        print(slice(1, 5, 2))
        pyString = 'Python'
        # contains indices (0, 1, 2)
        # i.e. P, y and t
        sObject = slice(3)
        print(pyString[sObject])
        # contains indices (1, 3)
        # i.e. y and h
        sObject = slice(1, 5, 2)
        print(pyString[sObject])
        pyString = 'Python'
        # contains indices (-1, -2, -3)
        # i.e. n, o and h
        sObject = slice(-1, -4, -1)
        print(pyString[sObject])
        pyList = ['P', 'y', 't', 'h', 'o', 'n']
        pyTuple = ('P', 'y', 't', 'h', 'o', 'n')
        # contains indices (0, 1, 2)
        # i.e. P, y and t
        sObject = slice(3)
        # slice a list
        print(pyList[sObject])
        # contains indices (1, 3)
        # i.e. y and h
        sObject = slice(1, 5, 2)
        # slice a tuple
        print(pyTuple[sObject])
        # contains indices (-1, -2, -3)
        # i.e. n, o and h
        sObject = slice(-1, -4, -1)
        # slice a list
        print(pyList[sObject])
        # contains indices (-1, -3)
        # i.e. n and h
        sObject = slice(-1, -5, -2)
        # slice a tuple
        print(pyTuple[sObject])
        pyString = 'Python'
        # contains indices (0, 1, 2)
        # i.e. P, y and t
        print(pyString[0:3])
        # contains indices (1, 3)
        # i.e. y and h
        print(pyString[1:5:2])
        return
        
    def sorted_test(self, *args, **kwargs):
        """
        Return a new sorted list from the items in iterable.
        Has two optional arguments which must be specified as keyword 
        arguments.
        key specifies a function of one argument that is used to extract a 
        comparison key from each element in iterable (for example, 
        key=str.lower). The default value is None (compare the elements 
        directly).
        reverse is a boolean value. If set to True, then the list elements are 
        sorted as if each comparison were reversed.
        Use functools.cmp_to_key() to convert an old-style cmp function to a 
        key function.
        The built-in sorted() function is guaranteed to be stable. A sort is 
        stable if it guarantees not to change the relative order of elements 
        that compare equal — this is helpful for sorting in multiple passes 
        (for example, sort by department, then by salary grade).
        """
        # vowels list
        pyList = ['e', 'a', 'u', 'o', 'i']
        print(sorted(pyList))
        # string 
        pyString = 'Python'
        print(sorted(pyString))
        # vowels tuple
        pyTuple = ('e', 'a', 'u', 'o', 'i')
        print(sorted(pyTuple))
        # set
        pySet = {'e', 'a', 'u', 'o', 'i'}
        print(sorted(pySet, reverse=True))
        # dictionary
        pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
        print(sorted(pyDict, reverse=True))
        # frozen set
        pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
        print(sorted(pyFSet, reverse=True))
        # take second element for sort
        def takeSecond(elem):
            return elem[1]
        # random list
        random = [(2, 2), (3, 4), (4, 1), (1, 3)]
        # sort list with key
        sortedList = sorted(random, key=takeSecond)
        # print list
        print('Sorted list:', sortedList)
        return
        
    def staticmethod_test(self, *args, **kwargs):
        """
        Transform a method into a static method.
        A static method does not receive an implicit first argument.
        The @staticmethod form is a function decorator – see the description 
        of function definitions in Function definitions for details.
        It can be called either on the class (such as C.f()) or on an instance 
        (such as C().f()). The instance is ignored except for its class.
        Static methods in Python are similar to those found in Java or C++. 
        Also see classmethod() for a variant that is useful for creating 
        alternate class constructors.
        Like all decorators, it is also possible to call staticmethod as a 
        regular function and do something with its result. This is needed in 
        some cases where you need a reference to a function from a class body 
        and you want to avoid the automatic transformation to instance method.
        """
        class Mathematics:
        
            def addNumbers(x, y):
                return x + y
        # create addNumbers static method
        Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
        print('The sum is:', Mathematics.addNumbers(5, 10))
        class Dates:
            def __init__(self, date):
                self.date = date
                
            def getDate(self):
                return self.date
        
            @staticmethod
            def toDashDate(date):
                return date.replace("/", "-")
        date = Dates("15-12-2016")
        dateFromDB = "15/12/2016"
        dateWithDash = Dates.toDashDate(dateFromDB)
        
        if date.getDate() == dateWithDash:
            print("Equal")
        else:
            print("Unequal")
            
        class Dates:
            def __init__(self, date):
                self.date = date
                
            def getDate(self):
                return self.date
        
            @staticmethod
            def toDashDate(date):
                return date.replace("/", "-")
        
        class DatesWithSlashes(Dates):
            def getDate(self):
                return Dates.toDashDate(self.date)
        
        date = Dates("15-12-2016")
        dateFromDB = DatesWithSlashes("15/12/2016")
        
        if(date.getDate() == dateFromDB.getDate()):
            print("Equal")
        else:
            print("Unequal")
                        
    def str_test(self, *args, **kwargs):
        """
        The str() method returns the "informal" or nicely printable 
        representation of a given object.
        The str() method mainly takes three parameters which are same for both 
        constructs:
        object - object whose informal representation is to be returned
        encoding - Defaults of UTF-8. Encoding of the given object
        errors - response when decoding fails. There are six types of error 
        response
        strict - default response which raises a UnicodeDecodeError exception 
        on failure
        ignore - ignores the unencodable unicode from the result
        replace - replaces the unencodable unicode to a question mark ?
        xmlcharrefreplace - inserts XML character reference instead of 
        unencodable unicode
        backslashreplace - inserts a \\uNNNN espace sequence instead of 
        unencodable unicode
        namereplace - inserts a \\N{...} escape sequence instead of unencodable 
        unicode
        """
        print(str(10))
        # bytes
        b = bytes('pythön', encoding='utf-8')
        print(str(b, encoding='ascii', errors='ignore'))
        return
        
    def sum_test(self, *args, **kwargs):
        """
        Sums start and the items of an iterable from left to right and returns 
        the total. start defaults to 0. The iterable’s items are normally 
        numbers, and the start value is not allowed to be a string.
        For some use cases, there are good alternatives to sum(). The 
        preferred, fast way to concatenate a sequence of strings is by calling 
        ''.join(sequence). To add floating point values with extended 
        precision, see math.fsum(). To concatenate a series of iterables, 
        consider using itertools.chain().
        """
        numbers = [2.5, 3, 4, -5]
        # start parameter is not provided
        numbersSum = sum(numbers)
        print(numbersSum)
        # start = 10
        numbersSum = sum(numbers, 10)
        print(numbersSum)
        print(''.join(['wer', 'we','er']))
        return
        
    def super_test(self, *args, **kwargs):
        """
        Return a proxy object that delegates method calls to a parent or 
        sibling class of type. This is useful for accessing inherited methods 
        that have been overridden in a class. The search order is same as that 
        used by getattr() except that the type itself is skipped.
        The __mro__ attribute of the type lists the method resolution search 
        order used by both getattr() and super(). The attribute is dynamic and 
        can change whenever the inheritance hierarchy is updated.
        If the second argument is omitted, the super object returned is 
        unbound. If the second argument is an object, isinstance(obj, type) 
        must be true. If the second argument is a type, 
        issubclass(type2, type) must be true (this is useful for classmethods).        
        There are two typical use cases for super. In a class hierarchy with 
        single inheritance, super can be used to refer to parent classes 
        without naming them explicitly, thus making the code more maintainable. 
        This use closely parallels the use of super in other programming 
        languages.
        The second use case is to support cooperative multiple inheritance in 
        a dynamic execution environment. This use case is unique to Python and 
        is not found in statically compiled languages or languages that only 
        support single inheritance. This makes it possible to implement 
        “diamond diagrams” where multiple base classes implement the same 
        method. Good design dictates that this method have the same calling 
        signature in every case (because the order of calls is determined at 
        runtime, because that order adapts to changes in the class hierarchy, 
        and because that order can include sibling classes that are unknown 
        prior to runtime).
        Note that super() is implemented as part of the binding process for 
        explicit dotted attribute lookups such as super().__getitem__(name). 
        It does so by implementing its own __getattribute__() method for 
        searching classes in a predictable order that supports cooperative 
        multiple inheritance. Accordingly, super() is undefined for implicit 
        lookups using statements or operators such as super()[name].
        Also note that, aside from the zero argument form, super() is not 
        limited to use inside methods. The two argument form specifies the 
        arguments exactly and makes the appropriate references. The zero 
        argument form only works inside a class definition, as the compiler 
        fills in the necessary details to correctly retrieve the class being 
        defined, as well as accessing the current instance for ordinary 
        methods.
        """
        class Mammal(object):
          def __init__(self, mammalName):
            print(mammalName, 'is a warm-blooded animal.')
        class Dog(Mammal):
          def __init__(self):
            print('Dog has four legs.')
            super().__init__('Dog')
        d1 = Dog()
        
        class Animal:
          def __init__(self, animalName):
            print(animalName, 'is an animal.')
        class Mammal(Animal):
          def __init__(self, mammalName):
            print(mammalName, 'is a warm-blooded animal.')
            super().__init__(mammalName)
            
        class NonWingedMammal(Mammal):
          def __init__(self, NonWingedMammalName):
            print(NonWingedMammalName, "can't fly.")
            super().__init__(NonWingedMammalName)
        
        class NonMarineMammal(Mammal):
          def __init__(self, NonMarineMammalName):
            print(NonMarineMammalName, "can't swim.")
            super().__init__(NonMarineMammalName)
        
        class Dog(NonMarineMammal, NonWingedMammal):
          def __init__(self):
            print('Dog has 4 legs.');
            super().__init__('Dog')
            
        d = Dog()
        print(Dog.__mro__)
        bat = NonMarineMammal('Bat')
        return
        
    def  tuple_test(self, *args, **kwargs):
        """
        The tuple() built-in is used to create a tuple in Python.
        In Python, a tuple is an immutable sequence type.
        One of ways of creating tuple is by using tuple() built-in.
        """
        t1 = tuple()
        print('t1=', t1)
        # creating a tuple from a list
        t2 = tuple([1, 4, 6])
        print('t2=', t2)
        # creating a tuple from a string
        t1 = tuple('Python')
        print('t1=',t1)
        print(''.join(t1))
        # creating a tuple from a dictionary
        t1 = tuple({1: 'one', 2: 'two'})
        print('t1=',t1)
        return
        
    def type_test(self, *args, **kwargs):
        """
        With one argument, return the type of an object. The return value is a 
        type object and generally the same object as returned by 
        object.__class__.
        The isinstance() built-in function is recommended for testing the type 
        of an object, because it takes subclasses into account.
        With three arguments, return a new type object. This is essentially a 
        dynamic form of the class statement. The name string is the class name 
        and becomes the __name__ attribute; the bases tuple itemizes the base 
        classes and becomes the __bases__ attribute; and the dict dictionary 
        is the namespace containing definitions for class body and is copied 
        to a standard dictionary to become the __dict__ attribute.
        """
        numberList = [1, 2]
        print(type(numberList))
        numberDict = {1: 'one', 2: 'two'}
        print(type(numberDict))
        class Foo:
            a = 0
        InstanceOfFoo = Foo()
        print(type(InstanceOfFoo))
        o1 = type('X', (object,), dict(a='Foo', b=12))
        print(type(o1))
        print(vars(o1))
        
        class test:
          a = 'Foo'
          b = 12
          
        o2 = type('Y', (test,), dict(a='Foo', b=12))
        print(type(o2))
        print(vars(o2))
        return
        
    def vars_test(self, *args, **kwargs):
        """
        Return the __dict__ attribute for a module, class, instance, or any 
        other object with a __dict__ attribute.
        Objects such as modules and instances have an updateable __dict__ 
        attribute; however, other objects may have write restrictions on their 
        __dict__ attributes (for example, classes use a types.MappingProxyType 
        to prevent direct dictionary updates).
        Without an argument, vars() acts like locals(). Note, the locals 
        dictionary is only useful for reads since updates to the locals 
        dictionary are ignored.
        """
        class Foo:
            def __init__(self, a = 5, b = 10):
                self.a = a
                self.b = b
            def sum_func(self):
                return self.a + self.b
          
        InstanceOfFoo = Foo()
        print(vars(InstanceOfFoo))
        print(vars(list))
        return
        
    def zip_test(self, *args, **kwargs):
        """
        Make an iterator that aggregates elements from each of the iterables.
        Returns an iterator of tuples, where the i-th tuple contains the i-th 
        element from each of the argument sequences or iterables. The iterator 
        stops when the shortest input iterable is exhausted. With a single 
        iterable argument, it returns an iterator of 1-tuples. With no 
        arguments, it returns an empty iterator.
        The left-to-right evaluation order of the iterables is guaranteed. 
        This makes possible an idiom for clustering a data series into 
        n-length groups using zip(*[iter(s)]*n). This repeats the same 
        iterator n times so that each output tuple has the result of n calls 
        to the iterator. This has the effect of dividing the input into 
        n-length chunks.
        zip() should only be used with unequal length inputs when you don’t 
        care about trailing, unmatched values from the longer iterables. If 
        those values are important, use itertools.zip_longest() instead.
        """
        numberList = [1, 2, 3]
        strList = ['one', 'two', 'three']
        # No iterables are passed
        result = zip()
        # Converting itertor to list
        resultList = list(result)
        print(resultList)
        # Two iterables are passed
        result = zip(numberList, strList)
        print(result)
        # Converting itertor to set
        resultSet = set(result)
        print(resultSet)
        
        numbersList = [1, 2, 3]
        strList = ['one', 'two']
        numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
        result = zip(numbersList, numbersTuple)
        # Converting to set
        resultSet = set(result)
        print(resultSet)
        result = zip(numbersList, strList, numbersTuple)
        # Converting to set
        resultSet = set(result)
        print(resultSet)
        
        coordinate = ['x', 'y', 'z']
        value = [3, 4, 5, 0, 9]
        result = zip(coordinate, value)
        resultList = list(result)
        print(resultList)
        c, v =  zip(*resultList)
        print('c =', c)
        print('v =', v)
        return
        
    def import_test(self, *args, **kwargs):
        """
        Note:
        This is an advanced function that is not needed in everyday Python 
        programming, unlike importlib.import_module().
        This function is invoked by the import statement. It can be replaced 
        (by importing the builtins module and assigning to 
        builtins.__import__) in order to change semantics of the import 
        statement, but doing so is strongly discouraged as it is usually 
        simpler to use import hooks (see PEP 302) to attain the same goals and 
        does not cause issues with code which assumes the default import 
        implementation is in use. Direct use of __import__() is also 
        discouraged in favor of importlib.import_module().
        The function imports the module name, potentially using the given 
        globals and locals to determine how to interpret the name in a package 
        context. The fromlist gives the names of objects or submodules that 
        should be imported from the module given by name. The standard 
        implementation does not use its locals argument at all, and uses its 
        globals only to determine the package context of the import statement.        
        level specifies whether to use absolute or relative imports. 0 (the 
        default) means only perform absolute imports. Positive values for 
        level indicate the number of parent directories to search relative to 
        the directory of the module calling __import__() (see PEP 328 for the 
        details).
        When the name variable is of the form package.module, normally, the 
        top-level package (the name up till the first dot) is returned, not 
        the module named by name. However, when a non-empty fromlist argument 
        is given, the module named by name is returned.
        """
        mathematics = __import__('math', globals(), locals(), [], 0)
        print(mathematics.fabs(-2.5))
                
        
        
if __name__=='__main__':
    """
    Uncomment the function which you want to test.
    """
    bif = BuiltInFunctions()
    
    # abs(x)
    print('\n# abs(x)')
    #bif.abs_test()
    
    # all(itr)
    print('\n# all(itr)')
    #bif.all_test()
    
    # any(itr)
    print('\n# any(itr)')
    #bif.any_test()    
    
    # ascii(object)
    print('\n# ascii(object)')
    #bif.ascii_test()
    
    # bin(x)
    print('\n# bin(x)')
    #bif.bin_test()
    
    # bool([x])
    print('\n# bool([x])')
    #bif.bool_test()
    
    # breakpoint(*args, **kws)
    print('\n# breakpoint(*args, **kws)')
    #bif.breakpoint_test()
    
    # bytearray([source[, encoding[, errors]]])
    print('\n# bytearray([source[, encoding[, errors]]])')
    #bif.bytearray_test()
    
    # bytes([source[, encoding[, errors]]])
    print('\n# bytes([source[, encoding[, errors]]])')
    #bif.bytes_test()
    
    # callable(object)
    print('\n# callable(object)')
    #bif.callable_test()
    
    # chr(i)
    print('\n# chr(i)')
    #bif.chr_test()
    
    # @classmethod
    print('\n# @classmethod')
    #bif.classmethod_test()
    
    # compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    print('\n# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)')
    #bif.compile_test()
    
    # complex([real[, imag]])
    print('\n# complex([real[, imag]])')
    #bif.complex_test()
    
    # delattr(object, name)
    print('\n# delattr(object, name)')
    #bif.delattr_test()
    
    # dict(**kwarg)
    # dict(mapping, **kwarg)
    # dict(iterable, **kwarg)
    print('\n# dict(**kwarg)\n# dict(mapping, **kwarg)\n# dict(iterable, **kwarg)')
    #bif.dict_test()
    
    # dir([object])
    print('\n# dir([object])')
    #bif.dir_test()
    
    # divmod(a, b)
    print('\n# divmod(a, b)')
    #bif.divmod_test()
    
    # enumerate(iterable, start=0)
    print('\n# enumerate(iterable, start=0)')
    #bif.enumerate_test()
    
    # eval(expression, globals=None, locals=None)
    print('\n# eval(expression, globals=None, locals=None)')
    #bif.eval_test()
    
    # exec(object[, globals[, locals]])
    print('\n# exec(object[, globals[, locals]])')
    #bif.exec_test()
    
    # filter(function, iterable)
    print('\n# filter(function, iterable)')
    #bif.filter_test()
    
    # float([x])
    print('\n# float([x])')
    #bif.float_test()
    
    # format(value[, format_spec])
    print('\n# format(value[, format_spec])')
    #bif.format_test()
    
    # frozenset([iterable])
    print('\n# frozenset([iterable])')
    #bif.frozenset_test()
    
    # getattr(object, name[, default])
    print('\n# getattr(object, name[, default])')
    #bif.getattr_test()
    
    # globals()
    print('\n# globals()')
    #bif.globals_test()
    
    # hasattr(object, name)
    print('\n# hasattr(object, name)')
    #bif.hasattr_test()
    
    # hash(object)
    print('\n# hash(object)')
    #bif.hash_test()
    
    # help([object])
    print('\n# help([object])')
    #bif.help_test()
    
    # hex(x)
    print('\n# hex(x)')
    #bif.hex_test()
    
    # id(object)
    print('\n# id(object)')
    #bif.id_test()
    
    # input([prompt])
    print('\n# input([prompt])')
    #bif.input_test()
    
    # int([x])
    # int(x, base=10)
    print('\n# int([x])\n# int(x, base=10)')
    #bif.int_test()
    
    # isinstance(object, classinfo)
    print('\n# isinstance(object, classinfo)')
    #bif.isinstance_test()   
    
    # issubclass(class, classinfo)
    print('\n# issubclass(class, classinfo)')
    #bif.issubclass_test()
    
    # iter(object[, sentinel])
    print('\n# iter(object[, sentinel])')
    #bif.iter_test()
    
    # len(s)
    print('\n# len(s)')
    #bif.len_test()
    
    # list([iterable])
    print('\n# list([iterable])')
    #bif.list_test()
    
    # locals()
    print('\n# locals()')
    #bif.locals_test()
    
    # map(function, iterable, ...)
    print('\n# map(function, iterable, ...)')
    #bif.map_test()
    
    # max(iterable, *[, key, default])
    # max(arg1, arg2, *args[, key])
    print('\n# max(iterable, *[, key, default])\n# max(arg1, arg2, *args[, key])')
    #bif.max_test()
    
    # memoryview(obj)
    print('\n# memoryview(obj)')
    #bif.memoryview_test()
    
    # min(iterable, *[, key, default])
    # min(arg1, arg2, *args[, key])
    print('\n# min(iterable, *[, key, default])\n# min(arg1, arg2, *args[, key])')
    #bif.min_test()
    
    # next(iterator[, default])
    print('\n# next(iterator[, default])')
    #bif.next_test()
    
    # object
    print('\n# object')
    #bif.object_test()
    
    # oct(x)
    print('\n# oct(x)')
    #bif.oct_test()
    
    # open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    print('\n# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)')
    #bif.open_test()
    
    # ord(c)
    print('\n# ord(c)')
    #bif.ord_test()
    
    # pow(x, y[, z])
    print('\n# pow(x, y[, z])')
    #bif.pow_test()
    
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    print('\n# print(*objects, sep=" ", end="\\n", file=sys.stdout, flush=False)')
    #bif.print_test()
    
    # property(fget=None, fset=None, fdel=None, doc=None)
    print('\n# property(fget=None, fset=None, fdel=None, doc=None)')
    #bif.property_test()
    
    # range(stop)
    # range(start, stop[, step])
    print('\n# range(stop)\n# range(start, stop[, step])')
    #bif.range_test()
    
    # repr(object)
    print('\n# repr(object)')
    #bif.repr_test()
    
    # reversed(seq)
    print('\n# reversed(seq)')
    #bif.reversed_test()
    
    # round(number[, ndigits])
    print('\n# round(number[, ndigits])')
    #bif.round_test()
    
    # set([iterable])
    print('\n# set([iterable])')
    #bif.set_test()
    
    # setattr(object, name, value)
    print('\n# setattr(object, name, value)')
    #bif.setattr_test()
    
    # slice(stop)
    # slice(start, stop[, step])
    print('\n# slice(stop)\n# slice(start, stop[, step])')
    #bif.slice_test()
    
    # sorted(iterable, *, key=None, reverse=False)
    print('\n# sorted(iterable, *, key=None, reverse=False)')
    #bif.sorted_test()
    
    # @staticmethod
    print('\n# @staticmethod')
    #bif.staticmethod_test()
    
    # str(object='')
    # str(object=b'', encoding='utf-8', errors='strict')
    print("\n# str(object='')\n# str(object=b'', encoding='utf-8', errors='strict')")
    #bif.str_test()
    
    # sum(iterable[, start])
    print('\n# sum(iterable[, start])')
    #bif.sum_test()
    
    # super([type[, object-or-type]])
    print('\n# super([type[, object-or-type]])')
    #bif.super_test()
    
    # tuple([iterable])
    print('\n# tuple([iterable])')
    #bif.tuple_test()
    
    # type(object)
    # type(name, bases, dict)
    print('\n# type(object)\n# type(name, bases, dict)')
    #bif.type_test()
    
    # vars([object])
    print('\n# vars([object])')
    #bif.vars_test()
    
    # zip(*iterables)
    print('\n# zip(*iterables)')
    #bif.zip_test()
    
    # __import__(name, globals=None, locals=None, fromlist=(), level=0)
    print('\n# __import__(name, globals=None, locals=None, fromlist=(), level=0)')
    #bif.import_test()
    
    
    
    
    
    
    
    
    
    
    
    