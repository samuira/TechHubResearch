# -*- coding: utf-8 -*-


class BuiltInType:
    """
    
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



        

         



        
        
        
        
        
    
if __name__ == '__main__':
    bit = BuiltInType()
    
    # Boolean
    print('\n# Boolean')
    #bit.boolean_test()

    # Numeric
    print('\n# Numeric')
    #bit.numeric_test()
    
    # Iterator
    print('\n# Iterator')
    #bit.iterator_test()
    
    # Generator
    print('\n# Generator')
    #bit.generator_test()
    
    # Sequence
    print('\n# Sequence')
    #bit.sequence_test()
    
    # Immutable Sequence
    print('\n# Immutable sequence')
    #bit.immutable_sequence_test()
    
    # Mutable Sequence
    print('\n# Mutable Sequence')
    #bit.mutable_sequence_test()
    
    # list([iterable])
    print('\n# list([iterable])')
    #bit.list_test()
    
    # tuple([iterable])
    print('\n# tuple([iterable])')
    #bit.tuple_test()
    
    # range(stop)
    # range(start, stop[, step])
    print('\n# range(stop)\n# range(start, stop[, step])')
    #bit.range_test()
    
    # str(object='')
    # str(object=b'', encoding='utf-8', errors='strict')
    print("\n# str(object='')\n# str(object=b'', encoding='utf-8', errors='strict')")
    #bit.str_test()
    
    # String Methods
    print('\n# String Methods')
    bit.string_method_test()
    
    
    
    
    
    
    
    
    
    
    
    
    