# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:31:24 2019

@author: Rajesh Samui
"""

class BuiltInType:
    """
    Built in Types
    """
    def __init__(self):
        pass
    
    def boolean_test(self, *args, **kwargs):
        """
        Here are most of the built-in objects considered false:
        constants defined to be false: None and False.
        zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        empty sequences and collections: '', (), [], {}, set(), range(0)
        This table summarizes the comparison operations:
        Operation 	Meaning
        < 	    strictly less than
        <= 	    less than or equal
        > 	    strictly greater than
        >= 	    greater than or equal
        == 	    equal
        != 	    not equal
        is 	    object identity
        is not     negated object identity
        """
        print('4 < 5:',4 < 5)
        print('type of 4 < 5:',type(4 < 5))
        print('bool(2014):',bool(2014))
        print('bool(0):',bool(0))
        print('bool(3.1415):',bool(3.1415))
        print('bool(None):',bool(None))
        print('bool(""):',bool(""))
        print('bool("abc"):',bool("abc"))
        print('bool([1, 2, 3]):',bool([1, 2, 3]))
        return
        
    def numeric_test(self, *args, **kwargs):
        """
        All numeric types (except complex) support the following operations, 
        sorted by ascending priority (all numeric operations have a higher 
        priority than comparison operations):
        Operation 	            Result
        x + y 	                 sum of x and y 	  	 
        x - y 	                 difference of x and y 	  	 
        x * y 	                 product of x and y 	  	 
        x / y 	                 quotient of x and y 	  	 
        x // y 	            floored quotient of x and y 	 	 
        x % y 	                 remainder of x / y 	 	 
        -x 	                 x negated 	  	 
        +x 	                 x unchanged 	  	 
        abs(x) 	            absolute value or magnitude of x
        int(x) 	            x converted to integer
        float(x) 	            x converted to floating point
        complex(re, im) 	       a complex number with real part re, imaginary part im. im defaults to zero.
        c.conjugate() 	       conjugate of the complex number c 	  	 
        divmod(x, y) 	       the pair (x // y, x % y)
        pow(x, y) 	            x to the power y
        x ** y 	            x to the power y
        
        Notes:
        Also referred to as integer division. The resultant value is a whole 
        integer, though the result’s type is not necessarily int. The result 
        is always rounded towards minus infinity: 1//2 is 0, (-1)//2 is -1, 
        1//(-2) is -1, and (-1)//(-2) is 0.
        Not for complex numbers. Instead convert to floats using abs() if 
        appropriate.
        Conversion from floating point to integer may round or truncate as in 
        C; see functions math.floor() and math.ceil() for well-defined 
        conversions.
        float also accepts the strings “nan” and “inf” with an optional prefix 
        “+” or “-” for Not a Number (NaN) and positive or negative infinity.
        Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for 
        programming languages.
        The numeric literals accepted include the digits 0 to 9 or any Unicode 
        equivalent (code points with the Nd property).
        
        All numbers.Real types (int and float) also include the following 
        operations:
        Operation 	     Result
        math.trunc(x) 	x truncated to Integral
        round(x[, n]) 	x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0.
        math.floor(x) 	the greatest Integral <= x
        math.ceil(x) 	the least Integral >= x

        Operation 	Result 	                         Notes
        x | y 	     bitwise or of x and y 	          (4)
        x ^ y 	     bitwise exclusive or of x and y 	(4)
        x & y 	     bitwise and of x and y 	          (4)
        x << n 	x shifted left by n bits 	     (1)(2)
        x >> n 	x shifted right by n bits 	     (1)(3)
        ~x 	     the bits of x inverted
        
        Notes:
        Negative shift counts are illegal and cause a ValueError to be raised.
        A left shift by n bits is equivalent to multiplication by pow(2, n) 
        without overflow check.
        A right shift by n bits is equivalent to division by pow(2, n) without 
        overflow check.
        Performing these calculations with at least one extra sign extension 
        bit in a finite two’s complement representation (a working bit-width 
        of 1 + max(x.bit_length(), y.bit_length()) or more) is sufficient to 
        get the same result as if there were an infinite number of sign bits.
        """
        import sys, math, decimal, fractions, itertools
        print('sys.float_info:',sys.float_info)
        print('\nint():',int('4'), type(int('4')))
        print('float():',float('4.0'),float('-nan'),float('-inf'), type(float('4.0')))
        print('complex():',complex(1+5j),complex('1+5j'),type(complex('1+5j')))
        print('abs(x):',abs(+4),abs(-4),abs(+4.0),abs(-4.0),abs(4+3j),abs(4-3j),abs(-4+3j),abs(-4-3j))
        print('c.conjugate():',complex(3,4).conjugate(), complex(3,-4).conjugate(), complex(-3,4).conjugate(),complex(-3,-4).conjugate())
        print('divmod(x, y):',divmod(13,5))
        print('pow(x, y):',pow(4, 3))
        print('math.floor():', math.floor(4.33),math.floor(4.77))
        print('math.ceil():',math.ceil(4.33),math.ceil(4.77))
        print('math.trunc(x):',math.trunc(3.4)) # work as floor
        x = -55
        print('bin(x):',bin(x))
        print('x.bit_length():',x.bit_length())
        print('int.to_bytes(length, byteorder, *, signed=False):',(1000).to_bytes((1000).bit_length(), byteorder='big'))
        print('byteorder:', sys.byteorder)
        print('int.to_bytes(length, byteorder, *, signed=False):',(1000).to_bytes((1000).bit_length(), byteorder=sys.byteorder)) # byteorder: little, big
        print('int.from_bytes(bytes, byteorder, *, signed=False)',int.from_bytes(b'\x00\x10', byteorder='big'))
        print('int.from_bytes(bytes, byteorder, *, signed=False)',int.from_bytes((1000).to_bytes((1000).bit_length(), byteorder=sys.byteorder), byteorder=sys.byteorder))
        print('float.as_integer_ratio():',(2/3).as_integer_ratio())
        print('(-2.0).is_integer():',(-2.0).is_integer())
        print('(3.2).is_integer():',(3.2).is_integer())
        print('(2.3).hex():',(2.3).hex())
        print('float.fromhex((2.3).hex()):',float.fromhex((2.3).hex()))
        print('decimal.Decimal("3.43"):',decimal.Decimal('3.43'), ', type:',type(decimal.Decimal('3.43')))
        print('Fraction(16, -10):',fractions.Fraction(16, -10))
        print('Fraction(Decimal("1.1")):',fractions.Fraction(decimal.Decimal('1.1')))
        def modInverse(a, m) : 
            a = a % m; 
            for x in range(1, m) : 
                if ((a * x) % m == 1) : 
                    return x 
            return 1
          
        # Driver Program 
        a = 3
        m = 11
        print('modInverse(a, m):',modInverse(a, m))
        
        import sys, math

        def hash_fraction(m, n):
            """Compute the hash of a rational number m / n.
        
            Assumes m and n are integers, with n positive.
            Equivalent to hash(fractions.Fraction(m, n)).
        
            """
            P = sys.hash_info.modulus
            # Remove common factors of P.  (Unnecessary if m and n already coprime.)
            while m % P == n % P == 0:
                m, n = m // P, n // P
        
            if n % P == 0:
                hash_value = sys.hash_info.inf
            else:
                # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
                # pow(n, P-2, P) gives the inverse of n modulo P.
                hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
            if m < 0:
                hash_value = -hash_value
            if hash_value == -1:
                hash_value = -2
            return hash_value
        
        def hash_float(x):
            """Compute the hash of a float x."""
        
            if math.isnan(x):
                return sys.hash_info.nan
            elif math.isinf(x):
                return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
            else:
                return hash_fraction(*x.as_integer_ratio())
        
        def hash_complex(z):
            """Compute the hash of a complex number z."""
        
            hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
            # do a signed reduction modulo 2**sys.hash_info.width
            M = 2**(sys.hash_info.width - 1)
            hash_value = (hash_value & (M - 1)) - (hash_value & M)
            if hash_value == -1:
                hash_value = -2
            return hash_value
            
        print('hash_fraction(m, n):',hash_fraction(3, 4))
        print('hash_float(x):',hash_float(5.8))
        print('hash_complex(z):',hash_complex(6+7j))
        return
        
    def iterator_test(self, *args, **kwargs):
        """
        Python supports a concept of iteration over containers. This is 
        implemented using two distinct methods; these are used to allow 
        user-defined classes to support iteration. Sequences, described below 
        in more detail, always support the iteration methods.
        One method needs to be defined for container objects to provide 
        iteration support:
        container.__iter__()
            Return an iterator object. The object is required to support the 
            iterator protocol described below. If a container supports 
            different types of iteration, additional methods can be provided 
            to specifically request iterators for those iteration types. (An 
            example of an object supporting multiple forms of iteration would 
            be a tree structure which supports both breadth-first and 
            depth-first traversal.) This method corresponds to the tp_iter 
            slot of the type structure for Python objects in the Python/C API.        
        The iterator objects themselves are required to support the following 
        two methods, which together form the iterator protocol:
        iterator.__iter__()
            Return the iterator object itself. This is required to allow both 
            containers and iterators to be used with the for and in statements. 
            This method corresponds to the tp_iter slot of the type structure 
            for Python objects in the Python/C API.
        iterator.__next__()
            Return the next item from the container. If there are no further 
            items, raise the StopIteration exception. This method corresponds 
            to the tp_iternext slot of the type structure for Python objects 
            in the Python/C API.
        Python defines several iterator objects to support iteration over 
        general and specific sequence types, dictionaries, and other more 
        specialized forms. The specific types are not important beyond their 
        implementation of the iterator protocol.
        Once an iterator’s __next__() method raises StopIteration, it must 
        continue to do so on subsequent calls. Implementations that do not 
        obey this property are deemed broken.
        """
        # define a list
        my_list = [4, 7, 0, 3]
        # get an iterator using iter()
        my_iter = iter(my_list)
        ## iterate through it using next() 
        #prints 4
        print('next(my_iter)',next(my_iter))
        #prints 7
        print('next(my_iter)',next(my_iter))
        ## next(obj) is same as obj.__next__()
        #prints 0
        print('my_iter.__next__()',my_iter.__next__())
        #prints 3
        print('my_iter.__next__()',my_iter.__next__())
        try:
            ## This will raise error, no items left
            next(my_iter)
        except Exception as e:
            print('StopIteration Exception')
        for element in my_list:
            print(element)
            
        class PowTwo:
            """Class to implement an iterator
            of powers of two"""
        
            def __init__(self, max = 0):
                self.max = max
        
            def __iter__(self):
                self.n = 0
                return self
        
            def __next__(self):
                if self.n <= self.max:
                    result = 2 ** self.n
                    self.n += 1
                    return result
                else:
                    raise StopIteration
                    
        a = PowTwo(4)
        i = iter(a)
        print('next(i):',next(i))
        print('next(i):',next(i))
        print('next(i):',next(i))
        print('next(i):',next(i))
        print('next(i):',next(i))
        try:
            print('next(i):',next(i))
        except Exception as e:
            print('StopIteration Exception')
        for i in PowTwo(5):
            print(i)
        print('int():',int())
        inf = iter(int,1)
        print('next(inf):',next(inf))
        print('next(inf):',next(inf))
        print('next(inf):',next(inf))
        print('next(inf):',next(inf))
        
        class InfIter:
            """Infinite iterator to return all
                odd numbers"""
        
            def __iter__(self):
                self.num = 1
                return self
        
            def __next__(self):
                num = self.num
                self.num += 2
                return num
                
        a = iter(InfIter())
        print('next(a):',next(a))
        print('next(a):',next(a))
        print('next(a):',next(a))
        print('next(a):',next(a))
        return
        
    def generator_test(self, *args, **kwargs):
        """
        Python’s generators provide a convenient way to implement the iterator 
        protocol. If a container object’s __iter__() method is implemented as 
        a generator, it will automatically return an iterator object 
        (technically, a generator object) supplying the __iter__() and 
        __next__() methods.
        It is fairly simple to create a generator in Python. It is as easy as 
        defining a normal function with yield statement instead of a return 
        statement.
        If a function contains at least one yield statement (it may contain 
        other yield or return statements), it becomes a generator function. 
        Both yield and return will return some value from a function.
        The difference is that, while a return statement terminates a function 
        entirely, yield statement pauses the function saving all its states 
        and later continues from there on successive calls.
        """
        # A simple generator function
        def my_gen():
            n = 1
            print('This is printed first')
            # Generator function contains yield statements
            yield n
        
            n += 1
            print('This is printed second')
            yield n
        
            n += 1
            print('This is printed at last')
            yield n
            
        # It returns an object but does not start execution immediately.
        a = my_gen()
        # We can iterate through the items using next().
        next(a)
        next(a)
        next(a)
        try:
            next(a)
        except StopIteration as e:
            print('StopIteration Exception')
        print('\nmy_gen():')
        # A simple generator function
        def my_gen():
            n = 1
            print('This is printed first')
            # Generator function contains yield statements
            yield n
        
            n += 1
            print('This is printed second')
            yield n
        
            n += 1
            print('This is printed at last')
            yield n
        
        # Using for loop
        for item in my_gen():
            print(item)
        print('\nrev_str(my_str):')
        def rev_str(my_str):
            length = len(my_str)
            for i in range(length - 1,-1,-1):
                yield my_str[i]
        
        for char in rev_str("hello"):
             print(char)
        
        import time
        # Initialize the list
        my_list = [1, 3, 6, 10]

        tfp = time.time()
        for x in my_list:
            x**2
        tfa = time.time()
        print('for loop:',tfa-tfp)
        
        # square each term using list comprehension
        # Output: [1, 9, 36, 100]
        tlp = time.time()
        [x**2 for x in my_list]
        tla = time.time()
        print('list comprehention:',tla-tlp)
        
        # same thing can be done using generator expression
        # Output: <generator object <genexpr> at 0x0000000002EBDAF8>
        tgp = time.time()
        (x**2 for x in my_list)
        tga = time.time()
        print('generator expression:',tga-tgp)
        
        """
        We can see above that the generator expression did not produce the 
        required result immediately. Instead, it returned a generator object 
        with produces items on demand.
        """
        # Intialize the list
        my_list = [1, 3, 6, 10]
        a = (x**2 for x in my_list)
        # Output: 1
        print(next(a))
        # Output: 9
        print(next(a))
        # Output: 36
        print(next(a))
        # Output: 100
        print(next(a))
        try:
            # Output: StopIteration
            next(a)
        except StopIteration as e:
            print('StopIteration Exception')
        # Generator expression can be used inside functions. When used in such 
        # a way, the round parentheses can be dropped.
        print('sum():',sum(x**2 for x in my_list))
        print('max():',max(x**2 for x in my_list))
        return
        
    def sequence_test(self, *args, **kwargs):
        """
        There are three basic sequence types: lists, tuples, and range 
        objects. Additional sequence types tailored for processing of binary 
        data and text strings are described in dedicated sections.
        The operations in the following table are supported by most sequence 
        types, both mutable and immutable. The collections.abc.Sequence ABC is 
        provided to make it easier to correctly implement these operations on 
        custom sequence types.
        This table lists the sequence operations sorted in ascending priority. 
        In the table, s and t are sequences of the same type, n, i, j and k 
        are integers and x is an arbitrary object that meets any type and 
        value restrictions imposed by s.
        The in and not in operations have the same priorities as the 
        comparison operations. The + (concatenation) and * (repetition) 
        operations have the same priority as the corresponding numeric 
        operations.
        
        Operation 	             Result 	                                                                        Notes
        x in s 	             True if an item of s is equal to x, else False 	                                (1)
        x not in s 	             False if an item of s is equal to x, else True 	                                (1)
        s + t 	                  the concatenation of s and t 	                                                    (6)(7)
        s * n or n * s 	        equivalent to adding s to itself n times 	                                          (2)(7)
        s[i] 	                  ith item of s, origin 0 	                                                         (3)
        s[i:j] 	             slice of s from i to j 	                                                         (3)(4)
        s[i:j:k] 	             slice of s from i to j with step k 	                                               (3)(5)
        len(s) 	             length of s 	 
        min(s) 	             smallest item of s 	 
        max(s) 	             largest item of s 	 
        s.index(x[, i[, j]]) 	   index of the first occurrence of x in s (at or after index i and before index j) 	  (8)
        s.count(x) 	             total number of occurrences of x in s 	 
        
        Sequences of the same type also support comparisons. In particular, 
        tuples and lists are compared lexicographically by comparing 
        corresponding elements. This means that to compare equal, every 
        element must compare equal and the two sequences must be of the same 
        type and have the same length.
        
        Function 	    Description
        all() 	         Return True if all elements of the list are true (or if the list is empty).
        any() 	         Return True if any element of the list is true. If the list is empty, return False.
        enumerate()     Return an enumerate object. It contains the index and value of all the items of list as a tuple.
        len() 	         Return the length (the number of items) in the list.
        list() 	    Convert an iterable (tuple, string, set, dictionary) to a list.
        max() 	         Return the largest item in the list.
        min() 	         Return the smallest item in the list
        sorted() 	    Return a new sorted list (does not sort the list itself).
        sum() 	         Return the sum of all elements in the list.
        """
        # While the in and not in operations are used only for simple 
        # containment testing in the general case, some specialised sequences 
        # (such as str, bytes and bytearray) also use them for subsequence 
        # testing:
        print('"gg" in "eggs":',"gg" in "eggs")
        # Values of n less than 0 are treated as 0 (which yields an empty 
        # sequence of the same type as s). Note that items in the sequence s 
        # are not copied; they are referenced multiple times. This often 
        # haunts new Python programmers; consider:
        lists = [[]] * 3
        print('lists:',lists)
        lists[0].append(3)
        print('lists:',lists)
        # What has happened is that [[]] is a one-element list containing an 
        # empty list, so all three elements of [[]] * 3 are references to this 
        # single empty list. Modifying any of the elements of lists modifies 
        # this single list. You can create a list of different lists this way:
        lists = [[] for i in range(3)]
        print('lists:',lists)
        lists[0].append(3)
        print('lists:',lists)
        i = -2
        # convert index in positive value
        print('len(lists) + i:',len(lists) + i)
        #######################################################################
        my_list = ['p','r','o','b','e']
        # Output: p
        print('my_list[0]:',my_list[0])
        # Output: o
        print('my_list[2]:',my_list[2])
        # Output: e
        print('my_list[4]:',my_list[4])
        # Error! Only integer can be used for indexing
        try:
            my_list[4.0]
        except Exception as e:
            print(e)
        # Nested List
        n_list = ["Happy", [2,0,1,5]]
        # Nested indexing
        # Output: a
        print('n_list[0][1]:',n_list[0][1])    
        # Output: 5
        print('n_list[1][3]:',n_list[1][3])
        my_list = ['p','r','o','b','e']
        # Output: e
        print('my_list[-1]:',my_list[-1])
        # Output: p
        print('my_list[-5]:',my_list[-5])
        my_list = ['p','r','o','g','r','a','m','i','z']
        # elements 3rd to 5th
        print('my_list[2:5]:',my_list[2:5])
        # elements beginning to 4th
        print('my_list[:-5]:',my_list[:-5])
        # elements 6th to end
        print('my_list[5:]:',my_list[5:])
        # elements beginning to end
        print('my_list[:]:',my_list[:])
        # mistake values
        odd = [2, 4, 6, 8]
        # change the 1st item    
        odd[0] = 1            
        # Output: [1, 4, 6, 8]
        print('odd:',odd)
        # change 2nd to 4th items
        odd[1:4] = [3, 5, 7]  
        # Output: [1, 3, 5, 7]
        print('odd:',odd)
        odd = [1, 3, 5]
        odd.append(7)
        # Output: [1, 3, 5, 7]
        print('odd:',odd)
        odd.extend([9, 11, 13])
        # Output: [1, 3, 5, 7, 9, 11, 13]
        print('odd:',odd)
        odd = [1, 3, 5]
        # Output: [1, 3, 5, 9, 7, 5]
        print('odd + [9, 7, 5]:',odd + [9, 7, 5])
        #Output: ["re", "re", "re"]
        print('["re"] * 3:',["re"] * 3)
        odd = [1, 9]
        odd.insert(1,3)
        # Output: [1, 3, 9] 
        print('odd:',odd)
        odd[2:2] = [5, 7]
        # Output: [1, 3, 5, 7, 9]
        print('odd:',odd)
        my_list = ['p','r','o','b','l','e','m']
        # delete one item
        del my_list[2]
        # Output: ['p', 'r', 'b', 'l', 'e', 'm']     
        print('my_list:',my_list)
        # delete multiple items
        del my_list[1:5]  
        # Output: ['p', 'm']
        print('my_list:',my_list)
        # delete entire list
        del my_list
        # Error: List not defined
        try:
            print('my_list:',my_list)
        except Exception as e:
            print(e)
        my_list = ['p','r','o','b','l','e','m']
        my_list.remove('p')
        # Output: ['r', 'o', 'b', 'l', 'e', 'm']
        print('my_list:',my_list)
        # Output: 'o'
        print('my_list.pop(1):',my_list.pop(1))
        # Output: ['r', 'b', 'l', 'e', 'm']
        print('my_list:',my_list)
        # Output: 'm'
        print('my_list.pop():',my_list.pop())
        # Output: ['r', 'b', 'l', 'e']
        print('my_list:',my_list)
        my_list.clear()
        # Output: []
        print('my_list:',my_list)
        my_list = [3, 8, 1, 6, 0, 8, 4]
        # Output: 1
        print('my_list.index(8):',my_list.index(8))
        # Output: 2
        print('my_list.count(8):',my_list.count(8))
        my_list.sort()
        # Output: [0, 1, 3, 4, 6, 8, 8]
        print('my_list:',my_list)
        my_list.reverse()
        # Output: [8, 8, 6, 4, 3, 1, 0]
        print('my_list:',my_list)
        pow2 = [2 ** x for x in range(10)]
        # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        print('pow2:',pow2)
        my_list = ['p','r','o','b','l','e','m']
        # Output: True
        print("'p' in my_list:",'p' in my_list)
        # Output: False
        print("'a' in my_list:",'a' in my_list)
        # Output: True
        print("'c' not in my_list:",'c' not in my_list)
        for fruit in ['apple','banana','mango']:
            print("I like",fruit)
        print("enumerate({'a':1,'b':2}):",enumerate({'a':1,'b':2}))
        for i,j in enumerate({'a':1,'b':2}):
            print(i,j)
        return
        
    def immutable_sequence_test(self, *args, **kwargs):
        """
        The only operation that immutable sequence types generally implement 
        that is not also implemented by mutable sequence types is support for 
        the hash() built-in.
        This support allows immutable sequences, such as tuple instances, to 
        be used as dict keys and stored in set and frozenset instances.
        Attempting to hash an immutable sequence that contains unhashable 
        values will result in TypeError.
        """
        try:
            print({[1]:'abc'})
        except Exception as e:
            print(e)
        print({('a','b'):'abc'})
        try:
            print({({'a':'b'}):'abc'})
        except Exception as e:
            print(e)
            
    def mutable_sequence_test(self, *args, **kwargs):
        """
        The operations in the following table are defined on mutable sequence 
        types. The collections.abc.MutableSequence ABC is provided to make it 
        easier to correctly implement these operations on custom sequence 
        types.
        In the table s is an instance of a mutable sequence type, t is any 
        iterable object and x is an arbitrary object that meets any type and 
        value restrictions imposed by s (for example, bytearray only accepts 
        integers that meet the value restriction 0 <= x <= 255).
        
        Operation 	             Result 	                                                                                Notes
        s[i] = x 	             item i of s is replaced by x 	 
        s[i:j] = t 	             slice of s from i to j is replaced by the contents of the iterable t 	 
        del s[i:j] 	             same as s[i:j] = [] 	 
        s[i:j:k] = t 	        the elements of s[i:j:k] are replaced by those of t 	                                   (1)
        del s[i:j:k] 	        removes the elements of s[i:j:k] from the list 	 
        s.append(x) 	        appends x to the end of the sequence (same as s[len(s):len(s)] = [x]) 	 
        s.clear() 	             removes all items from s (same as del s[:]) 	                                             (5)
        s.copy() 	             creates a shallow copy of s (same as s[:]) 	                                             (5)
        s.extend(t) or s += t    extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t) 	 
        s *= n 	             updates s with its contents repeated n times 	                                             (6)
        s.insert(i, x) 	        inserts x into s at the index given by i (same as s[i:i] = [x]) 	 
        s.pop([i]) 	             retrieves the item at i and also removes it from s 	                                        (2)
        s.remove(x) 	        remove the first item from s where s[i] is equal to x 	                                   (3)
        s.reverse() 	        reverses the items of s in place 
        Note:
        remove raises ValueError when x is not found in s.
        The reverse() method modifies the sequence in place for economy of 
        space when reversing a large sequence. To remind users that it 
        operates by side effect, it does not return the reversed sequence.
        clear() and copy() are included for consistency with the interfaces of 
        mutable containers that don’t support slicing operations (such as dict 
        and set)
        The value n is an integer, or an object implementing __index__(). Zero 
        and negative values of n clear the sequence. Items in the sequence are 
        not copied; they are referenced multiple times, as explained for s * n 
        under Common Sequence Operations.
        """
        pass
    
    def list_test(self, *args, **kwargs):
        """
        Lists are mutable sequences, typically used to store collections of 
        homogeneous items (where the precise degree of similarity will vary by 
        application).
        sort(*, key=None, reverse=False)
            This method sorts the list in place, using only < comparisons 
            between items. Exceptions are not suppressed - if any comparison 
            operations fail, the entire sort operation will fail (and the list 
            will likely be left in a partially modified state).
            sort() accepts two arguments that can only be passed by keyword 
            (keyword-only arguments):
            key specifies a function of one argument that is used to extract a 
            comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of None means that list items are sorted directly without calculating a separate key value.
        
            The functools.cmp_to_key() utility is available to convert a 2.x style cmp function to a key function.
        
            reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
        
            This method modifies the sequence in place for economy of space when sorting a large sequence. To remind users that it operates by side effect, it does not return the sorted sequence (use sorted() to explicitly request a new sorted list instance).
        
            The sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
        """
        # vowels list
        vowels = ['e', 'a', 'u', 'o', 'i']
        # sort the vowels
        vowels.sort()
        # print vowels
        print('Sorted list:', vowels)
        # vowels list
        vowels = ['e', 'a', 'u', 'o', 'i']
        # sort the vowels
        vowels.sort(reverse=True)
        # print vowels
        print('Sorted list (in Descending):', vowels)
        # take second element for sort
        def takeSecond(elem):
            return elem[1]
        # random list
        random = [(2, 2), (3, 4), (4, 1), (1, 3)]
        # sort list with key
        random.sort(key=takeSecond)
        # print list
        print('Sorted list:', random)
        
        # append
        # animal list
        animal = ['cat', 'dog', 'rabbit']
        # an element is added
        animal.append('guinea pig')
        #Updated Animal List
        print('Updated animal list: ', animal)
        # animal list
        animal = ['cat', 'dog', 'rabbit']
        # another list of wild animals
        wild_animal = ['tiger', 'fox']
        # adding wild_animal list to animal list
        animal.append(wild_animal)
        #Updated List
        print('Updated animal list: ', animal)
        
        # extend
        # language list
        language = ['French', 'English', 'German']
        # another list of language
        language1 = ['Spanish', 'Portuguese']
        language.extend(language1)
        # Extended List
        print('Language List: ', language)
        # language list
        language = ['French', 'English', 'German']
        # language tuple
        language_tuple = ('Spanish', 'Portuguese')
        # language set
        language_set = {'Chinese', 'Japanese'}
        # appending element of language tuple
        language.extend(language_tuple)
        print('New Language List: ', language)
        # appending element of language set
        language.extend(language_set)
        print('Newest Language List: ', language)
        a = [1, 2]
        b = [3, 4]
        a += b
        # Output: a = [1, 2, 3, 4]
        print('a = ', a)
        
        # insert
        # vowel list
        vowel = ['a', 'e', 'i', 'u']
        # inserting element to list at 4th position
        vowel.insert(3, 'o')
        print('Updated List: ', vowel)
        mixed_list = [{1, 2}, [5, 6, 7]]
        # number tuple
        number_tuple = (3, 4)
        # inserting tuple to the list
        mixed_list.insert(1, number_tuple)
        print('Updated List: ', mixed_list)
        
        # remove
        # animal list
        animal = ['cat', 'dog', 'rabbit', 'guinea pig']
        # 'rabbit' element is removed
        animal.remove('rabbit')
        #Updated Animal List
        print('Updated animal list: ', animal)
        # If a list contains duplicate elements
        # the remove() method removes only the first instance
        # animal list
        animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
        # 'dog' element is removed
        animal.remove('dog')
        #Updated Animal List
        print('Updated animal list: ', animal)
        # animal list
        animal = ['cat', 'dog', 'rabbit', 'guinea pig']
        # Deleting 'fish' element
        try:
            animal.remove('fish')
        except Exception as e:
            print(e)
        # Updated Animal List
        print('Updated animal list: ', animal)
        
        # pop
        # programming language list
        language = ['Python', 'Java', 'C++', 'French', 'C']
        # Return value from pop()
        # When 3 is passed
        return_value = language.pop(3)
        print('Return Value: ', return_value)
        # Updated List
        print('Updated List: ', language)
        # programming language list
        language = ['Python', 'Java', 'C++', 'Ruby', 'C']
        # When index is not passed
        print('When index is not passed:') 
        print('Return Value: ', language.pop())
        print('Updated List: ', language)
        # When -1 is passed
        # Pops Last Element
        print('\nWhen -1 is passed:') 
        print('Return Value: ', language.pop(-1))
        print('Updated List: ', language)
        # When -3 is passed
        # Pops Third Last Element
        print('\nWhen -3 is passed:') 
        print('Return Value: ', language.pop(-3))
        print('Updated List: ', language)
        
        # clear
        # Defining a list
        l = [{1, 2}, ('a'), ['1.1', '2.2']]
        # clearing the list
        l.clear()
        print('\nList:', l)
        # Defining a list
        l = [{1, 2}, ('a'), ['1.1', '2.2']]
        # clearing the list
        del l[:]
        print('List:', l)
        
        # index
        # vowels list
        vowels = ['a', 'e', 'i', 'o', 'i', 'u']
        # element 'e' is searched
        index = vowels.index('e')
        # index of 'e' is printed
        print('The index of e:', index)
        # element 'i' is searched
        index = vowels.index('i')
        # only the first index of the element is printed
        print('The index of i:', index)
        # vowels list
        vowels = ['a', 'e', 'i', 'o', 'u']
        # element 'p' is searched
        try:
            index = vowels.index('p')
            # index is printed
            print('The index of p:', index)
        except Exception as e:
            print(e)
        # random list
        random = ['a', ('a', 'b'), [3, 4]]
        # element ('a', 'b') is searched
        index = random.index(('a', 'b'))
        # index is printed
        print("The index of ('a', 'b'):", index)
        # element [3, 4] is searched
        index = random.index([3, 4])
        # index is printed
        print("The index of [3, 4]:", index)
        
        # count
        # vowels list
        vowels = ['a', 'e', 'i', 'o', 'i', 'u']
        # count element 'i'
        count = vowels.count('i')
        # print count
        print('The count of i is:', count)
        # count element 'p'
        count = vowels.count('p')
        # print count
        print('The count of p is:', count)
        # random list
        random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
        # count element ('a', 'b')
        count = random.count(('a', 'b'))
        # print count
        print("The count of ('a', 'b') is:", count)
        # count element [3, 4]
        count = random.count([3, 4])
        # print count
        print("The count of [3, 4] is:", count)
        
        # reverse
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']
        print('Original List:', os)
        # List Reverse
        os.reverse()
        # updated list
        print('Updated List:', os)
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']
        print('Original List:', os)
        # Reversing a list	
        #Syntax: reversed_list = os[start:stop:step] 
        reversed_list = os[::-1]
        # updated list
        print('Updated List:', reversed_list)
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']
        
        # Printing Elements in Reversed Order
        for o in reversed(os):
            print(o)
        
        # copy
        old_list = [1, 2, 3]
        new_list = old_list
        # add element to list
        new_list.append('a')
        print('New List:', new_list )
        print('Old List:', old_list )
        # mixed list
        l = ['cat', 0, 6.7]
        # copying a list
        new_list = l.copy()
        # Adding element to the new list
        new_list.append('dog')
        # Printing new and old list
        print('Old List: ', l)
        print('New List: ', new_list)
        # mixed list
        l = ['cat', 0, 6.7]
        # copying a list using slicing
        new_list = l[:]
        # Adding element to the new list
        new_list.append('dog')
        # Printing new and old list
        print('Old List: ', l)
        print('New List: ', new_list)
        return
        
    def tuple_test(self, *args, **kwargs):
        """
        Tuples are immutable sequences, typically used to store collections of 
        heterogeneous data (such as the 2-tuples produced by the enumerate() 
        built-in). Tuples are also used for cases where an immutable sequence 
        of homogeneous data is needed (such as allowing storage in a set or 
        dict instance)
        class tuple([iterable])
            Tuples may be constructed in a number of ways:
                Using a pair of parentheses to denote the empty tuple: ()
                Using a trailing comma for a singleton tuple: a, or (a,)
                Separating items with commas: a, b, c or (a, b, c)
                Using the tuple() built-in: tuple() or tuple(iterable)
            The constructor builds a tuple whose items are the same and in the 
            same order as iterable’s items. iterable may be either a sequence, 
            a container that supports iteration, or an iterator object. If 
            iterable is already a tuple, it is returned unchanged. For 
            example, tuple('abc') returns ('a', 'b', 'c') and tuple([1, 2, 3]) 
            returns (1, 2, 3). If no argument is given, the constructor 
            creates a new empty tuple, ().
            Note that it is actually the comma which makes a tuple, not the 
            parentheses. The parentheses are optional, except in the empty 
            tuple case, or when they are needed to avoid syntactic ambiguity. 
            For example, f(a, b, c) is a function call with three arguments, 
            while f((a, b, c)) is a function call with a 3-tuple as the sole 
            argument.
            Tuples implement all of the common sequence operations.
        For heterogeneous collections of data where access by name is clearer 
        than access by index, collections.namedtuple() may be a more 
        appropriate choice than a simple tuple object.
        """
        # empty tuple
        # Output: ()
        my_tuple = ()
        print('my_tuple:',my_tuple)
        # tuple having integers
        # Output: (1, 2, 3)
        my_tuple = (1, 2, 3)
        print('my_tuple:',my_tuple)
        # tuple with mixed datatypes
        # Output: (1, "Hello", 3.4)
        my_tuple = (1, "Hello", 3.4)
        print('my_tuple:',my_tuple)
        # nested tuple
        # Output: ("mouse", [8, 4, 6], (1, 2, 3))
        my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
        print('my_tuple:',my_tuple)
        # tuple can be created without parentheses
        # also called tuple packing
        # Output: 3, 4.6, "dog"
        my_tuple = 3, 4.6, "dog"
        print('my_tuple:',my_tuple)
        # tuple unpacking is also possible
        # Output:
        # 3
        # 4.6
        # dog
        a, b, c = my_tuple
        print('a:',a)
        print('b:',b)
        print('c:',c)
        # only parentheses is not enough
        # Output: <class 'str'>
        my_tuple = ("hello")
        print('type(my_tuple):',type(my_tuple))
        # need a comma at the end
        # Output: <class 'tuple'>
        my_tuple = ("hello",)  
        print('type(my_tuple):',type(my_tuple))
        # parentheses is optional
        # Output: <class 'tuple'>
        my_tuple = "hello",
        print('type(my_tuple):',type(my_tuple))
        my_tuple = ('p','e','r','m','i','t')
        # Output: 'p'
        print('my_tuple[0]:',my_tuple[0])
        # Output: 't'
        print('my_tuple[5]:',my_tuple[5])
        # index must be in range
        # If you uncomment line 14,
        # you will get an error.
        # IndexError: list index out of range
        try:
            print('my_tuple[6]:',my_tuple[6])
        except Exception as e:
            print(e)
        # index must be an integer
        # If you uncomment line 21,
        # you will get an error.
        # TypeError: list indices must be integers, not float
        try:
            my_tuple[2.0]
        except Exception as e:
            print(e)
        # nested tuple
        n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
        # nested index
        # Output: 's'
        print('n_tuple[0][3]:',n_tuple[0][3])
        # nested index
        # Output: 4
        print('n_tuple[1][1]:',n_tuple[1][1])
        my_tuple = ('p','e','r','m','i','t')
        # Output: 't'
        print('my_tuple[-1]:',my_tuple[-1])
        # Output: 'p'
        print('my_tuple[-6]:',my_tuple[-6])
        my_tuple = ('p','r','o','g','r','a','m','i','z')
        # elements 2nd to 4th
        # Output: ('r', 'o', 'g')
        print('my_tuple[1:4]:',my_tuple[1:4])
        # elements beginning to 2nd
        # Output: ('p', 'r')
        print('my_tuple[:-7]:',my_tuple[:-7])
        # elements 8th to end
        # Output: ('i', 'z')
        print('my_tuple[7:]:',my_tuple[7:])
        # elements beginning to end
        # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
        print('my_tuple[:]:',my_tuple[:])
        my_tuple = (4, 2, 3, [6, 5])
        # we cannot change an element
        # If you uncomment line 8
        # you will get an error:
        # TypeError: 'tuple' object does not support item assignment
        try:
            my_tuple[1] = 9
        except Exception as e:
            print(e)
        # but item of mutable element can be changed
        # Output: (4, 2, 3, [9, 5])
        my_tuple[3][0] = 9
        print('my_tuple:',my_tuple)
        # tuples can be reassigned
        # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
        my_tuple = ('p','r','o','g','r','a','m','i','z')
        print('my_tuple:',my_tuple)
        # Concatenation
        # Output: (1, 2, 3, 4, 5, 6)
        print('(1, 2, 3) + (4, 5, 6):',(1, 2, 3) + (4, 5, 6))
        # Repeat
        # Output: ('Repeat', 'Repeat', 'Repeat')
        print('("Repeat",) * 3:',("Repeat",) * 3)
        my_tuple = ('p','r','o','g','r','a','m','i','z')
        # can't delete items
        # if you uncomment line 8,
        # you will get an error:
        # TypeError: 'tuple' object doesn't support item deletion
        try:
            del my_tuple[3]
        except Exception as e:
            print(e)
        # can delete entire tuple
        # NameError: name 'my_tuple' is not defined
        del my_tuple
        try:
            print('my_tuple:',my_tuple)
        except Exception as e:
            print(e)  
        my_tuple = ('a','p','p','l','e',)
        # Count
        # Output: 2
        print("my_tuple.count('p'):",my_tuple.count('p'))
        # Index
        # Output: 3
        print("my_tuple.index('l'):",my_tuple.index('l'))
        my_tuple = ('a','p','p','l','e',)
        # In operation
        # Output: True
        print("'a' in my_tuple:",'a' in my_tuple)
        # Output: False
        print("'b' in my_tuple:",'b' in my_tuple)
        # Not in operation
        # Output: True
        print("'g' not in my_tuple:",'g' not in my_tuple)     
        # Output: 
        # Hello John
        # Hello Kate
        for name in ('John','Kate'):
             print("Hello",name)        
        return
        
    def range_test(self, *args, **kwargs):
        """
        The arguments to the range constructor must be integers (either 
        built-in int or any object that implements the __index__ special 
        method). If the step argument is omitted, it defaults to 1. If the 
        start argument is omitted, it defaults to 0. If step is zero, 
        ValueError is raised.
        For a positive step, the contents of a range r are determined by the 
        formula r[i] = start + step*i where i >= 0 and r[i] < stop.
        For a negative step, the contents of the range are still determined by 
        the formula r[i] = start + step*i, but the constraints are i >= 0 and 
        r[i] > stop.
        A range object will be empty if r[0] does not meet the value 
        constraint. Ranges do support negative indices, but these are 
        interpreted as indexing from the end of the sequence determined by the 
        positive indices.
        Ranges containing absolute values larger than sys.maxsize are 
        permitted but some features (such as len()) may raise OverflowError.
        r[n] = start + step*n (for both positive and negative step)
        where, n >=0 and r[n] < stop (for positive step)
        where, n >= 0 and r[n] > stop (for negative step)
        """
        import sys
        print('sys.maxsize:',sys.maxsize)
        # empty range
        print('list(range(0)):',list(range(0)))
        # using range(stop)
        print('list(range(10)):',list(range(10)))
        # using range(start, stop)
        print('list(range(1, 10)):',list(range(1, 10)))
        start = 2
        stop = 14
        step = 2
        print('list(range(start, stop, step)):',list(range(start, stop, step)))
        start = 2
        stop = -14
        step = -2
        print('list(range(start, stop, step)):',list(range(start, stop, step)))
        # value constraint not met
        print('list(range(start, 14, step)):',list(range(start, 14, step)))
        r = range(0, 20, 2)
        print('r:',r)
        print('11 in r:',11 in r)
        print('10 in r:',10 in r)
        print('r.index(10):',r.index(10))
        print('r[5]:',r[5])
        print('r[:5]:',r[:5])
        print('r[-1]:',r[-1])
        return
        
    def str_test(self, *args, **kwargs):
        """
        String literals that are part of a single expression and have only 
        whitespace between them will be implicitly converted to a single 
        string literal. That is, ("spam " "eggs") == "spam eggs".
        Since there is no separate “character” type, indexing a string 
        produces strings of length 1. That is, for a non-empty string s, s[0] 
        == s[0:1].
        Return a string version of object. If object is not provided, returns 
        the empty string. Otherwise, the behavior of str() depends on whether 
        encoding or errors is given, as follows.
        If neither encoding nor errors is given, str(object) returns 
        object.__str__(), which is the “informal” or nicely printable string 
        representation of object. For string objects, this is the string 
        itself. If object does not have a __str__() method, then str() falls 
        back to returning repr(object).
        If at least one of encoding or errors is given, object should be a 
        bytes-like object (e.g. bytes or bytearray). In this case, if object 
        is a bytes (or bytearray) object, then str(bytes, encoding, errors) is 
        equivalent to bytes.decode(encoding, errors). Otherwise, the bytes 
        object underlying the buffer object is obtained before calling 
        bytes.decode(). See Binary Sequence Types — bytes, bytearray, 
        memoryview and Buffer Protocol for information on buffer objects.
        Passing a bytes object to str() without the encoding or errors 
        arguments falls under the first case of returning the informal string 
        representation (see also the -b command-line option to Python).
        
        """
        print('("spam " "eggs"):',("spam " "eggs"))
        s = 'This is a string.'
        print('s[0]:',s[0])
        print('s[0] == s[0:1]:',s[0] == s[0:1])
        print("str(b'Zoot!'):",str(b'Zoot!'))
        str1 = 'Hello'
        str2 ='World!'
        # using +
        print('str1 + str2 = ', str1 + str2)
        # using *
        print('str1 * 3 =', str1 * 3)
        count = 0
        for letter in 'Hello World':
            if(letter == 'l'):
                count += 1
        print(count,'letters found')
        s = 'cold'
        # enumerate()
        list_enumerate = list(enumerate(s))
        print('list(enumerate(s)) = ', list_enumerate)
        #character count
        print('len(s) = ', len(s))
        # using triple quotes
        print('''He said, "What's there?"''')
        # escaping single quotes
        print('He said, "What\'s there?"')
        # escaping double quotes
        print("He said, \"What's there?\"")
        print("This is \x61 \ngood example")
        print(r"This is \x61 \ngood example")
        # default(implicit) order
        default_order = "{}, {} and {}".format('John','Bill','Sean')
        print('\n--- Default Order ---')
        print(default_order)
        # order using positional argument
        positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
        print('\n--- Positional Order ---')
        print(positional_order)
        # order using keyword argument
        keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
        print('\n--- Keyword Order ---')
        print(keyword_order)
        print('"Binary representation of {0} is {0:b}".format(12):',
        "Binary representation of {0} is {0:b}".format(12))
        print('"Exponent representation: {0:e}".format(1566.345):',
        "Exponent representation: {0:e}".format(1566.345))
        print('"One third is: {0:.3f}".format(1/3):',
        "One third is: {0:.3f}".format(1/3))
        print('"|{:<10}|{:^10}|{:>10}|".format(\'butter\',\'bread\',\'ham\'):',
        "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
        x = 4.34565
        # padding for float numbers
        print('The value of x is %8.2f' %x)
        print('The value of x is %8.4f' %x)
        return
        
    def string_method_test(self, *args, **kwargs):
        """
        Strings implement all of the common sequence operations, along with 
        the additional methods described below.
        Strings also support two styles of string formatting, one providing a 
        large degree of flexibility and customization (see str.format(), 
        Format String Syntax and Custom String Formatting) and the other based 
        on C printf style formatting that handles a narrower range of types 
        and is slightly harder to use correctly, but is often faster for the 
        cases it can handle (printf-style String Formatting).
        The Text Processing Services section of the standard library covers a 
        number of other modules that provide various text related utilities 
        (including regular expression support in the re module).
        """
        # str.capitalize()
        print('\n# str.capitalize()')
        # Return a copy of the string with its first character capitalized and 
        # the rest lowercased.
        print("'asdgwertgFW'.capitalize():",'asdgwertgFW'.capitalize())
        
        # str.casefold()
        print('\n# str.casefold()')
        # Return a casefolded copy of the string. Casefolded strings may be 
        # used for caseless matching.
        # Casefolding is similar to lowercasing but more aggressive because it 
        # is intended to remove all case distinctions in a string. For 
        # example, the German lowercase letter 'ß' is equivalent to "ss". 
        # Since it is already lowercase, lower() would do nothing to 'ß'; 
        # casefold() converts it to "ss".
        print("'ßdfgEGE'.casefold():",'ßdfgEGE'.casefold())
        
        # str.center(width[, fillchar])
        print('\n# str.center(width[, fillchar])')
        # Return centered in a string of length width. Padding is done using 
        # the specified fillchar (default is an ASCII space). The original 
        # string is returned if width is less than or equal to len(s).
        string = "Python is awesome"
        new_string = string.center(24)
        print("Centered String: ", new_string)
        string = "Python is awesome"
        print(string)
        new_string = string.center(24, '*')
        print("Centered String: ", new_string)
        
        # str.count(sub[, start[, end]])
        print('\n# str.count(sub[, start[, end]])')
        # Return the number of non-overlapping occurrences of substring sub in 
        # the range [start, end]. Optional arguments start and end are 
        # interpreted as in slice notation.
        # define string
        string = "Python is awesome, isn't it?"
        print(string)
        substring = "is"
        count = string.count(substring)
        # print count
        print("The count is:", count)
        # define string
        string = "Python is awesome, isn't it?"
        print(string)
        substring = "i"
        # count after first 'i' and before the last 'i'
        count = string.count(substring, 8, 25)
        # print count
        print("The count is:", count)
        
        # str.encode(encoding="utf-8", errors="strict")
        print('\n# str.encode(encoding="utf-8", errors="strict")')
        # Return an encoded version of the string as a bytes object. Default 
        # encoding is 'utf-8'. errors may be given to set a different error 
        # handling scheme. The default for errors is 'strict', meaning that 
        # encoding errors raise a UnicodeError. Other possible values are 
        # 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any 
        # other name registered via codecs.register_error(), see section Error 
        # Handlers. For a list of possible encodings, see section Standard 
        # Encodings.
        # unicode string
        string = 'pythön!'
        # print string
        print('The string is:', string)
        # default encoding to utf-8
        string_utf = string.encode()
        # print result
        print('The encoded version is:', string_utf)
        # unicode string
        string = 'pythön!'
        # print string
        print('The string is:', string)
        # ignore error
        print('The encoded version (with ignore) is:', 
              string.encode("ascii", "ignore"))
        # replace error
        print('The encoded version (with replace) is:', 
              string.encode("ascii", "replace"))
        
        # str.endswith(suffix[, start[, end]])
        print('\n# str.endswith(suffix[, start[, end]])')
        # Return True if the string ends with the specified suffix, otherwise 
        # return False. suffix can also be a tuple of suffixes to look for. 
        # With optional start, test beginning at that position. With optional 
        # end, stop comparing at that position.
        text = "Python is easy to learn."
        print(text)
        print("text.endswith('to learn'):",text.endswith('to learn'))
        print("text.endswith('to learn.'):",text.endswith('to learn.'))
        print("text.endswith('Python is easy to learn.'):",text.endswith('Python is easy to learn.'))
        text = "Python programming is easy to learn."
        print(text)
        # start parameter: 7
        # "programming is easy to learn." string is searched
        print("text.endswith('learn.', 7):",text.endswith('learn.', 7))
        # Both start and end is provided
        # start: 7, end: 26
        # "programming is easy" string is searched
        print("text.endswith('is', 7, 26):",text.endswith('is', 7, 26))
        print("text.endswith('easy', 7, 26):",text.endswith('easy', 7, 26))
        text = "programming is easy"
        print(text)
        print("text.endswith(('programming', 'python')):",
              text.endswith(('programming', 'python')))
        print("text.endswith(('python', 'easy', 'java')):",
              text.endswith(('python', 'easy', 'java')))
        # With start and end parameter
        # 'programming is' string is checked
        # If the string ends with any item of the tuple, endswith() returns 
        # True. If not, it returns False
        print("text.endswith(('is', 'an'), 0, 14):",
              text.endswith(('is', 'an'), 0, 14))
        
        # str.expandtabs(tabsize=8)
        print('\n# str.expandtabs(tabsize=8)')
        # Return a copy of the string where all tab characters are replaced by 
        # one or more spaces, depending on the current column and the given 
        # tab size. Tab positions occur every tabsize characters (default is 
        # 8, giving tab positions at columns 0, 8, 16 and so on). To expand 
        # the string, the current column is set to zero and the string is 
        # examined character by character. If the character is a tab (\t), one 
        # or more space characters are inserted in the result until the 
        # current column is equal to the next tab position. (The tab character 
        # itself is not copied.) If the character is a newline (\n) or return 
        # (\r), it is copied and the current column is reset to zero. Any 
        # other character is copied unchanged and the current column is 
        # incremented by one regardless of how the character is represented 
        # when printed.
        s = 'xyz\t12345\tabc'
        print('s:',s)
        # no argument is passed
        # default tabsize is 8
        print('s.expandtabs():',s.expandtabs())
        # The default tabsize is 8. The tab stops are 8, 16 and so on. Hence, 
        # there is 5 spaces after 'xyz' and 3 after '12345' when you print the 
        # original string.
        # When you set the tabsize to 2. The tab stops are 2, 4, 6, 8 and so on. 
        # For 'xyz', the tab stop is 4, and for '12345', the tab stop is 10. 
        # Hence, there is 1 space after 'xyz' and 1 space after '12345'.
        # When you set the tabsize to 3. The tab stops are 3, 6, 9 and so on. 
        # For 'xyz', the tab stop is 6, and for '12345', the tab stop is 12. 
        # Hence, there are 3 spaces after 'xyz' and 1 space after '12345'.
        # When you set the tabsize to 4. The tab stops are 4, 8, 12 and so on. 
        # For 'xyz', the tab stop is 4 and for '12345', the tab stop is 12. 
        # Hence, there is 1 space after 'xyz' and 3 spaces after '12345'.
        # When you set the tabsize to 5. The tab stops are 5, 10, 15 and so on. 
        # For 'xyz', the tab stop is 5 and for '12345', the tab stop is 15. 
        # Hence, there are 2 spaces after 'xyz' and 5 spaces after '12345'.
        # When you set the tabsize to 6. The tab stops are 6, 12, 18 and so on. 
        # For 'xyz', the tab stop is 6 and for '12345', the tab stop is 12. 
        # Hence, there are 3 spaces after 'xyz' and 1 space after '12345'.
        print('Original String:', s)
        # tabsize is set to 2
        print('Tabsize 2:', s.expandtabs(2))
        # tabsize is set to 3
        print('Tabsize 3:', s.expandtabs(3))
        # tabsize is set to 4
        print('Tabsize 4:', s.expandtabs(4))
        # tabsize is set to 5
        print('Tabsize 5:', s.expandtabs(5))
        # tabsize is set to 6
        print('Tabsize 6:', s.expandtabs(6))
        
        # str.find(sub[, start[, end]])
        print('\n# str.find(sub[, start[, end]])')
        # Return the lowest index in the string where substring sub is found 
        # within the slice s[start:end]. Optional arguments start and end are 
        # interpreted as in slice notation. Return -1 if sub is not found.
        # Note:
        # The find() method should be used only if you need to know the 
        # position of sub. To check if sub is a substring or not, use the in 
        # operator
        quote = 'Let it be, let it be, let it be'
        result = quote.find('let it')
        print("Substring 'let it':", result)
        result = quote.find('small')
        print("Substring 'small ':", result)
        # How to use find()
        if quote.find('be,') != -1:
            print("Contains substring 'be,'")
        else:
            print("Doesn't contain substring")
            
        quote = 'Do small things with great love'
        # Substring is searched in 'hings with great love'
        print("quote.find('small things', 10):",quote.find('small things', 10))
        # Substring is searched in ' small things with great love' 
        print("quote.find('small things', 2):",quote.find('small things', 2))
        # Substring is searched in 'hings with great lov'
        print("quote.find('o small ', 10, -1):",quote.find('o small ', 10, -1))
        # Substring is searched in 'll things with'
        print("quote.find('things ', 6, 20):",quote.find('things ', 6, 20))
        
        # str.format(*args, **kwargs)
        print('\n# str.format(*args, **kwargs)')
        # Perform a string formatting operation. The string on which this 
        # method is called can contain literal text or replacement fields 
        # delimited by braces {}. Each replacement field contains either the 
        # numeric index of a positional argument, or the name of a keyword 
        # argument. Returns a copy of the string where each replacement field 
        # is replaced with the string value of the corresponding argument.
        # default arguments
        print("Hello {}, your balance is {}.".format("Adam", 230.2346))
        # positional arguments
        print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
        # keyword arguments
        print("Hello {name}, your balance is {blc}.".format(name="Adam", 
              blc=230.2346))
        # mixed arguments
        print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
        # Type 	Meaning
        # d 	Decimal integer
        # c 	Corresponding Unicode character
        # b 	Binary format
        # o 	Octal format
        # x 	Hexadecimal format (lower case)
        # X 	Hexadecimal format (upper case)
        # n 	Same as 'd'. Except it uses current locale setting for number separator
        # e 	Exponential notation. (lowercase e)
        # E 	Exponential notation (uppercase E)
        # f 	Displays fixed point number (Default: 6)
        # F 	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
        # g 	General format. Rounds number to p significant digits. (Default precision: 6)
        # G 	Same as 'g'. Except switches to 'E' if the number is large.
        # % 	Percentage. Multiples by 100 and puts % at the end.
        # integer arguments
        print("\nThe number is:{:d}".format(123))
        # float arguments
        print("The float number is:{:f}".format(123.4567898))
        # octal, binary and hexadecimal format
        print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
        
        # in the first statement, {:5d} takes an integer argument and assigns 
        # a minimum width of 5. Since, no alignment is specified, it is 
        # aligned to the right.
        # In the second statement, you can see the width (2) is less than the 
        # number (1234), so it doesn't take any space to the left but also 
        # doesn't truncate the number.
        # Unlike integers, floats has both integer and decimal parts. And, the 
        # mininum width defined to the number is for both parts as a whole 
        # including ".".
        # In the third statement, {:8.3f} truncates the decimal part into 3 
        # places rounding off the last 2 digits. And, the number, now 12.235, 
        # takes a width of 8 as a whole leaving 2 places to the left.
        # If you want to fill the remaining places with zero, placing a zero 
        # before the format specifier does this. It works both for integers 
        # and floats: {:05d} and {:08.3f}.

        # integer numbers with minimum width
        print('\n"{:5d}".format(12):',"{:5d}".format(12))
        # width doesn't work for numbers longer than padding
        print('"{:2d}".format(1234):',"{:2d}".format(1234))
        # padding for float numbers
        print('"{:8.3f}".format(12.2346):',"{:8.3f}".format(12.2346))
        # integer numbers with minimum width filled with zeros
        print('"{:05d}".format(12):',"{:05d}".format(12))
        # padding for float numbers filled with zeros
        print('"{:08.3f}".format(12.2346):',"{:08.3f}".format(12.2346))
        # show the + sign
        print('"{:+f} {:+f}".format(12.23, -12.23):',
        "{:+f} {:+f}".format(12.23, -12.23))
        # show the - sign only
        print('"{:-f} {:-f}".format(12.23, -12.23):',
        "{:-f} {:-f}".format(12.23, -12.23))
        # show space for + sign
        print('"{: f} {: f}".format(12.23, -12.23):',
        "{: f} {: f}".format(12.23, -12.23))
        # Type 	Meaning
        # < 	Left aligned to the remaining space
        # ^ 	Center aligned to the remaining space
        # > 	Right aligned to the remaining space
        # = 	Forces the signed (+) (-) to the leftmost position
        # integer numbers with right alignment
        print('\n"{:5d}".format(12):',"{:5d}".format(12))
        # float numbers with center alignment
        print('"{:^10.3f}".format(12.2346):',"{:^10.3f}".format(12.2346))
        # integer left alignment filled with zeros
        print('"{:<05d}".format(12):',"{:<05d}".format(12))
        # float numbers with center alignment
        print('"{:=8.3f}".format(-12.2346):',"{:=8.3f}".format(-12.2346))
        # string padding with left alignment
        print('"{:5}".format("cat"):',"{:5}".format("cat"))
        # string padding with right alignment
        print('"{:>5}".format("cat"):',"{:>5}".format("cat"))
        # string padding with center alignment
        print('"{:^5}".format("cat"):',"{:^5}".format("cat"))
        # string padding with center alignment
        # and '*' padding character
        print('"{:*^5}".format("cat"):',"{:*^5}".format("cat"))
        # truncating strings to 3 letters
        print('"{:.3}".format("caterpillar"):',"{:.3}".format("caterpillar"))
        # truncating strings to 3 letters
        # and padding
        print('"{:5.3}".format("caterpillar"):',"{:5.3}".format("caterpillar"))
        # truncating strings to 3 letters,
        # padding and center alignment
        print('"{:^5.3}".format("caterpillar"):',
        "{:^5.3}".format("caterpillar"))
        # define Person class
        class Person:
            age = 23
            name = "Adam"
        # format age
        print('\n"{p.name}\'s age is: {p.age}".format(p=Person()):',"{p.name}'s age is: {p.age}".format(p=Person()))
        # define Person dictionary
        person = {'age': 23, 'name': 'Adam'}
        # format age
        print('"{p[name]}\'s age is: {p[age]}".format(p=person):',"{p[name]}'s age is: {p[age]}".format(p=person))
        # define Person dictionary
        person = {'age': 23, 'name': 'Adam'}
        # format age
        print('"{name}\'s age is: {age}".format(**person):',"{name}'s age is: {age}".format(**person))
        
        # dynamic string format template
        string = "{:{fill}{align}{width}}"
        print('\nstring:',string)
        # passing format codes as arguments
        print('string.format(\'cat\', fill=\'*\', align=\'^\', width=5):',
              string.format('cat', fill='*', align='^', width=5))
        # dynamic float format template
        num = "{:{align}{width}.{precision}f}"
        print('num:',num)
        # passing format codes as arguments
        print('num.format(123.236, align=\'<\', width=8, precision=2):',
              num.format(123.236, align='<', width=8, precision=2))
        
        import datetime
        # datetime formatting
        date = datetime.datetime.now()
        print("\nIt's now: {:%Y/%m/%d %H:%M:%S}".format(date))
        # complex number formatting
        complexNumber = 1+2j
        print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))
        # custom __format__() method
        class Person:
            def __format__(self, format):
                if(format == 'age'):
                    return '23'
                return 'None'
        print("Adam's age is: {:age}".format(Person()))
        # __str__() and __repr__() shorthand !r and !s
        print("\nQuotes: {0!r}, Without Quotes: {0!s}".format("cat"))
        # __str__() and __repr__() implementation for class
        class Person:
            def __str__(self):
                return "STR"
            def __repr__(self):
                return "REPR"
        print("repr: {p!r}, str: {p!s}".format(p=Person()))
        
        # str.format_map(mapping)
        print('\n# str.format_map(mapping)')
        # Similar to str.format(**mapping), except that mapping is used 
        # directly and not copied to a dict. This is useful if for example 
        # mapping is a dict subclass
        point = {'x':4,'y':-5}
        print("'{x} {y}'.format_map(point):",
        '{x} {y}'.format_map(point))
        point = {'x':4,'y':-5, 'z': 0}
        print("'{x} {y} {z}'.format_map(point):",
        '{x} {y} {z}'.format_map(point))
        class Coordinate(dict):
            def __missing__(self, key):
              return key
        print("\n'({x}, {y})'.format_map(Coordinate(x='6')):", 
        '({x}, {y})'.format_map(Coordinate(x='6')))
        print("'({x}, {y})'.format_map(Coordinate(y='5')):",
        '({x}, {y})'.format_map(Coordinate(y='5')))
        print("'({x}, {y})'.format_map(Coordinate(x='6', y='5')):",
        '({x}, {y})'.format_map(Coordinate(x='6', y='5')))
        
        # str.index(sub[, start[, end]])
        print('\n# str.index(sub[, start[, end]])')
        # Like find(), but raise ValueError when the substring is not found.
        sentence = 'Python programming is fun.'
        result = sentence.index('is fun')
        print("Substring 'is fun':", result)
        try:
            result = sentence.index('Java')
            print("Substring 'Java':", result)
        except Exception as e:
            print(e)
        sentence = 'Python programming is fun.'
        print('\nsentence:',sentence)
        # Substring is searched in 'gramming is fun.'
        print("sentence.index('ing', 10):",sentence.index('ing', 10))
        # Substring is searched in 'gramming is '
        print("sentence.index('g is', 10, -4):",sentence.index('g is', 10, -4))
        try:
            # Substring is searched in 'programming'
            print("sentence.index('fun', 7, 18):",sentence.index('fun', 7, 18))
        except Exception as e:
            print(e)
            
        # str.isalnum()
        print('\n# str.isalnum()')
        # Return true if all characters in the string are alphanumeric and 
        # there is at least one character, false otherwise. A character c is 
        # alphanumeric if one of the following returns True: c.isalpha(), 
        # c.isdecimal(), c.isdigit(), or c.isnumeric().
        print('"M234onica".isalnum():',"M234onica".isalnum())
        # contains whitespace
        print('"M3onica Gell22er ".isalnum():',"M3onica Gell22er ".isalnum())
        print('"Mo3nicaGell22er".isalnum():',"Mo3nicaGell22er".isalnum())
        print('"133".isalnum():',"133".isalnum())
        
        name = "M0n1caG3ll3r"
        print('\nname:',name)
        if name.isalnum():
           print("All characters of string (name) are alphanumeric.")
        else:
            print("All characters are not alphanumeric.")
            
        # str.isalpha()
        print('\n# str.isalpha()')
        # Return true if all characters in the string are alphabetic and there 
        # is at least one character, false otherwise. Alphabetic characters 
        # are those characters defined in the Unicode character database as 
        # “Letter”, i.e., those with general category property being one of 
        # “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Note that this is different from 
        # the “Alphabetic” property defined in the Unicode Standard.
        print('"Monica".isalpha():',"Monica".isalpha())
        # contains whitespace
        print('"Monica Geller".isalpha():',"Monica Geller".isalpha())
        # contains number
        print('"Mo3nicaGell22er".isalpha():',"Mo3nicaGell22er".isalpha())
        print("MonicaGeller")
        if "MonicaGeller".isalpha():
           print("All characters are alphabets")
        else:
            print("All characters are not alphabets.")
            
        # str.isascii()
        print('\n# str.isascii()')
        # Return true if the string is empty or all characters in the string 
        # are ASCII, false otherwise. ASCII characters have code points in the 
        # range U+0000-U+007F.
        # New in version 3.7.
        
        # str.isdecimal()
        print('\n# str.isdecimal()')
        # Return true if all characters in the string are decimal characters 
        # and there is at least one character, false otherwise. Decimal 
        # characters are those that can be used to form numbers in base 10, 
        # e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character 
        # is a character in the Unicode General Category “Nd”.
        print('"28212".isdecimal():',"28212".isdecimal())
        # contains alphabets
        print('"32ladk3".isdecimal():',"32ladk3".isdecimal())
        # contains alphabets and spaces
        print('"Mo3 nicaG el l22er".isdecimal():',
        "Mo3 nicaG el l22er".isdecimal())
        print("'23455'.isdecimal():",'23455'.isdecimal())
        #s = '²3455'
        print("'\u00B23455'.isdecimal():",'\u00B23455'.isdecimal())
        # s = '½'
        print("'\u00BD'.isdecimal():",'\u00BD'.isdecimal())
        
        # str.isdigit()
        print('\n# str.isdigit()')
        # Return true if all characters in the string are digits and there is 
        # at least one character, false otherwise. Digits include decimal 
        # characters and digits that need special handling, such as the 
        # compatibility superscript digits. This covers digits which cannot be 
        # used to form numbers in base 10, like the Kharosthi numbers. 
        # Formally, a digit is a character that has the property value 
        # Numeric_Type=Digit or Numeric_Type=Decimal.
        print('"28212".isdigit():',"28212".isdigit())
        # contains alphabets and spaces
        print('"Mo3 nicaG el l22er".isdigit():',"Mo3 nicaG el l22er".isdigit())
        print("'23455'.isdigit():",'23455'.isdigit())
        #s = '²3455'
        print("'\u00B23455'.isdigit():",'\u00B23455'.isdigit())
        # s = '½'
        print("'\u00BD'.isdigit():",'\u00BD'.isdigit())
        
        # str.isidentifier()
        print('\n# str.isidentifier()')
        # Return true if the string is a valid identifier according to the 
        # language definition, section Identifiers and keywords.
        # Use keyword.iskeyword() to test for reserved identifiers such as def 
        # and class. This means that if we can use a string as valid variable 
        # name or class name or identifier.
        print("'Python'.isidentifier():",'Python'.isidentifier())
        print("'Py thon'.isidentifier():",'Py thon'.isidentifier())
        print("'22Python'.isidentifier():",'22Python'.isidentifier())
        print("''.isidentifier():",''.isidentifier())
        if 'root33'.isidentifier():
            print('root33', 'is a valid identifier.')
        else:
            print('root33', 'is not a valid identifier.')
        if '33root'.isidentifier():
            print('33root', 'is a valid identifier.')
        else:
            print('33root', 'is not a valid identifier.')
        if 'root 33'.isidentifier():
            print('root 33', 'is a valid identifier.')
        else:
            print('root 33', 'is not a valid identifier.')
            
        # str.islower()
        print('\n# str.islower()')
        # Return true if all cased characters [4] in the string are lowercase 
        # and there is at least one cased character, false otherwise.
        print("'this is good'.islower():",'this is good'.islower())
        print("'th!s is a1so g00d'.islower():",'th!s is a1so g00d'.islower())
        print("'this is Not good'.islower():",'this is Not good'.islower())
        if 'this is good'.islower():
            print('"this is good"','Does not contain uppercase letter.')
        else:
            print('"this is good"','Contains uppercase letter.')
        if 'this is Good'.islower():
            print('"this is Good"','Does not contain uppercase letter.')
        else:
            print('"this is Good"','Contains uppercase letter.')
            
        # str.isnumeric()
        print('\n# str.isnumeric()')
        # Return true if all characters in the string are numeric characters, 
        # and there is at least one character, false otherwise. Numeric 
        # characters include digit characters, and all characters that have 
        # the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE 
        # FIFTH. Formally, numeric characters are those with the property 
        # value Numeric_Type=Digit, Numeric_Type=Decimal or 
        # Numeric_Type=Numeric.
        print("'1242323'.isnumeric():",'1242323'.isnumeric())
        #s = '²3455'
        print("'\u00B23455'.isnumeric():",'\u00B23455'.isnumeric())
        # s = '½'
        print("'\u00BD'.isnumeric():",'\u00BD'.isnumeric())
        print("'python12'.isnumeric():",'python12'.isnumeric())
        #s = '²3455'
        if '\u00B23455'.isnumeric() == True:
            print('"\u00B23455"','All characters are numeric.')
        else:
            print('"\u00B23455"','All characters are not numeric.')
            
        # str.isprintable()
        print('\n# str.isprintable()')
        # Return true if all characters in the string are printable or the 
        # string is empty, false otherwise. Nonprintable characters are those 
        # characters defined in the Unicode character database as “Other” or 
        # “Separator”, excepting the ASCII space (0x20) which is considered 
        # printable. (Note that printable characters in this context are those 
        # which should not be escaped when repr() is invoked on a string. It 
        # has no bearing on the handling of strings written to sys.stdout or 
        # sys.stderr.)
        print("'Space is a printable'.isprintable():",
        'Space is a printable'.isprintable())
        print("'\nNew Line is printable'.isprintable():",
        '\nNew Line is printable'.isprintable())
        print('\nEmpty string printable?', ''.isprintable())
        # written using ASCII
        # chr(27) is escape character
        # char(97) is letter 'a'
        s = chr(27) + chr(97)
        if s.isprintable():
            print(s,'Printable')
        else:
            print(s,'Not Printable')
        s = '2+2 = 4'
        if s.isprintable():
            print(s,'Printable')
        else:
            print(s,'Not Printable')
            
        # str.isspace()
        print('\n# str.isspace()')
        # Return true if there are only whitespace characters in the string 
        # and there is at least one character, false otherwise. Whitespace 
        # characters are those characters defined in the Unicode character 
        # database as “Other” or “Separator” and those with bidirectional 
        # property being one of “WS”, “B”, or “S”.
        print("'   \t'.isspace():",'   \t'.isspace())
        print("' a '.isspace():",' a '.isspace())
        print("''.isspace():",''.isspace())
        s = '\t  \n'
        if s.isspace() == True:
            print(s,'All whitespace characters')
        else:
            print(s,'Contains non-whitespace characters')
        s = '2+2 = 4\n'
        if s.isspace() == True:
            print(s,'All whitespace characters')
        else:
            print(s,'Contains non-whitespace characters.')
           
        # str.istitle()
        print('\n# str.istitle()')
        # Return true if the string is a titlecased string and there is at 
        # least one character, for example uppercase characters may only 
        # follow uncased characters and lowercase characters only cased ones. 
        # Return false otherwise.
        print("'Python Is Good.'.istitle():",'Python Is Good.'.istitle())
        print("'Python is good'.istitle():",'Python is good'.istitle())
        print("'This Is @ Symbol.'.istitle():",'This Is @ Symbol.'.istitle())
        print("'99 Is A Number'.istitle():",'99 Is A Number'.istitle())
        print("'PYTHON'.istitle():",'PYTHON'.istitle())
        s = 'I Love Python.'
        if s.istitle() == True:
            print(s,'Titlecased String')
        else:
            print(s,'Not a Titlecased String')
        s = 'PYthon'
        if s.istitle() == True:
            print(s,'Titlecased String')
        else:
            print(s,'Not a Titlecased String')
        # str.isupper()
        print('\n# str.isupper()')
        # Return true if all cased characters [4] in the string are uppercase 
        # and there is at least one cased character, false otherwise.
        # example string
        print('"THIS IS GOOD!".isupper():',"THIS IS GOOD!".isupper())
        # numbers in place of alphabets
        print('"THIS IS ALSO G00D!".isupper():',"THIS IS ALSO G00D!".isupper())
        # lowercase string
        print('"THIS IS not GOOD!".isupper():',"THIS IS not GOOD!".isupper())
        string = 'THIS IS GOOD'
        if string.isupper() == True:
            print(string,'Does not contain lowercase letter.')
        else:
            print(string,'Contains lowercase letter.')
          
        string = 'THIS IS gOOD'
        if string.isupper() == True:
            print(string,'Does not contain lowercase letter.')
        else:
            print(string,'Contains lowercase letter.')
        
        # str.join(iterable)
        print('\n# str.join(iterable)')
        # Return a string which is the concatenation of the strings in 
        # iterable. A TypeError will be raised if there are any non-string 
        # values in iterable, including bytes objects. The separator between 
        # elements is the string providing this method.
        numList = ['1', '2', '3', '4']
        seperator = ', '
        print('seperator.join(numList):',seperator.join(numList))
        numTuple = ('1', '2', '3', '4')
        print('seperator.join(numTuple):',seperator.join(numTuple))
        s1 = 'abc'
        s2 = '123'
        """ Each character of s2 is concatenated to the front of s1""" 
        print('s1.join(s2):', s1.join(s2))
        """ Each character of s1 is concatenated to the front of s2""" 
        print('s2.join(s1):', s2.join(s1))
        test =  {'2', '1', '3'}
        s = ', '
        print('s.join(test):',s.join(test))
        test = {'Python', 'Java', 'Ruby'}
        s = '->->'
        print('s.join(test):',s.join(test))
        test =  {'mat': 1, 'that': 2}
        s = '->'
        print('s.join(test):',s.join(test))
        test =  {1:'mat', 2:'that'}
        s = ', '
        # this gives error
        try:
            print(s.join(test))
        except Exception as e:
            print(e)
              
        # str.ljust(width[, fillchar])
        print('\n# str.ljust(width[, fillchar])')
        # Return the string left justified in a string of length width. 
        # Padding is done using the specified fillchar (default is an ASCII 
        # space). The original string is returned if width is less than or 
        # equal to len(s).
        # example string
        string = 'cat'
        width = 5
        # print left justified string
        print('string.ljust(width):',string.ljust(width))
        # example string
        string = 'cat'
        width = 5
        fillchar = '*'
        # print left justified string
        print('string.ljust(width, fillchar):',string.ljust(width, fillchar))
        
        # str.lower()
        print('\n# str.lower()')
        # Return a copy of the string with all the cased characters [4] 
        # converted to lowercase.
        # example string
        print('"THIS SHOULD BE LOWERCASE!".lower():',
        "THIS SHOULD BE LOWERCASE!".lower())
        # string with numbers
        # all alphabets whould be lowercase
        print('"Th!s Sh0uLd B3 L0w3rCas3!".lower():',
        "Th!s Sh0uLd B3 L0w3rCas3!".lower())
        # first string
        firstString = "PYTHON IS AWESOME!"
        # second string
        secondString = "PyThOn Is AwEsOmE!"
        
        if(firstString.lower() == secondString.lower()):
            print(firstString,secondString,"The strings are same.")
        else:
            print(firstString,secondString,"The strings are not same.")
            
        # str.lstrip([chars])
        print('\n# str.lstrip([chars])')
        # Return a copy of the string with leading characters removed. The 
        # chars argument is a string specifying the set of characters to be 
        # removed. If omitted or None, the chars argument defaults to removing 
        # whitespace. The chars argument is not a prefix; rather, all 
        # combinations of its values are stripped. All combinations of 
        # characters in the chars argument are removed from the left of the 
        # string until first mismatch.
        # Leading whitepsace are removed
        print("'   this is good '.lstrip():",'   this is good '.lstrip())
        # Argument doesn't contain space
        # No characters are removed.
        print("'   this is good '.lstrip('sti'):",
        '   this is good '.lstrip('sti'))
        print("'   this is good '.lstrip('s ti'):",
        '   this is good '.lstrip('s ti'))
        print("'https://www.programiz.com/'.lstrip('htps:/.'):",
        'https://www.programiz.com/'.lstrip('htps:/.'))
        
        # static str.maketrans(x[, y[, z]])
        print('\n# static str.maketrans(x[, y[, z]])')
        # This static method returns a translation table usable for 
        # str.translate().
        # If there is only one argument, it must be a dictionary mapping 
        # Unicode ordinals (integers) or characters (strings of length 1) to 
        # Unicode ordinals, strings (of arbitrary lengths) or None. Character 
        # keys will then be converted to ordinals.
        # If there are two arguments, they must be strings of equal length, 
        # and in the resulting dictionary, each character in x will be mapped 
        # to the character at the same position in y. If there is a third 
        # argument, it must be a string, whose characters will be mapped to 
        # None in the result.
        # example dictionary
        print('"abc".maketrans({"a": "123", "b": "456", "c": "789"}):',
        "abc".maketrans({"a": "123", "b": "456", "c": "789"}))
        # example dictionary
        print('"abc".maketrans({97: "123", 98: "456", 99: "789"}):',
        "abc".maketrans({97: "123", 98: "456", 99: "789"}))
        # first string
        print('"abc".maketrans("abc", "def"):',"abc".maketrans("abc", "def"))
        # example dictionary
        try:
            print("abc".maketrans("abc", "defghi"))
        except Exception as e:
            print(e)
        # Here, first the mapping between the two strings firstString and 
        # secondString are created.
        # Then, the third argument thirdString resets the mapping of each 
        # character in it to None and also creates new mapping for 
        # non-existent characters.
        # In this case, thirdString resets the mapping of 97 ('a') and 
        # 98 ('b') to None, and also creates a new mapping for 100 ('d') 
        # mapped to None.
        print('"abc".maketrans("abc", "def", "abd"):',
        "abc".maketrans("abc", "def", "abd"))
        
        # str.partition(sep)
        print('\n# str.partition(sep)')
        # Split the string at the first occurrence of sep, and return a 
        # 3-tuple containing the part before the separator, the separator 
        # itself, and the part after the separator. If the separator is not 
        # found, return a 3-tuple containing the string itself, followed by 
        # two empty strings.
        # 'is' separator is found
        print('"Python is fun".partition('is '):',
        "Python is fun".partition('is '))
        # 'not' separator is not found
        print('"Python is fun".partition(\'not \'):',
        "Python is fun".partition('not '))
        # splits at first occurence of 'is'
        print('"Python is fun, isn\'t it".partition(\'is\'):',
        "Python is fun, isn't it".partition('is'))
            
        # str.replace(old, new[, count])
        print('\n# str.replace(old, new[, count])')
        # Return a copy of the string with all occurrences of substring old 
        # replaced by new. If the optional argument count is given, only the 
        # first count occurrences are replaced.
        print ("'cold, cold heart'.replace('cold', 'hurt'):",
        'cold, cold heart'.replace('cold', 'hurt'))
        '''only two occurences of 'let' is replaced'''
        print("'let it be, let it be, let it be'.replace('let', \"don't let\", 2):",
        'let it be, let it be, let it be'.replace('let', "don't let", 2))
        song = 'cold, cold heart'
        replaced_song =  song.replace('o', 'e')
        # The original string is unchanged
        print ('Original string:', song)
        print ('Replaced string:', replaced_song)
        song = 'let it be, let it be, let it be'
        # maximum of 0 substring is replaced
        # returns copy of the original string
        print(song.replace('let', 'so', 0))
        
        # str.rfind(sub[, start[, end]])
        print('\n# str.rfind(sub[, start[, end]])')
        # Return the highest index in the string where substring sub is found, 
        # such that sub is contained within s[start:end]. Optional arguments 
        # start and end are interpreted as in slice notation. Return -1 on 
        # failure.
        quote = 'Let it be, let it be, let it be'
        print('quote:',quote)
        result = quote.rfind('let it')
        print("Substring 'let it':", result)
        result = quote.rfind('small')
        print("Substring 'small ':", result)
        result = quote.rfind('be,')
        if result != -1:
            print("Highest index where 'be,' occurs:", result)
        else:
            print("Doesn't contain substring")

        # Substring is searched in 'hings with great love'
        print("'Do small things with great love'.rfind('things', 10):",
        'Do small things with great love'.rfind('things', 10))
        
        # Substring is searched in ' small things with great love' 
        print("'Do small things with great love'.rfind('t', 2):",
        'Do small things with great love'.rfind('t', 2))
        # Substring is searched in 'hings with great lov'
        print("'Do small things with great love'.rfind('o small ', 10, -1)",
        'Do small things with great love'.rfind('o small ', 10, -1))
        # Substring is searched in 'll things with'
        print("'Do small things with great love'.rfind('th', 6, 20):",
        'Do small things with great love'.rfind('th', 6, 20))
        
        # str.rindex(sub[, start[, end]])
        print('\n# str.rindex(sub[, start[, end]])')
        # The rindex() method returns the highest index of the substring 
        # inside the string (if found).
        # Like rfind() but raises ValueError when the substring sub is not 
        # found.
        quote = 'Let it be, let it be, let it be'
        print('quote:',quote)
        result = quote.rindex('let it')
        print("Substring 'let it':", result)
        try:
            result = quote.rindex('small')
            print("Substring 'small ':", result)
        except Exception as e:
            print(e)
        quote = 'Do small things with great love'
        print('quote:',quote)
        # Substring is searched in ' small things with great love' 
        print("quote.rindex('t', 2):",quote.rindex('t', 2))
        # Substring is searched in 'll things with'
        print("quote.rindex('th', 6, 20):",quote.rindex('th', 6, 20))
        try:
            # Substring is searched in 'hings with great lov'
            print(quote.rindex('o small ', 10, -1))
        except Exception as e:
            print(e)
            
        # str.rjust(width[, fillchar])
        print('\n# str.rjust(width[, fillchar])')
        # Return the string right justified in a string of length width. 
        # Padding is done using the specified fillchar (default is an ASCII 
        # space). The original string is returned if width is less than or 
        # equal to len(s).
        # example string
        # print right justified string
        print("'cat'.rjust(5):",'cat'.rjust(5))
        # example string
        # print right justified string
        print("'cat'.rjust(5, '*'):",'cat'.rjust(5, '*'))
        
        # str.rpartition(sep)
        print('\n# str.rpartition(sep)')
        # Split the string at the last occurrence of sep, and return a 3-tuple 
        # containing the part before the separator, the separator itself, and 
        # the part after the separator. If the separator is not found, return 
        # a 3-tuple containing two empty strings, followed by the string 
        # itself.
        # 'is' separator is found
        print('"Python is fun".rpartition("is "):',
        "Python is fun".rpartition("is "))
        # 'not' separator is not found
        print('"Python is fun".rpartition("not "):',
        "Python is fun".rpartition("not "))
        # splits at last occurence of 'is'
        print('"Python is fun, isn\'t it".rpartition("is"):',
        "Python is fun, isn't it".rpartition("is"))
        
        # str.rstrip([chars])
        print('\n# str.rstrip([chars])')
        # Return a copy of the string with trailing characters removed. The 
        # chars argument is a string specifying the set of characters to be 
        # removed. If omitted or None, the chars argument defaults to removing 
        # whitespace. The chars argument is not a suffix; rather, all 
        # combinations of its values are stripped.
        print("'   spacious   '.rstrip():",'   spacious   '.rstrip())
        print("'mississippi'.rstrip('ipz'):",'mississippi'.rstrip('ipz'))
        # Leading whitepsace are removed
        print("' this is good'.rstrip():",' this is good'.rstrip())
        # Argument doesn't contain 'd'
        # No characters are removed.
        print("' this is good'.rstrip('si oo'):",
        ' this is good'.rstrip('si oo'))
        print("' this is good'.rstrip('sid oo'):",
        ' this is good'.rstrip('sid oo'))
        print("'www.programiz.com/'.rstrip('m/.'):",
        'www.programiz.com/'.rstrip('m/.'))
        
        # str.split(sep=None, maxsplit=-1)
        print('\n# str.split(sep=None, maxsplit=-1)')
        # Return a list of the words in the string, using sep as the delimiter 
        # string. If maxsplit is given, at most maxsplit splits are done 
        # (thus, the list will have at most maxsplit+1 elements). If maxsplit 
        # is not specified or -1, then there is no limit on the number of 
        # splits (all possible splits are made).
        # If sep is given, consecutive delimiters are not grouped together and 
        # are deemed to delimit empty strings (for example, '1,,2'.split(',') 
        # returns ['1', '', '2']). The sep argument may consist of multiple 
        # characters (for example, '1<>2<>3'.split('<>') returns 
        # ['1', '2', '3']). Splitting an empty string with a specified 
        # separator returns [''].
        print("'1,2,3'.split(','):",'1,2,3'.split(','))
        print("'1,2,3'.split(',', maxsplit=1):",'1,2,3'.split(',', maxsplit=1))
        print("'1,2,,3,'.split(','):",'1,2,,3,'.split(','))
        # If sep is not specified or is None, a different splitting algorithm 
        # is applied: runs of consecutive whitespace are regarded as a single 
        # separator, and the result will contain no empty strings at the start 
        # or end if the string has leading or trailing whitespace. 
        # Consequently, splitting an empty string or a string consisting of 
        # just whitespace with a None separator returns [].
        print("'1 2 3'.split():",'1 2 3'.split())
        print("'1 2 3'.split(maxsplit=1):",'1 2 3'.split(maxsplit=1))
        print("'   1   2   3   '.split():",'   1   2   3   '.split())
        
        # splits at space
        print("'Love thy neighbor'.split():",'Love thy neighbor'.split())
        # splits at ','
        print("'Milk, Chicken, Bread'.split(', '):",
        'Milk, Chicken, Bread'.split(', '))
        # Splitting at ':'
        print("'Milk, Chicken, Bread'.split(':'):",
        'Milk, Chicken, Bread'.split(':'))
        # maxsplit: 2
        print("'Milk, Chicken, Bread, Butter'.split(', ', 2):",
        'Milk, Chicken, Bread, Butter'.split(', ', 2))
        # maxsplit: 1
        print("'Milk, Chicken, Bread, Butter'.split(', ', 1):",
        'Milk, Chicken, Bread, Butter'.split(', ', 1))
        # maxsplit: 5
        print("'Milk, Chicken, Bread, Butter'.split(', ', 5):",
        'Milk, Chicken, Bread, Butter'.split(', ', 5))
        # maxsplit: 0
        print("'Milk, Chicken, Bread, Butter'.split(', ', 0):",
        'Milk, Chicken, Bread, Butter'.split(', ', 0))
        
        # str.splitlines([keepends])
        print('\n# str.splitlines([keepends])')
        # Return a list of the lines in the string, breaking at line 
        # boundaries. Line breaks are not included in the resulting list 
        # unless keepends is given and true.
        # This method splits on the following line boundaries. In particular, 
        # the boundaries are a superset of universal newlines.
        
        # Representation 	        Description
        # \n 	                       Line Feed
        # \r 	                       Carriage Return
        # \r\n 	                  Carriage Return + Line Feed
        # \v or \x0b 	             Line Tabulation
        # \f or \x0c 	             Form Feed
        # \x1c 	                  File Separator
        # \x1d 	                  Group Separator
        # \x1e 	                  Record Separator
        # \x85 	                  Next Line (C1 Control Code)
        # \u2028 	                  Line Separator
        # \u2029 	                  Paragraph Separator
        print("'ab c\\n\\nde fg\\rkl\\r\\n'.splitlines():",
        'ab c\n\nde fg\rkl\r\n'.splitlines())
        print("'ab c\\n\\nde fg\\rkl\\r\\n'.splitlines(keepends=True):",
        'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
        print('"".splitlines():',"".splitlines())
        print('"One line\\n".splitlines():',"One line\n".splitlines())
        print("''.split('\\n'):",''.split('\n'))
        print("'Two lines\\n'.split('\\n'):",'Two lines\n'.split('\n'))

        print("'Milk\\nChicken\\r\\nBread\\rButter'.splitlines():",
        'Milk\nChicken\r\nBread\rButter'.splitlines())
        print("'Milk\\nChicken\\r\\nBread\\rButter'.splitlines(True):",
        'Milk\nChicken\r\nBread\rButter'.splitlines(True))
        print("'Milk Chicken Bread Butter'.splitlines():",
        'Milk Chicken Bread Butter'.splitlines())
          
        # str.startswith(prefix[, start[, end]])
        print('\n# str.startswith(prefix[, start[, end]])')
        # Return True if string starts with the prefix, otherwise return False. 
        # prefix can also be a tuple of prefixes to look for. With optional 
        # start, test string beginning at that position. With optional end, 
        # stop comparing string at that position.
        # returns False
        print("'Python is easy to learn.'.startswith('is easy'):",
        'Python is easy to learn.'.startswith('is easy'))
        # returns True
        print("'Python is easy to learn.'.startswith('Python is '):",
        'Python is easy to learn.'.startswith('Python is '))
        # returns True
        print("'Python is easy to learn.'.startswith('Python is easy to learn.'):",
        'Python is easy to learn.'.startswith('Python is easy to learn.'))
        # start parameter: 7
        # 'programming is easy.' string is searched
        print('"Python programming is easy.".startswith("programming is", 7):',
        "Python programming is easy.".startswith("programming is", 7))     
        # start: 7, end: 18
        # 'programming' string is searched
        print('"Python programming is easy.".startswith("programming is", 7, 18):',
        "Python programming is easy.".startswith("programming is", 7, 18))
        print('"Python programming is easy.".startswith("program", 7, 18):',
        "Python programming is easy.".startswith("program", 7, 18))
        # If the string starts with any item of the tuple, startswith() 
        # returns True. If not, it returns False
        # prints True
        print("'programming is easy'.startswith(('python', 'programming')):",
        'programming is easy'.startswith(('python', 'programming')))
        # prints False
        print("'programming is easy'.startswith(('is', 'easy', 'java')):",
        'programming is easy'.startswith(('is', 'easy', 'java')))  
        # With start and end parameter
        # 'is easy' string is checked
        # prints False
        print("'programming is easy'.startswith(('programming', 'easy'), 12, 19):",
        'programming is easy'.startswith(('programming', 'easy'), 12, 19))
        
        # str.strip([chars])
        print('\n# str.strip([chars])')
        # Return a copy of the string with the leading and trailing characters 
        # removed. The chars argument is a string specifying the set of 
        # characters to be removed. If omitted or None, the chars argument 
        # defaults to removing whitespace. The chars argument is not a prefix 
        # or suffix; rather, all combinations of its values are stripped.
        print("'   spacious   '.strip():",'   spacious   '.strip())
        print("'www.example.com'.strip('cmowz.'):",
        'www.example.com'.strip('cmowz.'))
        print("'#....... Section 3.2.1 Issue #32 .......'.strip('.#! '):",
        '#....... Section 3.2.1 Issue #32 .......'.strip('.#! '))
        # Leading whitepsace are removed
        print("' xoxo love xoxo   '.strip():",' xoxo love xoxo   '.strip())
        print("' xoxo love xoxo   '.strip(' xoxoe'):",
        ' xoxo love xoxo   '.strip(' xoxoe'))
        # Argument doesn't contain space
        # No characters are removed.
        print("' xoxo love xoxo   '.strip('sti'):",
        ' xoxo love xoxo   '.strip('sti'))
        print("'android is awesome'.strip('an'):",
        'android is awesome'.strip('an'))
        
        # str.swapcase()
        print('\n# str.swapcase()')
        # Return a copy of the string with uppercase characters converted to 
        # lowercase and vice versa. Note that it is not necessarily true that 
        # s.swapcase().swapcase() == s.
        # example string
        print('"THIS SHOULD ALL BE LOWERCASE.".swapcase():',
        "THIS SHOULD ALL BE LOWERCASE.".swapcase())
        print('"this should all be uppercase.".swapcase():',
        "this should all be uppercase.".swapcase())
        print('"ThIs ShOuLd Be MiXeD cAsEd.".swapcase():',
        "ThIs ShOuLd Be MiXeD cAsEd.".swapcase())
        
        # str.title()
        print('\n# str.title()')
        # Return a titlecased version of the string where words start with an 
        # uppercase character and the remaining characters are lowercase.
        print("'Hello world'.title():",'Hello world'.title())
        # The algorithm uses a simple language-independent definition of a 
        # word as groups of consecutive letters. The definition works in many 
        # contexts but it means that apostrophes in contractions and 
        # possessives form word boundaries, which may not be the desired 
        # result.
        print('"they\'re bill\'s friends from the UK".title():',
        "they're bill's friends from the UK".title())
        # A workaround for apostrophes can be constructed using regular 
        # expressions.
        import re
        def titlecase(s):
            return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                          lambda mo: mo.group(0)[0].upper() +
                            mo.group(0)[1:].lower(),s)
        print(titlecase("they're bill's friends."))
        print("'My favorite number is 25.'.title():",
        'My favorite number is 25.'.title())
        print("'234 k3l2 *43 fun'.title():",'234 k3l2 *43 fun'.title())
        print('"He\'s an engineer, isn\'t he?".title():',
        "He's an engineer, isn't he?".title())
        
        # str.translate(table)
        print('\n# str.translate(table)')
        # Return a copy of the string in which each character has been mapped 
        # through the given translation table. The table must be an object 
        # that implements indexing via __getitem__(), typically a mapping or 
        # sequence. When indexed by a Unicode ordinal (an integer), the table 
        # object can do any of the following: return a Unicode ordinal or a 
        # string, to map the character to one or more other characters; return 
        # None, to delete the character from the return string; or raise a 
        # LookupError exception, to map the character to itself.
        # You can use str.maketrans() to create a translation map from 
        # character-to-character mappings in different formats.
        # See also the codecs module for a more flexible approach to custom 
        # character mappings.
        # first string
        print('translation = "abcdef".maketrans("abc", "ghi", "ab")')
        translation = "abcdef".maketrans("abc", "ghi", "ab")
        print('translation:',translation)
        # translate string
        print('"abcdef".translate(translation):',
              "abcdef".translate(translation))

        intab = "aeiou"
        outtab = "12345"
        trantab = ''.maketrans(intab, outtab,'akyth')
        print(trantab)
        s = "this is string example....wow!!!"
        print(s,'\n',s.translate(trantab))
        # translation table - a dictionary
        translation = {97: None, 98: None, 99: 105}
        string = "abcdef"
        print("Original string:", string)
        # translate string
        print("Translated string:", string.translate(translation))
        
        # str.upper()
        print('\n# str.upper()')
        # Return a copy of the string with all the cased characters [4] 
        # converted to uppercase. Note that s.upper().isupper() might be False 
        # if s contains uncased characters or if the Unicode category of the 
        # resulting character(s) is not “Lu” (Letter, uppercase), but e.g. 
        # “Lt” (Letter, titlecase).
        # The uppercasing algorithm used is described in section 3.13 of the 
        # Unicode Standard.
        # example string
        print('"this should be uppercase!".upper():',
        "this should be uppercase!".upper())
        # string with numbers
        # all alphabets whould be lowercase
        print('"Th!s Sh0uLd B3 uPp3rCas3!".upper():',
        "Th!s Sh0uLd B3 uPp3rCas3!".upper())
        # first string
        firstString = "python is awesome!"
        # second string
        secondString = "PyThOn Is AwEsOmE!"
        print(firstString, secondString, sep='\n')
        if(firstString.upper() == secondString.upper()):
            print("The strings are same.")
        else:
            print("The strings are not same.")
         
        # str.zfill(width)
        print('\n# str.zfill(width)')
        # Return a copy of the string left filled with ASCII '0' digits to 
        # make a string of length width. A leading sign prefix ('+'/'-') is 
        # handled by inserting the padding after the sign character rather 
        # than before. The original string is returned if width is less than 
        # or equal to len(s).
        print('"42".zfill(5):',"42".zfill(5))
        print('"-42".zfill(5):',"-42".zfill(5))
        print('"program is fun".zfill(15):',"program is fun".zfill(15))
        print('"program is fun".zfill(20):',"program is fun".zfill(20))
        print('"program is fun".zfill(10):',"program is fun".zfill(10))
        print('"-290".zfill(8):',"-290".zfill(8))
        print('"+290".zfill(8):',"+290".zfill(8))
        print('"--random+text".zfill(20):',"--random+text".zfill(20))
        
        # printf-style String Formatting
        print('\n# printf-style String Formatting')
        print('%(language)s has %(number)03d quote types.' 
              %{'language': "Python", "number": 2})
        return
        
    def binary_sequence_test(self, *args, **kwargs):
        """
        The core built-in types for manipulating binary data are bytes and 
        bytearray. They are supported by memoryview which uses the buffer 
        protocol to access the memory of other binary objects without needing 
        to make a copy.
        """
        # bytes([source[, encoding[, errors]]])
        print('# bytes([source[, encoding[, errors]]])')
        # Bytes objects are immutable sequences of single bytes. Since many 
        # major binary protocols are based on the ASCII text encoding, bytes 
        # objects offer several methods that are only valid when working with 
        # ASCII compatible data and are closely related to string objects in a 
        # variety of other ways.
        # Firstly, the syntax for bytes literals is largely the same as that 
        # for string literals, except that a b prefix is added.
        # As with string literals, bytes literals may also use a r prefix to 
        # disable processing of escape sequences. See String and Bytes 
        # literals for more about the various forms of bytes literal, 
        # including supported escape sequences.
        # string with encoding 'utf-8'
        print('bytes("Python is interesting.", "utf-8"):',
              bytes("Python is interesting.", "utf-8"))
        print('bytes(5):',bytes(5))
        print('bytes([1, 2, 3, 4, 5]):',bytes([1, 2, 3, 4, 5]))
        
        # fromhex(string)
        print('\n# fromhex(string)')
        # This bytes class method returns a bytes object, decoding the given 
        # string object. The string must contain two hexadecimal digits per 
        # byte, with ASCII whitespace being ignored.
        print("bytes.fromhex('2Ef0 F1f2  '):",bytes.fromhex('2Ef0 F1f2  '))
        # A reverse conversion function exists to transform a bytes object 
        # into its hexadecimal representation.
        
        # hex()
        print('\n# hex()')
        # Return a string object containing two hexadecimal digits for each 
        # byte in the instance.
        print("b'.\\xf0\\xf1\\xf2'.hex():",b'.\xf0\xf1\xf2'.hex())
        
        # bytearray([source[, encoding[, errors]]])
        print('\n# bytearray([source[, encoding[, errors]]])')
        # bytearray objects are a mutable counterpart to bytes objects.
        # There is no dedicated literal syntax for bytearray objects, instead 
        # they are always created by calling the constructor.
        # Creating an empty instance: bytearray()
        # Creating a zero-filled instance with a given length: bytearray(10)
        # From an iterable of integers: bytearray(range(20))
        # Copying existing binary data via the buffer protocol: bytearray(b'Hi!')
        # string with encoding 'utf-8'
        print('bytearray("Python is interesting.", "utf-8"):',
              bytearray("Python is interesting.", "utf-8"))
        print('bytearray(5):',bytearray(5))
        print('bytearray([1, 2, 3, 4, 5]):',bytearray([1, 2, 3, 4, 5]))
        
        # fromhex(string)
        print('\n# fromhex(string)')
        # This bytearray class method returns bytearray object, decoding the 
        # given string object. The string must contain two hexadecimal digits 
        # per byte, with ASCII whitespace being ignored.
        print("bytearray.fromhex('2Ef0 F1f2  '):",
              bytearray.fromhex('2Ef0 F1f2  '))
        # A reverse conversion function exists to transform a bytearray object 
        # into its hexadecimal representation.
        
        # hex()
        print('\n# hex()')
        # Return a string object containing two hexadecimal digits for each 
        # byte in the instance.
        print("bytearray(b'.\\xf0\\xf1\\xf2').hex():",
              bytearray(b'.\xf0\xf1\xf2').hex())
        return
        
    def memoryview_test(self, *args, **kwargs):
        """
        memoryview objects allow Python code to access the internal data of an 
        object that supports the buffer protocol without copying.
        Create a memoryview that references obj. obj must support the buffer 
        protocol. Built-in objects that support the buffer protocol include 
        bytes and bytearray.
        A memoryview has the notion of an element, which is the atomic memory 
        unit handled by the originating object obj. For many simple types such 
        as bytes and bytearray, an element is a single byte, but other types 
        such as array.array may have bigger elements.
        len(view) is equal to the length of tolist. If view.ndim = 0, the 
        length is 1. If view.ndim = 1, the length is equal to the number of 
        elements in the view. For higher dimensions, the length is equal to 
        the length of the nested list representation of the view. The itemsize 
        attribute will give you the number of bytes in a single element.
        A memoryview supports slicing and indexing to expose its data. 
        One-dimensional slicing will result in a subview.
        """
        v = memoryview(b'abcefg')
        print('v[1]:',v[1])
        print('v[-1]:',v[-1])
        print('v[1:4]:', v[1:4])
        print('bytes(v[1:4]):',bytes(v[1:4]))
        import array
        a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
        m = memoryview(a)
        print('m[0]:',m[0])
        print('m[-1]:',m[-1])
        print('m[::2].tolist():',m[::2].tolist())
        
        data = bytearray(b'abcefg')
        v = memoryview(data)
        print('v.readonly:',v.readonly)
        v[0] = ord(b'z')
        print('data:',data)
        v[1:4] = b'123'
        print('data:',data)
        try:
            v[2:3] = b'spam'
        except Exception as e:
            print(e)
        v[2:6] = b'spam'
        print('data:',data)
        v = memoryview(b'abcefg')
        print("hash(v) == hash(b'abcefg'):",hash(v) == hash(b'abcefg'))
        print("hash(v[2:4]) == hash(b'ce'):",hash(v[2:4]) == hash(b'ce'))
        print("hash(v[::-2]) == hash(b'abcefg'[::-2]):",
              hash(v[::-2]) == hash(b'abcefg'[::-2]))
        
        # __eq__(exporter)
        print('\n# __eq__(exporter)')
        # For the subset of struct format strings currently supported by 
        # tolist(), v and w are equal if v.tolist() == w.tolist()
        import array
        a = array.array('I', [1, 2, 3, 4, 5])
        b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
        c = array.array('b', [5, 3, 1])
        x = memoryview(a)
        y = memoryview(b)
        print('x == a == y == b:',x == a == y == b)
        print('x.tolist() == a.tolist() == y.tolist() == b.tolist():',
              x.tolist() == a.tolist() == y.tolist() == b.tolist())
        z = y[::-2]
        print('z == c:',z == c)
        print('z.tolist() == c.tolist():',z.tolist() == c.tolist())
        
        # If either format string is not supported by the struct module, then 
        # the objects will always compare as unequal (even if the format 
        # strings and buffer contents are identical)
        from ctypes import BigEndianStructure, c_long
        class BEPoint(BigEndianStructure):
            _fields_ = [("x", c_long), ("y", c_long)]
                        
        point = BEPoint(100, 200)
        a = memoryview(point)
        b = memoryview(point)
        print('a == point:',a == point)
        print('a == b:',a == b)
        
        # tobytes()
        print('\n# tobytes()')
        # Return the data in the buffer as a bytestring. This is equivalent to 
        # calling the bytes constructor on the memoryview.
        m = memoryview(b"abc")
        print('m.tobytes():',m.tobytes())
        print('bytes(m):',bytes(m))
        
        # hex()
        print('\n# hex()')
        # Return a string object containing two hexadecimal digits for each 
        # byte in the buffer.
        m = memoryview(b"abc")
        print('m.hex():',m.hex())
        
        # tolist()
        print('\n# tolist()')
        # Return the data in the buffer as a list of elements.
        print("memoryview(b'abc').tolist():",memoryview(b'abc').tolist())
        import array
        a = array.array('d', [1.1, 2.2, 3.3])
        m = memoryview(a)
        print('m.tolist():',m.tolist())
        
        # release()
        print('\n# release()')
        # Release the underlying buffer exposed by the memoryview object. Many 
        # objects take special actions when a view is held on them (for 
        # example, a bytearray would temporarily forbid resizing); therefore, 
        # calling release() is handy to remove these restrictions (and free 
        # any dangling resources) as soon as possible.
        # After this method has been called, any further operation on the view 
        # raises a ValueError (except release() itself which can be called 
        # multiple times)
        m = memoryview(b'abc')
        m.release()
        try:
            print('m[0]:',m[0])
        except Exception as e:
            print(e)
        # The context management protocol can be used for a similar effect, 
        # using the with statement.
        with memoryview(b'abc') as m:
            print('m[0]:',m[0])
            
        # cast(format[, shape])
        print('\n# cast(format[, shape])')
        # Cast a memoryview to a new format or shape. shape defaults to 
        # [byte_length//new_itemsize], which means that the result view will 
        # be one-dimensional. The return value is a new memoryview, but the 
        # buffer itself is not copied. Supported casts are 1D -> C-contiguous 
        # and C-contiguous -> 1D.
        # The destination format is restricted to a single element native 
        # format in struct syntax. One of the formats must be a byte format 
        # (‘B’, ‘b’ or ‘c’). The byte length of the result must be the same as 
        # the original length.
        a = array.array('l', [1,2,3])
        x = memoryview(a)
        print('x.format:',x.format)
        print('x.itemsize:',x.itemsize)
        print('len(x):',len(x))
        print('x.nbytes:',x.nbytes)
        y = x.cast('B')
        print('y.format:',y.format)
        print('y.itemsize:',y.itemsize)
        print('len(y):',len(y))
        print('y.nbytes:',y.nbytes)
        b = bytearray(b'zyz')
        x = memoryview(b)
        try:
            x[0] = b'a'
        except Exception as e:
            print(e)
        y = x.cast('c')
        y[0] = b'a'
        print('b:',b)
        
        import struct
        buf = struct.pack("i"*12, *list(range(12)))
        x = memoryview(buf)
        y = x.cast('i', shape=[2,2,3])
        print('y.tolist():',y.tolist())
        print('y.format:',y.format)
        print('y.itemsize:',y.itemsize)
        print('len(y):',len(y))
        print('y.nbytes:',y.nbytes)
        z = y.cast('b')
        print('z.format:',z.format)
        print('z.itemsize:',z.itemsize)
        print('len(z):',len(z))
        print('z.nbytes:',z.nbytes)
        
        buf = struct.pack("L"*6, *list(range(6)))
        x = memoryview(buf)
        y = x.cast('L', shape=[2,3])
        print('len(y):',len(y))
        print('y.nbytes:',y.nbytes)
        print('y.tolist():',y.tolist())
        
        # obj
        print('\n# obj')
        # The underlying object of the memoryview.
        b  = bytearray(b'xyz')
        m = memoryview(b)
        print('m.obj is b:',m.obj is b)
        
        # nbytes
        print('\n# nbytes')
        # nbytes == product(shape) * itemsize == len(m.tobytes()). This is the 
        # amount of space in bytes that the array would use in a contiguous 
        # representation. It is not necessarily equal to len(m)
        a = array.array('i', [1,2,3,4,5])
        m = memoryview(a)
        print('len(m):',len(m))
        print('m.nbytes:',m.nbytes)
        y = m[::2]
        print('len(y):',len(y))
        print('y.nbytes:',y.nbytes)
        print('len(y.tobytes()):',len(y.tobytes()))
        buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
        x = memoryview(buf)
        y = x.cast('d', shape=[3,4])
        print('y.tolist():',y.tolist())
        print('len(y):',len(y))
        print('y.nbytes:',y.nbytes)
        
        # readonly
        print('\n# readonly')
        # A bool indicating whether the memory is read only.
        print('y.readonly:',y.readonly)
        
        # format
        print('\n# format')
        # A string containing the format (in struct module style) for each 
        # element in the view. A memoryview can be created from exporters with 
        # arbitrary format strings, but some methods (e.g. tolist()) are 
        # restricted to native single element formats.
        # Changed in version 3.3: format 'B' is now handled according to the 
        # struct module syntax. This means that 
        # memoryview(b'abc')[0] == b'abc'[0] == 97.
        print('y.format:',y.format)
        
        # itemsize
        print('\n# itemsize')
        # The size in bytes of each element of the memoryview.
        m = memoryview(array.array('H', [32000, 32001, 32002]))
        print('m.itemsize:',m.itemsize)
        print('m[0]:',m[0])
        print("struct.calcsize('H') == m.itemsize:",
              struct.calcsize('H') == m.itemsize)
        
        # ndim
        print('\n# ndim')
        # An integer indicating how many dimensions of a multi-dimensional 
        # array the memory represents.
        buf = struct.pack("i"*12, *list(range(12)))
        x = memoryview(buf)
        y = x.cast('i', shape=[2,2,3])
        print('y.ndim:',y.ndim)
        
        # shape
        print('\n# shape')
        # A tuple of integers the length of ndim giving the shape of the 
        # memory as an N-dimensional array.
        # Changed in version 3.3: An empty tuple instead of None when ndim = 0.
        print('y.shape:',y.shape)
        
        # strides
        print('\n # strides')
        # A tuple of integers the length of ndim giving the size in bytes to 
        # access each element for each dimension of the array.
        # Changed in version 3.3: An empty tuple instead of None when ndim = 0.
        print('y.strides:',y.strides)
        
        # suboffsets
        print('\n# suboffsets')
        # Used internally for PIL-style arrays. The value is informational only.
        print('y.suboffsets:',y.suboffsets)
        
        # c_contiguous
        print('\n# c_contiguous')
        # A bool indicating whether the memory is C-contiguous.
        print('y.c_contiguous:',y.c_contiguous)
        
        # f_contiguous
        print('\n# f_contiguous')
        # A bool indicating whether the memory is Fortran contiguous.
        print('y.f_contiguous:',y.f_contiguous)
        
        # contiguous
        print('\n# contiguous')
        # A bool indicating whether the memory is contiguous.
        print('y.contiguous:',y.contiguous)
        
        #random bytearray
        randomByteArray = bytearray('ABC', 'utf-8')
        mv = memoryview(randomByteArray)
        # access memory view's zeroth index
        print('\nmv[0]:',mv[0])
        # create byte from memory view
        print('bytes(mv[0:2]):',bytes(mv[0:2]))
        # create list from memory view
        print('list(mv[0:3]):',list(mv[0:3]))
        
        #random bytearray
        randomByteArray = bytearray('ABC', 'utf-8')
        print('\nBefore updation:', randomByteArray)
        mv = memoryview(randomByteArray)
        # update 1st index of mv to Z
        mv[1] = 90
        print('After updation:', randomByteArray)
        return

    def set_test(self, *args, **kwargs):
        """
        A set object is an unordered collection of distinct hashable objects. 
        Common uses include membership testing, removing duplicates from a 
        sequence, and computing mathematical operations such as intersection, 
        union, difference, and symmetric difference. (For other containers see 
        the built-in dict, list, and tuple classes, and the collections module.)
        Like other collections, sets support x in set, len(set), and for x in 
        set. Being an unordered collection, sets do not record element 
        position or order of insertion. Accordingly, sets do not support 
        indexing, slicing, or other sequence-like behavior.
        There are currently two built-in set types, set and frozenset. The set 
        type is mutable — the contents can be changed using methods like add() 
        and remove(). Since it is mutable, it has no hash value and cannot be 
        used as either a dictionary key or as an element of another set. 
        The frozenset type is immutable and hashable — its contents cannot be 
        altered after it is created; it can therefore be used as a dictionary 
        key or as an element of another set.
        Non-empty sets (not frozensets) can be created by placing a 
        comma-separated list of elements within braces, for example: 
        {'jack', 'sjoerd'}, in addition to the set constructor.        
        """
        # set([iterable])
        print('# set([iterable])')
        # set of integers
        print('{1, 2, 3}:',{1, 2, 3})
        # set of mixed datatypes
        print('{1.0, "Hello", (1, 2, 3)}:',{1.0, "Hello", (1, 2, 3)})
        # set do not have duplicates
        # Output: {1, 2, 3, 4}
        print('{1,2,3,4,3,2}:',{1,2,3,4,3,2})
        # set cannot have mutable items
        # here [3, 4] is a mutable list
        # If you uncomment line #12,
        # this will cause an error.
        # TypeError: unhashable type: 'list'
        try:
            my_set = {1, 2, [3, 4]}
        except Exception as e:
            print(e)
        # we can make set from a list
        # Output: {1, 2, 3}
        print('set([1,2,3,2]):',set([1,2,3,2]))
        # initialize a with {}
        # check data type of a
        # Output: <class 'dict'>
        print('type({}):',type({}))
        # initialize a with set()
        # check data type of a
        # Output: <class 'set'>
        print('type(set()):',type(set()))
        # initialize my_set
        my_set = {1,3}
        print('my_set:',my_set)
        # if you uncomment line 9,
        # you will get an error
        # TypeError: 'set' object does not support indexing
        try:
            my_set[0]
        except Exception as e:
            print(e)
        # add an element
        # Output: {1, 2, 3}
        my_set.add(2)
        print('my_set:',my_set)
        # add multiple elements
        # Output: {1, 2, 3, 4}
        my_set.update([2,3,4])
        print('my_set:',my_set)
        # add list and set
        # Output: {1, 2, 3, 4, 5, 6, 8}
        my_set.update([4,5], {1,6,8})
        print('my_set:',my_set)
        # initialize my_set
        my_set = {1, 3, 4, 5, 6}
        print('my_set:',my_set)
        # discard an element
        # Output: {1, 3, 5, 6}
        my_set.discard(4)
        print('my_set:',my_set)
        # remove an element
        # Output: {1, 3, 5}
        my_set.remove(6)
        print('my_set:',my_set)
        # discard an element
        # not present in my_set
        # Output: {1, 3, 5}
        my_set.discard(2)
        print('my_set:',my_set)
        # remove an element
        # not present in my_set
        # If you uncomment line 27,
        # you will get an error.
        # Output: KeyError: 2
        try:
            my_set.remove(2)
        except Exception as e:
            print('KeyError:',e)
        # initialize A and B
        A = {1, 2, 3, 4, 5}
        B = {4, 5, 6, 7, 8}
        print('A:',A,'\nB:',B)
        # use | operator
        # Output: {1, 2, 3, 4, 5, 6, 7, 8}
        print('A | B:',A | B)
        print('A.union(B):',A.union(B))
        print('B.union(A):',B.union(A))
        # use & operator
        # Output: {4, 5}
        print('A & B:',A & B)
        print('A.intersection(B):',A.intersection(B))
        print('B.intersection(A):',B.intersection(A))
        # use - operator on A
        # Output: {1, 2, 3}
        print('A - B:',A - B)
        print('A.difference(B):',A.difference(B))
        print('B - A:',B - A)
        print('B.difference(A):',B.difference(A))
        # use ^ operator
        # Output: {1, 2, 3, 6, 7, 8}
        print('A ^ B:',A ^ B)
        print('A.symmetric_difference(B):',A.symmetric_difference(B))
        print('B.symmetric_difference(A):',B.symmetric_difference(A))
        # check if 'a' is present
        # Output: True
        print("'a' in set('apple'):",'a' in set("apple"))
        # check if 'p' is present
        # Output: False
        print("'p' not in set('apple'):",'p' not in set('apple'))
        for letter in set("apple"):
            print(letter)
            
        # add(elem)
        print('\n# add(elem)')
        # Add element elem to the set.
        # set of vowels
        vowels = {'a', 'e', 'i', 'u'}
        # adding 'o'
        vowels.add('o')
        print('Vowels are:', vowels)
        # adding 'a' again
        vowels.add('a')
        print('Vowels are:', vowels)
        # set of vowels
        vowels = {'a', 'e', 'u'}
        # a tuple ('i', 'o')
        tup = ('i', 'o')
        # adding tuple
        vowels.add(tup)
        print('Vowels are:', vowels)
        # adding same tuple again
        vowels.add(tup)
        print('Vowels are:', vowels)
        
        # clear()
        print('\n# clear()')
        # Remove all elements from the set.
        # set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        print('Vowels (before clear):', vowels)
        # clearing vowels
        vowels.clear()
        print('Vowels (after clear):', vowels)
        
        # copy()
        print('\n# copy()')
        # Return a new set with a shallow copy.
        numbers = {1, 2, 3, 4}
        new_numbers = numbers
        new_numbers.add('5')
        print('numbers: ', numbers)
        print('new_numbers: ', new_numbers)
        
        numbers = {1, 2, 3, 4}
        new_numbers = numbers.copy()
        new_numbers.add('5')
        print('numbers: ', numbers)
        print('new_numbers: ', new_numbers)
        
        # difference()
        print('\n# difference()')
        # Return a new set with elements in the set that are not in the others.
        A = {'a', 'b', 'c', 'd'}
        B = {'c', 'f', 'g'}
        print('A:',A,'\nB:',B)
        # Equivalent to A-B
        print('A.difference(B):',A.difference(B))
        # Equivalent to B-A
        print('B.difference(A):',B.difference(A))
        print('A-B:',A-B)
        print('B-A:',B-A)
        
        # difference_update(*others)
        print('\n# difference_update(*others)')
        # Update the set, removing elements found in others.
        # The difference_update() returns None indicating the object (set) is 
        # mutated.
        # Suppose,
        # result = A.difference_update(B)
        # When you run the code,
        # result will be None
        # A will be equal to A-B
        # B will be unchanged
        A = {'a', 'c', 'g', 'd'}
        B = {'c', 'f', 'g'}
        result = A.difference_update(B)
        print('A = ', A)
        print('B = ', B)
        print('result = ', result)
        
        # discard(elem)
        print('\n# discard(elem)')
        # Remove element elem from the set if it is present.
        numbers = {2, 3, 4, 5}
        numbers.discard(3)
        print('numbers = ', numbers)
        numbers.discard(10)
        print('numbers = ', numbers)
        numbers = {2, 3, 5, 4}
        # Returns None
        # Meaning, absence of a return value 
        print(numbers.discard(3))
        print('numbers =', numbers)
        
        # intersection(*others)
        print('\n# intersection(*others)')
        # Return a new set with elements common to the set and all others.
        A = {2, 3, 5, 4}
        B = {2, 5, 100}
        C = {2, 3, 8, 9, 10}
        print('A:',A,'\nB:',B,'\nC:',C)
        print('B.intersection(A):',B.intersection(A))
        print('B.intersection(C):',B.intersection(C))
        print('A.intersection(C):',A.intersection(C))
        print('C.intersection(A, B):',C.intersection(A, B))
        A = {100, 7, 8}
        B = {200, 4, 5}
        C = {300, 2, 3}
        D = {100, 200, 300}
        print('\nA:',A,'\nB:',B,'\nC:',C,'\nD:',D)
        print('A.intersection(D):',A.intersection(D))
        print('B.intersection(D):',B.intersection(D))
        print('C.intersection(D):',C.intersection(D))
        print('A.intersection(B, C, D):',A.intersection(B, C, D))
        A = {100, 7, 8}
        B = {200, 4, 5}
        C = {300, 2, 3, 7}
        D = {100, 200, 300}
        print('\nA:',A,'\nB:',B,'\nC:',C,'\nD:',D)
        print('A & C:',A & C)
        print('A & D:',A & D)
        print('A & C & D:',A & C & D)
        print('A & B & C & D:',A & B & C & D)
        
        # intersection_update(*others)
        print('\n# intersection_update(*others)')
        # Update the set, keeping only elements found in it and all others. 
        # This method returns None (meaning, absence of a return value). It 
        # only updates the set calling the intersection_update() method.
        # Suppose,
        # result = A.intersection_update(B, C)
        # When you run the code,
        # result will be None
        # A will be equal to the intersection of A, B and C
        # B remains unchanged
        # C remains unchanged
        A = {1, 2, 3, 4}
        B = {2, 3, 4, 5}
        print('A:',A,'\nB:',B)
        result = A.intersection_update(B)
        print('result =', result)
        print('A =', A)
        print('B =', B)
        A = {1, 2, 3, 4}
        B = {2, 3, 4, 5, 6}
        C = {4, 5, 6, 9, 10}
        print('\nA:',A,'\nB:',B,'\nC:',C)
        result = C.intersection_update(B, A)
        print('result =', result)
        print('C =', C)
        print('B =', B)
        print('A =', A)
        
        # isdisjoint(other)
        print('\n# isdisjoint(other)')
        # Return True if the set has no elements in common with other. Sets 
        # are disjoint if and only if their intersection is the empty set.
        A = {1, 2, 3, 4}
        B = {5, 6, 7}
        C = {4, 5, 6}
        print('A:',A,'\nB:',B,'\nC:',C)
        print('Are A and B disjoint?', A.isdisjoint(B))
        print('Are A and C disjoint?', A.isdisjoint(C))
        A = {'a', 'b', 'c', 'd'}
        B = ['b', 'e', 'f']
        C = '5de4'
        D ={1 : 'a', 2 : 'b'}
        E ={'a' : 1, 'b' : 2}
        print('\nA:',A,'\nB:',B,'\nC:',C,'\nD:',D,'\nE:',E)
        print('Are A and B disjoint?', A.isdisjoint(B))
        print('Are A and C disjoint?', A.isdisjoint(C))
        print('Are A and D disjoint?', A.isdisjoint(D))
        print('Are A and E disjoint?', A.isdisjoint(E))
        
        # issubset(other)
        print('\n# issubset(other)')
        # Test whether every element in the set is in other.
        A = {1, 2, 3}
        B = {1, 2, 3, 4, 5}
        C = {1, 2, 4, 5}
        print('\nA:',A,'\nB:',B,'\nC:',C)
        # Returns True
        print('A.issubset(B):',A.issubset(B))
        # Returns False
        # B is not subset of A
        print('B.issubset(A):',B.issubset(A))
        # Returns False
        print('A.issubset(C):',A.issubset(C))
        # Returns True
        print('C.issubset(B):',C.issubset(B))
        
        # issuperset(other)
        print('\n# issuperset(other)')
        # Test whether every element in other is in the set.
        A = {1, 2, 3, 4, 5}
        B = {1, 2, 3}
        C = {1, 2, 3}
        print('A:',A,'\nB:',B,'\nC:',C)
        # Returns True
        print('A.issuperset(B):',A.issuperset(B))
        # Returns False
        print('B.issuperset(A):',B.issuperset(A))
        # Returns True
        print('C.issuperset(B):',C.issuperset(B))
        
        # pop()
        print('\n# pop()')
        # Remove and return an arbitrary element from the set. Raises KeyError 
        # if the set is empty.
        A ={'a', 'b', 'c', 'd'}
        print('A:',A)
        print('Return Value is', A.pop())
        print('A = ', A)
        
        # remove(elem)
        print('\n# remove(elem)')
        # Remove element elem from the set. Raises KeyError if elem is not 
        # contained in the set.
        # language set
        language = {'English', 'French', 'German'}
        print('language:',language)
        # 'German' element is removed
        language.remove('German')
        # Updated language set
        print('Updated language set: ', language)
        # animal set
        animal = {'cat', 'dog', 'rabbit', 'guinea pig'}
        print('animal:',animal)
        # Deleting 'fish' element
        try:
            animal.remove('fish')
        except Exception as e:
            print('KeyError:',e)
        # Updated animal
        print('Updated animal set: ', animal)
        
        # symmetric_difference(other)
        print('\n# symmetric_difference(other)')
        # Return a new set with elements in either the set or other but not 
        # both.
        A = {'a', 'b', 'c', 'd'}
        B = {'c', 'd', 'e' }
        C = {}
        print('A:',A,'\nB:',B,'\nC:',C)
        print('A.symmetric_difference(B):',A.symmetric_difference(B))
        print('B.symmetric_difference(A):',B.symmetric_difference(A))
        print('A.symmetric_difference(C):',A.symmetric_difference(C))
        print('B.symmetric_difference(C):',B.symmetric_difference(C))
        A = {'a', 'b', 'c', 'd'}
        B = {'c', 'd', 'e' }
        print('\nA:',A,'\nB:',B)
        print('A ^ B:',A ^ B)
        print('B ^ A:',B ^ A)
        print('A ^ A:',A ^ A)
        print('B ^ B:',B ^ B)
        
        # symmetric_difference_update(other)
        print('\n# symmetric_difference_update(other)')
        # Update the set, keeping only elements found in either set, but not 
        # in both.
        A = {'a', 'c', 'd'}
        B = {'c', 'd', 'e' }
        print('A:',A,'\nB:',B)
        result = A.symmetric_difference_update(B)
        print('A = ', A)
        print('B = ', B)
        print('result = ', result)
        
        # union(*others)
        print('\n# union(*others)')
        # Return a new set with elements from the set and all others.
        A = {'a', 'c', 'd'}
        B = {'c', 'd', 2 }
        C= {1, 2, 3}
        print('A:',A,'\nB:',B,'\nC:',C)
        print('A U B =', A.union(B))
        print('B U C =', B.union(C))
        print('A U B U C =', A.union(B, C))
        print('A.union() = ', A.union())
        
        A = {'a', 'c', 'd'}
        B = {'c', 'd', 2 }
        C= {1, 2, 3}
        print('\nA:',A,'\nB:',B,'\nC:',C)
        print('A U B =', A| B)
        print('B U C =', B | C)
        print('A U B U C =', A | B | C)
        
        # update(*others)
        print('\n# update(*others)')
        # Update the set, adding elements from all others.
        A = {'a', 'b'}
        B = {1, 2, 3}
        print('A:',A,'\nB:',B)
        result = A.update(B)
        print('A =',A)
        print('B =',B)
        print('result =',result)
        # Update With String
        string_alphabet = 'abc'
        numbers_set = {1, 2}
        print('\nstring_alphabet:',string_alphabet,'\nnumbers_set:',numbers_set)
        numbers_set.update(string_alphabet)
        print('numbers_set =',numbers_set)
        print('string_alphabet =',string_alphabet)
        # Update With Dictionary
        info_dictionary = {'key': 1, 2 : 'lock'}
        numbers_set = {'a', 'b'}
        print('\ninfo_dictionary:',info_dictionary,'\nnumbers_set:',numbers_set)
        numbers_set.update(info_dictionary)
        print('numbers_set =',numbers_set)
        
        # frozenset([iterable])
        print('\n# frozenset([iterable])')
        # The frozenset() method returns an immutable frozenset object 
        # initialized with elements from the given iterable.
        # rozen set is just an immutable version of a Python set object. While 
        # elements of a set can be modified at any time, elements of frozen 
        # set remains the same after creation.
        # Due to this, frozen sets can be used as key in Dictionary or as 
        # element of another set. But like sets, it is not ordered (the 
        # elements can be set at any index).
        # tuple of vowels
        vowels = ('a', 'e', 'i', 'o', 'u')
        fSet = frozenset(vowels)
        print('The frozen set is:', fSet)
        print('The empty frozen set is:', frozenset())
        # random dictionary
        person = {"name": "John", "age": 23, "sex": "male"}
        fSet = frozenset(person)
        print('The frozen set is:', fSet)
        
    def dict_test(self, *args, **kwarg):
        """
        A mapping object maps hashable values to arbitrary objects. Mappings 
        are mutable objects. There is currently only one standard mapping type, 
        the dictionary. (For other containers see the built-in list, set, and 
        tuple classes, and the collections module.)
        A dictionary’s keys are almost arbitrary values. Values that are not 
        hashable, that is, values containing lists, dictionaries or other 
        mutable types (that are compared by value rather than by object 
        identity) may not be used as keys. Numeric types used for keys obey 
        the normal rules for numeric comparison: if two numbers compare equal 
        (such as 1 and 1.0) then they can be used interchangeably to index the 
        same dictionary entry. (Note however, that since computers store 
        floating-point numbers as approximations it is usually unwise to use 
        them as dictionary keys.)
        If no positional argument is given, an empty dictionary is created. If 
        a positional argument is given and it is a mapping object, a 
        dictionary is created with the same key-value pairs as the mapping 
        object. Otherwise, the positional argument must be an iterable object. 
        Each item in the iterable must itself be an iterable with exactly two 
        objects. The first object of each item becomes a key in the new 
        dictionary, and the second object the corresponding value. If a key 
        occurs more than once, the last value for that key becomes the 
        corresponding value in the new dictionary.
        """
        print('{1.0:4,1:3}:',{1.0:4,1:3})
        print('1==1.0:',1==1.0)
        a = dict(one=1, two=2, three=3)
        print('a = dict(one=1, two=2, three=3):',a)
        b = {'one': 1, 'two': 2, 'three': 3}
        print("b = {'one': 1, 'two': 2, 'three': 3}:",b)
        c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
        print("c = dict(zip(['one', 'two', 'three'], [1, 2, 3])):",c)
        d = dict([('two', 2), ('one', 1), ('three', 3)])
        print("d = dict([('two', 2), ('one', 1), ('three', 3)]):",d)
        e = dict({'three': 3, 'one': 1, 'two': 2})
        print("e = dict({'three': 3, 'one': 1, 'two': 2}):",e)
        print('a == b == c == d == e:',a == b == c == d == e)
        
        numbers = dict(x=5, y=0)
        print('numbers = ',numbers)
        print('type(numbers):',type(numbers))
        
        empty = dict()
        print('empty = ',empty)
        print('type(empty):',type(empty))
        
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
        print('\nnumbers1 =',numbers1)
        
        # you don't need to use dict() in above code
        numbers2 = {'x': 4, 'y': 5}
        print('numbers2 =',numbers2)
        
        # keyword argument is also passed
        numbers3 = dict({'x': 4, 'y': 5}, z=8)
        print('numbers3 =',numbers3)
        
        d = {'a':1,'b':2,'c':3,'d':4}
        print("\nd = {'a':1,'b':2,'c':3,'d':4}:")
        
        # len(d)
        print('\n# len(d):')
        # Return the number of items in the dictionary d.
        print('len(d):',len(d))
        
        # d[key]
        print('\n# d[key]')
        # Return the item of d with key key. Raises a KeyError if key is not 
        # in the map.
        # If a subclass of dict defines a method __missing__() and key is not 
        # present, the d[key] operation calls that method with the key key as 
        # argument. The d[key] operation then returns or raises whatever is 
        # returned or raised by the __missing__(key) call. No other operations 
        # or methods invoke __missing__(). If __missing__() is not defined, 
        # KeyError is raised. __missing__() must be a method; it cannot be an 
        # instance variable.
        class Counter(dict):
            def __missing__(self, key):
                return 0
        c = Counter()
        print("c['red']:",c['red'])
        
        # d[key] = value
        print('\n# d[key] = value')
        # Set d[key] to value.
        print('d =',d)
        print("d['e'] = 5")
        d['e'] = 5
        print('d =',d)
        
        # del d[key]
        print('\n# del d[key]')
        # Remove d[key] from d. Raises a KeyError if key is not in the map.
        print('d =',d)
        print('del d["e"]')
        del d['e']
        print('d =',d)
        
        # key in d
        print('\n# key in d')
        # Return True if d has a key key, else False.
        print('d =',d)
        print('"c" in d:',"c" in d)
        
        # key not in d
        print('\n# key not in d')
        # Equivalent to not key in d.
        print('d =',d)
        print('"c" not in d:',"c" not in d)
        
        # iter(d)
        print('\n# iter(d)')
        # Return an iterator over the keys of the dictionary. This is a 
        # shortcut for iter(d.keys()).
        print('d =',d)
        print('iter(d):',iter(d))
        for k in iter(d):
            print(k)
        print()
        for k in iter(d.keys()):
            print(k)
        print()
        for v in iter(d.values()):
            print(v)
            
        print("[*iter(d)]:",[*iter(d)])
        
        # clear()
        print('\n# clear()')
        # Remove all items from the dictionary.
        print('d =',d)
        print('d.clear()')
        d.clear()
        print('d =',d)
        
        d = {'a':1,'b':2,'c':3,'d':4}
        
        # copy()
        print('\n# copy()')
        # Return a shallow copy of the dictionary.
        print('d =',d)
        print('id(d):',id(d))
        print('dc = d.copy()')
        dc = d.copy()
        print('id(dc):',id(dc))
        print('dc =',dc)
        
        # fromkeys(iterable[, value])
        print('\n# fromkeys(iterable[, value])')
        # Create a new dictionary with keys from iterable and values set to 
        # value.
        # fromkeys() is a class method that returns a new dictionary. value 
        # defaults to None.
        # vowels keys
        keys = {'a', 'e', 'i', 'o', 'u' }
        print("keys = {'a', 'e', 'i', 'o', 'u' }")
        vowels = dict.fromkeys(keys)
        print(vowels)
        
        # vowels keys
        keys = {'a', 'e', 'i', 'o', 'u' }
        value = 'vowel'
        vowels = dict.fromkeys(keys, value)
        print('\n',vowels)
        
        # vowels keys
        keys = {'a', 'e', 'i', 'o', 'u' }
        value = [1]
        vowels = dict.fromkeys(keys, value)
        print('\n',vowels)
        # updating the value
        value.append(2)
        print(vowels)
        
        # vowels keys
        keys = {'a', 'e', 'i', 'o', 'u' }
        value = [1]
        vowels = { key : list(value) for key in keys }
        # you can also use { key : value[:] for key in keys }
        print('\n',vowels)
        # updating the value
        value.append(2)
        print(vowels)
        
        # get(key[, default])
        print('\n# get(key[, default])')
        # Return the value for key if key is in the dictionary, else default. 
        # If default is not given, it defaults to None, so that this method 
        # never raises a KeyError.
        d = {'b': 2, 'c': 3, 'd': 4, 'a': 1}
        print("d = {'b': 2, 'c': 3, 'd': 4, 'a': 1}")
        print("d.get('a',0):",d.get('a',0))
        print("d.get('e',0):",d.get('e',0))
        
        # items()
        print('\n# items()')
        # Return a new view of the dictionary’s items ((key, value) pairs).
        # random sales dictionary
        sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
        print("{ 'apple': 2, 'orange': 3, 'grapes': 4 }.items():",
              { 'apple': 2, 'orange': 3, 'grapes': 4 }.items())
        
        # random sales dictionary
        sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
        items = sales.items()
        print('Original items:', items)
        # delete an item from dictionary
        del[sales['apple']]
        print('Updated items:', items)
        
        # keys()
        print('\n# keys()')
        # Return a new view of the dictionary’s keys.
        print('d =',d)
        print('d.keys():',d.keys())
        
        # pop(key[, default])
        print('\n# pop(key[, default])')
        # If key is in the dictionary, remove it and return its value, else 
        # return default. If default is not given and key is not in the 
        # dictionary, a KeyError is raised.
        print('d =',d)
        print('d.pop("d"):',d.pop("d"))
        print('d =',d)
        try:
            print(d.pop("e"))
        except Exception as e:
            print('KeyError:',e)
        print('d.pop("e",0):',d.pop("e",0))
        
        # popitem()
        print('\n# popitem()')
        # Remove and return a (key, value) pair from the dictionary. Pairs are 
        # returned in LIFO order.
        # popitem() is useful to destructively iterate over a dictionary, as 
        # often used in set algorithms. If the dictionary is empty, calling 
        # popitem() raises a KeyError.
        # Changed in version 3.7: LIFO order is now guaranteed. In prior 
        # versions, popitem() would return an arbitrary key/value pair.
        d = {'b': 2, 'c': 3, 'd': 4, 'a': 1}
        print("d = {'b': 2, 'c': 3, 'd': 4, 'a': 1}")
        print('d.popitem():',d.popitem())
        print('d.popitem():',d.popitem())
        
        # setdefault(key[, default])
        print('\n# setdefault(key[, default])')
        # If key is in the dictionary, return its value. If not, insert key 
        # with a value of default and return default. default defaults to None.
        person = {'name': 'Phill', 'age': 22}
        print("age = person.setdefault('age')")
        age = person.setdefault('age')
        print('person = ',person)
        print('Age = ',age)
        
        person = {'name': 'Phill'}
        # key is not in the dictionary
        salary = person.setdefault('salary')
        print('\nperson = ',person)
        print('salary = ',salary)
        
        # key is not in the dictionary
        # default_value is provided
        age = person.setdefault('age', 22)
        print('person = ',person)
        print('age = ',age)
        
        # update([other])
        print('\n# update([other])')
        # Update the dictionary with the key/value pairs from other, 
        # overwriting existing keys. Return None.
        # update() accepts either another dictionary object or an iterable of 
        # key/value pairs (as tuples or other iterables of length two). If 
        # keyword arguments are specified, the dictionary is then updated with 
        # those key/value pairs: d.update(red=1, blue=2).
        d = {1: "one", 2: "three"}
        print('d =',d)
        d1 = {2: "two"}
        print('d1 =',d1)
        # updates the value of key 2
        print('d.update(d1)')
        d.update(d1)
        print('d =',d)
        d1 = {3: "three"}
        print('d1 =',d1)
        # adds element with key 3
        print('d.update(d1)')
        d.update(d1)
        print('d =',d)
        d = {'x': 2}
        print('d =',d)
        print('d.update(y = 3, z = 0)')
        d.update(y = 3, z = 0)
        print('d =',d)
        
        # values()
        print('\n# values()')
        # Return a new view of the dictionary’s values. See the documentation 
        # of view objects.
        # Dictionaries compare equal if and only if they have the same (key, 
        # value) pairs. Order comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise 
        # TypeError.
        # Dictionaries preserve insertion order. Note that updating a key does 
        # not affect the order. Keys added after deletion are inserted at the 
        # end.
        d = {"one": 1, "two": 2, "three": 3, "four": 4}
        print('d =',d)
        l = list(d)
        print('l =',l)
        l1 = list(d.values())
        print('l1 =',l1)
        d["one"] = 42
        print('d =',d)
        del d["two"]
        d["two"] = None
        print('d =',d)
        # random sales dictionary
        sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
        print('\nsales =',sales)
        print('sales.values():',sales.values())
        # random sales dictionary
        print('\nsales =',sales)
        values = sales.values()
        print('Original items:', values)
        # delete an item from dictionary
        del[sales['apple']]
        print('Updated items:', values)
        
        # Dictionary view objects
        print('\n# Dictionary view objects')
        # The objects returned by dict.keys(), dict.values() and dict.items() 
        # are view objects. They provide a dynamic view on the dictionary’s 
        # entries, which means that when the dictionary changes, the view 
        # reflects these changes.
        # Dictionary views can be iterated over to yield their respective 
        # data, and support membership tests.
        dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
        print('dishes =',dishes)
        keys = dishes.keys()
        print('keys =',keys)
        values = dishes.values()
        print('values =', values) 
        n = 0
        # iteration
        for val in values:
            n += val
        print('n =',n)
        # keys and values are iterated over in the same order (insertion order)
        key_list = list(keys)
        print('key_list =',key_list)
        value_list = list(values)
        print('value_list =',value_list)
        # view objects are dynamic and reflect dict changes
        print("del dishes['eggs']\ndel dishes['sausage']")
        del dishes['eggs']
        del dishes['sausage']
        print('keys =',list(keys))
        # set operations
        print("keys & {'eggs', 'bacon', 'salad'}:",
              keys & {'eggs', 'bacon', 'salad'})
        print("keys ^ {'sausage', 'juice'}:",keys ^ {'sausage', 'juice'})
        
    def context_manager_test(self, *args, **kwargs):
        """
        Python’s with statement supports the concept of a runtime context 
        defined by a context manager. This is implemented using a pair of 
        methods that allow user-defined classes to define a runtime context that 
        is entered before the statement body is executed and exited when the 
        statement ends.
        """
        # contextmanager.__enter__()
        print('# contextmanager.__enter__()')
        # Enter the runtime context and return either this object or another 
        # object related to the runtime context. The value returned by this method 
        # is bound to the identifier in the as clause of with statements using 
        # this context manager.
        # An example of a context manager that returns itself is a file object. 
        # File objects return themselves from __enter__() to allow open() to be 
        # used as the context expression in a with statement.
        # An example of a context manager that returns a related object is the one 
        # returned by decimal.localcontext(). These managers set the active 
        # decimal context to a copy of the original decimal context and then 
        # return the copy. This allows changes to be made to the current decimal 
        # context in the body of the with statement without affecting code outside 
        # the with statement.
        
        # contextmanager.__exit__(exc_type, exc_val, exc_tb)
        print('# contextmanager.__exit__(exc_type, exc_val, exc_tb)')
        # Exit the runtime context and return a Boolean flag indicating if any 
        # exception that occurred should be suppressed. If an exception occurred 
        # while executing the body of the with statement, the arguments contain 
        # the exception type, value and traceback information. Otherwise, all 
        # three arguments are None.
        # Returning a true value from this method will cause the with statement to suppress the exception and continue execution with the statement immediately following the with statement. Otherwise the exception continues propagating after this method has finished executing. Exceptions that occur during execution of this method will replace any exception that occurred in the body of the with statement.
        # The exception passed in should never be reraised explicitly - instead, 
        # this method should return a false value to indicate that the method 
        # completed successfully and does not want to suppress the raised 
        # exception. This allows context management code to easily detect whether 
        # or not an __exit__() method has actually failed.
        
        with open('some_file', 'w') as opened_file:
            opened_file.write('Hola!')
            print('some_file is opened in write mode and if some_file does not'
            ' exist it will create one and open in write mode.')
            print('opened_file:',opened_file)
        # The above code opens the file, writes some data to it and then 
        # closes it. If an error occurs while writing the data to the file, it 
        # tries to close it. The above code is equivalent to:
        file = open('some_file', 'w')
        try:
            file.write('Hola!')
            print('file:',file)
        finally:
            file.close()
            
        # At the very least a context manager has an __enter__ and __exit__ 
        # method defined. Let’s make our own file-opening Context Manager and 
        # learn the basics.
        class File(object):
            def __init__(self, file_name, method):
                self.file_obj = open(file_name, method)
            def __enter__(self):
                return self.file_obj
            def __exit__(self, type, value, traceback):
                self.file_obj.close()
                print('type:',type)
                print('value:',value)
                print('traceback:',traceback)
                return True
        
        with File('demo.txt', 'w') as opened_file:
            opened_file.write('Hola!')
            print('opened_file:',opened_file)
        
        with File('demo.txt', 'w') as opened_file:
            opened_file.undefined_function('Hola!')
            print('opened_file:',opened_file)
            
        from contextlib import contextmanager
        @contextmanager
        def open_file(name):
            f = open(name, 'w')
            yield f
            f.close()
            
        with open_file('some_file') as f:
            f.write('hola!')
            print('f:',f)
            
    def modules_test(self, *args, **kwargs):
        """
        The only special operation on a module is attribute access: m.name, 
        where m is a module and name accesses a name defined in m’s symbol 
        table. Module attributes can be assigned to. (Note that the import 
        statement is not, strictly speaking, an operation on a module object; 
        import foo does not require a module object named foo to exist, rather 
        it requires an (external) definition for a module named foo somewhere.)
        A special attribute of every module is __dict__. This is the dictionary
        containing the module’s symbol table. Modifying this dictionary will 
        actually change the module’s symbol table, but direct assignment to 
        the __dict__ attribute is not possible (you can write 
        m.__dict__['a'] = 1, which defines m.a to be 1, but you can’t write 
        m.__dict__ = {}). Modifying __dict__ directly is not recommended.
        Modules built into the interpreter are written like this: 
            <module 'sys' (built-in)>. If loaded from a file, they are written 
            as <module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>.
        """
        import example
        print('import example')
        print('example.add(4,5.5):',example.add(4,5.5))

        import example as e
        print('import example as e')
        print('e.add(4,5.5):',e.add(4,5.5))

        from example import add
        print('from example import add')
        print('add(4,5.5):',add(4,5.5))
        
        try:
            eval('from example import *')
            print('from example import *')
            print('add(4,5.5):',add(4,5.5))
        except SyntaxError as e:
            print('SyntaxError:','import * only allowed at module level\n',e.msg)
        
        # The Python interpreter imports a module only once during a session. 
        # This makes things more efficient. Here is an example to show how 
        # this works.
        print('\nimport my_module')
        import my_module
        print('import my_module')
        import my_module
        
        # Python provides a neat way of doing this. We can use the reload() 
        # function inside the imp module to reload a module. This is how its 
        # done.
        import imp
        print('\nimp.reload(my_module)')
        imp.reload(my_module)
        
        print('\ndir(example):',dir(example))
        return
        
    def class_object_test(self, *args, **kwargs):
        """
        
        """
        class MyClass:
            "This is my second class"
            a = 10
            def func(self):
                print('Hello')
        # Output: 10
        print(MyClass.a)
        # Output: <function MyClass.func at 0x0000000003079BF8>
        print(MyClass.func)
        # Output: 'This is my second class'
        print(MyClass.__doc__)
        
        class MyClass:
        	"This is my second class"
        	a = 10
        	def func(self):
        		print('Hello')
        
        # create a new MyClass
        ob = MyClass()
        
        # Output: <function MyClass.func at 0x000000000335B0D0>
        print('\n',MyClass.func)
        
        # Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
        print(ob.func)
        
        # Calling function func()
        # Output: Hello
        print('ob.func()')
        ob.func()
        return
        
    def function_test(self, *args, **kwargs):
        """
        Function objects are created by function definitions. The only 
        operation on a function object is to call it: func(argument-list).
        There are really two flavors of function objects: built-in functions 
        and user-defined functions. Both support the same operation (to call 
        the function), but the implementation is different, hence the 
        different object types.
        """
        def greet(name):
            """
            This function greets to the person passed in as parameter
            """
            print("Hello, " + name + ". Good morning!")
            
        greet('Rajesh')
        print(greet.__doc__)
        print(greet("Samui"))
        
        def absolute_value(num):
            """This function returns the absolute
            value of the entered number"""
        
            if num >= 0:
                return num
            else:
                return -num
        
        # Output: 2
        print('\nabsolute_value(2):',absolute_value(2))
        # Output: 4
        print('absolute_value(-4):',absolute_value(-4))
        
        def my_func():
            x = 10
            print("\nValue inside function:",x)
        
        x = 20
        my_func()
        print("Value outside function:",x)
        return
        
    def method_test(self, *args, **kwargs):
        """
        Methods are functions that are called using the attribute notation. 
        There are two flavors: built-in methods (such as append() on lists) 
        and class instance methods. Built-in methods are described with the 
        types that support them.
        If you access a method (a function defined in a class namespace) 
        through an instance, you get a special object: a bound method (also 
        called instance method) object. When called, it will add the self 
        argument to the argument list. Bound methods have two special 
        read-only attributes: m.__self__ is the object on which the method 
        operates, and m.__func__ is the function implementing the method. 
        Calling m(arg-1, arg-2, ..., arg-n) is completely equivalent to 
        calling m.__func__(m.__self__, arg-1, arg-2, ..., arg-n).
        Like function objects, bound method objects support getting arbitrary 
        attributes. However, since method attributes are actually stored on 
        the underlying function object (meth.__func__), setting method 
        attributes on bound methods is disallowed. Attempting to set an 
        attribute on a method results in an AttributeError being raised. In 
        order to set a method attribute, you need to explicitly set it on the 
        underlying function object
        """
        class C:
            def method(self):
                pass
        c = C()
        try:
            c.method.whoami = 'my name is method'  
            # can't set on the method
        except Exception as e:
            print(e)    
        c.method.__func__.whoami = 'my name is method'
        print('c.method.whoami:',c.method.whoami)
        return
        
    def code_object_test(self, *args, **kwargs):
        """
        Code objects are used by the implementation to represent 
        “pseudo-compiled” executable Python code such as a function body. They 
        differ from function objects because they don’t contain a reference to 
        their global execution environment. Code objects are returned by the 
        built-in compile() function and can be extracted from function objects 
        through their __code__ attribute. See also the code module.
        A code object can be executed or evaluated by passing it (instead of a 
        source string) to the exec() or eval() built-in functions.
        """
        code_obj = compile('sum([1, 2, 3])', '', 'eval')
        print("compile('sum([1, 2, 3])', '', 'eval'):", code_obj)
        print('exec(code_obj):',eval(code_obj))
        code_obj = compile('print("Hello world")', '', 'exec')
        exec(code_obj)
        return
        
    def type_object_test(self, *args, **kwargs):
        """
        Type objects represent the various object types. An object’s type is 
        accessed by the built-in function type(). There are no special 
        operations on types. The standard module types defines names for all 
        standard built-in types.
        Types are written like this: <class 'int'>.
        """
        numberList = [1, 2]
        print('type(numberList):',type(numberList))
        
        numberDict = {1: 'one', 2: 'two'}
        print('type(numberDict):',type(numberDict))
        
        class Foo:
            a = 0
        
        InstanceOfFoo = Foo()
        print('type(InstanceOfFoo):',type(InstanceOfFoo))
        
        o1 = type('X', (object,), dict(a='Foo', b=12))
        print('type(o1):',type(o1))
        print('vars(o1):',vars(o1))
        class test:
            a = 'Foo'
            b = 12
          
        o2 = type('Y', (test,), dict(a='Foo', b=12))
        print('type(o2):',type(o2))
        print('vars(o2):',vars(o2))
        
    def null_object_test(self, *args, **kwargs):
        """
        This object is returned by functions that don’t explicitly return a 
        value. It supports no special operations. There is exactly one null 
        object, named None (a built-in name). type(None)() produces the same 
        singleton.
        It is written as None.
        """
        obj = None
        print(obj, type(obj))
        return
        
    def ellipsis_object_test(self, *args, **kwargs):
        """
        This object is commonly used by slicing (see Slicings). It supports no 
        special operations. There is exactly one ellipsis object, named 
        Ellipsis (a built-in name). type(Ellipsis)() produces the Ellipsis 
        singleton.
        It is written as Ellipsis or "...".
        """
        class TestGetitem(object):
            def __getitem__(self, item):
                print('type:',type(item),'\titem:', item)
                
        t = TestGetitem()
        t[1]
        t[3-2]
        t['test']
        t[t]
        t[1:2]
        t[1:'this':t]
        t[...]
        t[...,1:]
        return
        
    def not_implemented_object_test(self, *args, **kwargs):
        """
        This object is returned from comparisons and binary operations when 
        they are asked to operate on types they don’t support. See Comparisons 
        for more information. There is exactly one NotImplemented object. 
        type(NotImplemented)() produces the singleton instance.
        It is written as NotImplemented.
        """
        def f1():
            print('type(NotImplemented):',type(NotImplemented))
            try:
                eval("None = 'hello'")
            except SyntaxError as e:
                print("can't assign to keyword",e.text)
                
            print(NotImplemented, type(NotImplemented))
        f1()
        def f2():
            print("\nNotImplemented = 'do not'")
            NotImplemented = 'do not'
            print('NotImplemented:',NotImplemented)
        f2()
        def f3():
            print('\nbool(NotImplemented):',bool(NotImplemented))
        f3()
        print()
        class A(object):
            def __init__(self, value):
                self.value = value
        
            def __eq__(self, other):
                if isinstance(other, A):
                    print('Comparing an A with an A')
                    return other.value == self.value
                if isinstance(other, B):
                    print('Comparing an A with a B')
                    return other.value == self.value
                print('Could not compare A with the other class')
                return NotImplemented
        
        class B(object):
            def __init__(self, value):
                self.value = value
        
            def __eq__(self, other):
                if isinstance(other, B):
                    print('Comparing a B with another B')
                    return other.value == self.value
                print('Could not compare B with the other class')
                return NotImplemented
            
        a1 = A(1)
        b1 = B(1)
        print('a1 == a1:',a1 == a1)
        print('b1 == b1:',b1 == b1)
        print('a1 == b1:',a1 == b1)
        print('b1 == a1:',b1 == a1)
        
    def boolean_value_test(self, *args, **kwargs):
        """
        Boolean values are the two constant objects False and True. They are 
        used to represent truth values (although other values can also be 
        considered false or true). In numeric contexts (for example when used 
        as the argument to an arithmetic operator), they behave like the 
        integers 0 and 1, respectively. The built-in function bool() can be 
        used to convert any value to a Boolean, if the value can be 
        interpreted as a truth value (see section Truth Value Testing above).
        They are written as False and True, respectively.
        """
        print('True:',True)
        print('type(True):',type(True))
        print('type(False):',type(False))
        return
        
    def internal_object_test(self, *args, **kwargs):
        """
        A few types used internally by the interpreter are exposed to the user.
        Their definitions may change with future versions of the interpreter, 
        but they are mentioned here for completeness.
        Internal Objects:
            - Code objects
            - Frame objects
            - Traceback objects
            - Slice objects
            - Static method objects
            - Class method objects
        """
        pass
    
    def special_attribute_test(self, *args, **kwargs):
        """
        The implementation adds a few special read-only attributes to several 
        object types, where they are relevant. Some of these are not reported 
        by the dir() built-in function.
        """
        # object.__dict__
        print('# object.__dict__')
        # A dictionary or other mapping object used to store an object’s 
        # (writable) attributes.
        
        class MyClass(object):
            class_var = 1
        
            def __init__(self, i_var):
                self.i_var = i_var
            def func(self):
                pass
        
        foo = MyClass(2)
        bar = MyClass(3)
        
        print('MyClass.__dict__:',MyClass.__dict__)
        print('foo.__dict__:',foo.__dict__)
        print('bar.__dict__:',bar.__dict__)
        
        # instance.__class__
        print('\n# instance.__class__')
        # The class to which a class instance belongs.
        class A:
            a = 1
            def __init(self, b):
                self.b = b
        a = A()
        print('a.__class__:',a.__class__)
        print('a.__class__ is A:',a.__class__ is A)
        
        # class.__bases__
        print('\n# class.__bases__')
        # The tuple of base classes of a class object.
        class A(object):
            pass
        class B(object):
            pass
        class C(A,B):
            pass
        class D(C):
            pass
        c = C()
        print('c.__class__.__bases__:',c.__class__.__bases__)
        d = D()
        print('d.__class__.bases__:',d.__class__.__bases__)
        
        # definition.__name__
        print('\n# definition.__name__')
        # The name of the class, function, method, descriptor, or generator 
        # instance.
        import File1 
  
        print("File2 __name__ = %s" %__name__)
          
        if __name__ == "__main__": 
            print("File2 is being run directly")
        else: 
            print("File2 is being imported")
            
        class A(object):
            def method(self):
                pass
        print('A.__name__:',A.__name__)
        a = A()
        print('a.method.__name__:',a.method.__name__)
        def func():
            pass
        print('func.__name__:',func.__name__)
        
        # definition.__qualname__
        print('\n# definition.__qualname__')
        # The qualified name of the class, function, method, descriptor, or 
        # generator instance.
        class C:
            class D:
                def meth(self):
                    pass
        print(C.D.meth.__qualname__)
        class A:
            class B:
                class C:
                    def me(self):
                        print('self.__module__:',self.__module__)
                        print('type(self).__name__:',type(self).__name__)
                        print('type(self).__qualname__:',type(self).__qualname__)
                        print('repr(self):',repr(self))
        x = A.B.C()
        x.me()
        
        # class.__mro__
        print('\n# class.__mro__')
        # This attribute is a tuple of classes that are considered when 
        # looking for base classes during method resolution.
        class X:
            pass
        print('X.__mro__:', X.__mro__)
        class Y:
            pass
        class Z:
            pass
        class A(X,Y):
            pass
        class B(Y,Z):
            pass
        class M(B,A,Z):
            pass
        print('M.__mro__:',M.__mro__)
        
        # class.mro()
        print('\n# class.mro()')
        # This method can be overridden by a metaclass to customize the method 
        # resolution order for its instances. It is called at class 
        # instantiation, and its result is stored in __mro__.
        print('M.mro():',M.mro())
        
        # class.__subclasses__()
        print('\n# class.__subclasses__()')
        # Each class keeps a list of weak references to its immediate 
        # subclasses. This method returns a list of all those references still 
        # alive.
        print('int.__subclasses__():',int.__subclasses__())
        print('X.__subclasses__():',X.__subclasses__())
        print('Y.__subclasses__():',Y.__subclasses__())
        print('Z.__subclasses__():',Z.__subclasses__())
        return
        
        
        
        
        
        
        
        
    
if __name__ == '__main__':
    bit = BuiltInType()
    
    ##Boolean
    #print('\n# Boolean')
    #print(bit.boolean_test.__doc__)
    #bit.boolean_test()

    ##Numeric
    #print('\n# Numeric')
    #print(bit.numeric_test.__doc__)
    #bit.numeric_test()
    
    ##Iterator
    #print('\n# Iterator')
    #print(bit.iterator_test.__doc__)
    #bit.iterator_test()
    
    ##Generator
    #print('\n# Generator')
    #print(bit.generator_test.__doc__)
    #bit.generator_test()
    
    ##Sequence
    #print('\n# Sequence')
    #print(bit.sequence_test.__doc__)
    #bit.sequence_test()
    
    ##Immutable Sequence
    #print('\n# Immutable sequence')
    #print(bit.immutable_sequence_test.__doc__)
    #bit.immutable_sequence_test()
    
    ##Mutable SequenceTrue
    #print('\n# Mutable Sequence')
    #print(bit.mutable_sequence_test.__doc__)
    #bit.mutable_sequence_test()
    
    ##list([iterable])
    #print('\n# list([iterable])')
    #print(bit.list_test.__doc__)
    #bit.list_test()
    
    ##tuple([iterable])
    #print('\n# tuple([iterable])')
    #print(bit.tuple_test.__doc__)
    #bit.tuple_test()
    
    ##range(stop)
    ##range(start, stop[, step])
    #print('\n# range(stop)\n# range(start, stop[, step])')
    #print(bit.range_test.__doc__)
    #bit.range_test()
    
    ##str(object='')
    ##str(object=b'', encoding='utf-8', errors='strict')
    #print("\n# str(object='')\n# str(object=b'', encoding='utf-8', errors='strict')")
    #print(bit.str_test.__doc__)
    #bit.str_test()
    
    ##String Methods
    #print('\n# String Methods')
    #print(bit.string_method_test.__doc__)
    #bit.string_method_test()
    
    ##Binary Sequence
    #print('\n# Binary Sequence')
    #print(bit.binary_sequence_test.__doc__)
    #bit.binary_sequence_test()
    
    ##memoryview(obj)
    #print('\n# memoryview(obj)')
    #print(bit.memoryview_test.__doc__)
    #bit.memoryview_test()
    
    ##Set
    #print('\n# Set')
    #print(bit.set_test.__doc__)
    #bit.set_test()
    
    #dict(**kwarg)
    #dict(mapping, **kwarg)
    #dict(iterable, **kwarg)
    print('\n# dict(**kwarg)\n# dict(mapping, **kwarg)\n# dict(iterable, **kwarg)')
    print(bit.dict_test.__doc__)
    bit.dict_test()
    
    ##Context Manager
    #print('\n# Context Manager')
    #print(bit.context_manager_test.__doc__)
    #bit.context_manager_test()
    
    ##Modules
    #print('\n# Modules')
    #print(bit.modules_test.__doc__)
    #bit.modules_test()

    ##Classes and Class Instances
    #print('\n# Classes and Class Instances')
    #print(bit.class_object_test.__doc__)
    #bit.class_object_test()
    
    ##Functions
    #print('\n# Functions')
    #print(bit.function_test.__doc__)
    #bit.function_test()
    
    ##Methods
    #print('\n# Methods')
    #print(bit.method_test.__doc__)
    #bit.method_test()
    
    ##Code Objects
    #print('\n# Code Objects')
    #print(bit.code_object_test.__doc__)
    #bit.code_object_test()
    
    ##Type Objects
    #print('\n# Type Objects')
    #print(bit.type_object_test.__doc__)
    #bit.type_object_test()
    
    ##The Null Object
    #print('\n# The Null Object')
    #print(bit.null_object_test.__doc__)
    #bit.null_object_test()
    
    #The Ellipsis Object
    #print('\n# The Ellipsis Object')
    #print(bit.ellipsis_object_test.__doc__)
    #bit.ellipsis_object_test()
    
    ##The NotImplemented Object
    #print('\n# The NotImplemented Object')
    #print(bit.not_implemented_object_test.__doc__)
    #bit.not_implemented_object_test()
    
    ##Boolean Values
    #print('\n# Boolean Values')
    #print(bit.boolean_value_test.__doc__)
    #bit.boolean_value_test()
    
    ##Internal Objects
    #print('\n# Internal Objects')
    #print(bit.internal_object_test.__doc__)
    #bit.internal_object_test()
    
    ##Special Attributes
    #print('\n# Special Attributes')
    #print(bit.special_attribute_test.__doc__)
    #bit.special_attribute_test()
    