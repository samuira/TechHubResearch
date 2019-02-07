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
        
    def sequence_test(self, *args, **kwargs):
        """
        There are three basic sequence types: lists, tuples, and range 
        objects. Additional sequence types tailored for processing of binary 
        data and text strings are described in dedicated sections.
        """
        pass

                        
    
if __name__ == '__main__':
    bit = BuiltInType()
    
    # boolean
    print('\n# boolean')
    #bit.boolean_test()

    # numeric
    print('\n# numeric')
    #bit.numeric_test()
    
    # iterator
    print('\n# iterator')
    #bit.iterator_test()
    
    # generator
    print('\n# generator')
    #bit.generator_test()
    
    # sequence
    print('\n# sequence')
    bit.sequence_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    