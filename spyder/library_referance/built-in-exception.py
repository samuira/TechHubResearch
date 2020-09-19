# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:41:22 2019

@author: Rajesh Samui
"""

class BuiltInException:
    """
    Built in Exceptions
    In Python, all exceptions must be instances of a class that derives from 
    BaseException. In a try statement with an except clause that mentions a 
    particular class, that clause also handles any exception classes derived 
    from that class (but not exception classes from which it is derived). Two 
    exception classes that are not related via subclassing are never 
    equivalent, even if they have the same name.
    The built-in exception classes can be subclassed to define new exceptions; 
    programmers are encouraged to derive new exceptions from the Exception 
    class or one of its subclasses, and not from BaseException. More 
    information on defining exceptions is available in the Python Tutorial 
    under User-defined Exceptions.
    
    Exception hierarchy
    The class hierarchy for built-in exceptions is:
        
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning
               
    """
    def __init__(self):
        pass
    
    def baseexception_test(self, *args, **kwargs):
        """
        The base class for all built-in exceptions. It is not meant to be 
        directly inherited by user-defined classes (for that, use Exception). 
        If str() is called on an instance of this class, the representation of 
        the argument(s) to the instance are returned, or the empty string when 
        there were no arguments.
        args:
            The tuple of arguments given to the exception constructor. Some 
            built-in exceptions (like OSError) expect a certain number of 
            arguments and assign a special meaning to the elements of this 
            tuple, while others are usually called only with a single string 
            giving an error message.
        with_traceback(tb):
            This method sets tb as the new traceback for the exception and 
            returns the exception object. It is usually used in exception 
            handling code like this:
            try:
                ...
            except SomeException:
                tb = sys.exc_info()[2]
                raise OtherException(...).with_traceback(tb)
        """
        try:
            raise BaseException('BaseException raised')
        except BaseException as e:
            print(e)
            
    def system_exit_test(self, *args, **kwargs):
        """
        This exception is raised by the sys.exit() function. It inherits from 
        BaseException instead of Exception so that it is not accidentally 
        caught by code that catches Exception. This allows the exception to 
        properly propagate up and cause the interpreter to exit. When it is 
        not handled, the Python interpreter exits; no stack traceback is 
        printed. The constructor accepts the same optional argument passed to 
        sys.exit(). If the value is an integer, it specifies the system exit 
        status (passed to C’s exit() function); if it is None, the exit status 
        is zero; if it has another type (such as a string), the object’s value 
        is printed and the exit status is one.
        A call to sys.exit() is translated into an exception so that clean-up 
        handlers (finally clauses of try statements) can be executed, and so 
        that a debugger can execute a script without running the risk of 
        losing control. The os._exit() function can be used if it is 
        absolutely positively necessary to exit immediately (for example, in 
        the child process after a call to os.fork()).
        code:
            The exit status or error message that is passed to the constructor.
            (Defaults to None.)
        """
        import sys
        try:
            sys.exit(42)
        except BaseException as be:
            print('except by BaseException exception',be)
            print(be)
            print(sys.exc_info()[2].tb_frame.f_lineno)
            
        try:
            sys.exit()
        except Exception as e:
            print('except by Exception exception',e)
        except SystemExit as e:
            print('except by SystemExit exception.',e)
        return
            
    def keyboard_interrupt_test(self, *args, **kwargs):
        """
        Raised when the user hits the interrupt key (normally Control-C or 
        Delete). During execution, a check for interrupts is made regularly. 
        The exception inherits from BaseException so as to not be accidentally 
        caught by code that catches Exception and thus prevent the interpreter 
        from exiting.
        """
        import time
        try:
            while True:
                print("Press ctrl-c to exit.")
                time.sleep(2)
        except Exception as e:
            print('except by Exception exception',e)
        except KeyboardInterrupt as e:
            print('except by KeyboardInterrupt exception.',e)
        return
            
    def generator_exit_test(self, *args, **kwargs):
        """
        Raised when a generator or coroutine is closed; see generator.close() 
        and coroutine.close(). It directly inherits from BaseException instead 
        of Exception since it is technically not an error.
        """
        def pump():
            numbers = [1, 2, 3, 4]
            try:
                for number in numbers:
                    yield number
                    print("Have sent", number)
            except GeneratorExit:
                print("Have sent*", number)
            print("Last number was sent")
        
        for number in pump():
            print("Got", number)
            if number == 2:
                break
        print("All done")
        return
        
    def exception_test(self, *args, **kwargs):
        """
        All built-in, non-system-exiting exceptions are derived from this 
        class. All user-defined exceptions should also be derived from this 
        class.
        """
        try:
            raise Exception('yae!!! Exception')
        except Exception as e:
            print(e)
        return
        
    def stop_iteration_test(self, *args, **kwargs):
        """
        Raised by built-in function next() and an iterator’s __next__() method 
        to signal that there are no further items produced by the iterator.
        The exception object has a single attribute value, which is given as 
        an argument when constructing the exception, and defaults to None.
        When a generator or coroutine function returns, a new StopIteration 
        instance is raised, and the value returned by the function is used as
        the value parameter to the constructor of the exception.
        If a generator code directly or indirectly raises StopIteration, it is 
        converted into a RuntimeError (retaining the StopIteration as the new 
        exception’s cause).
        Changed in version 3.3: Added value attribute and the ability for 
        generator functions to use it to return a value.
        Changed in version 3.5: Introduced the RuntimeError transformation via 
        from __future__ import generator_stop, see PEP 479.
        Changed in version 3.7: Enable PEP 479 for all code by default: a 
        StopIteration error raised in a generator is transformed into a 
        RuntimeError.
        """
        iter_obj = iter([1,2,3])
        # infinite loop
        while True:
            try:
                # get the next item
                element = next(iter_obj)
                print('element:',element)
                # do something with element
            except StopIteration as e:
                # if StopIteration is raised, break from loop
                print('except by StopIteration exception',e)
                break
        [print('element:',x) for x in iter([1,2,3,4])]
        print('StopIteration exception handled by for loop')
        
        def gen(container):
            for x in container:
                yield x
        gen_ob = gen([1,2,3])
        while True:
            try:
                # get the next item
                element = next(gen_ob)
                print('element:',element)
                # do something with element
            except StopIteration as e:
                # if StopIteration is raised, break from loop
                print('except by StopIteration exception',e)
                break
        [print('element:',x) for x in gen([1,2,3])]
        print('StopIteration exception handled by for loop')
        return
        
    def stop_async_iteration_test(self, *args, **kwargs):
        """
        Must be raised by __anext__() method of an asynchronous iterator object
        to stop the iteration.
        """
        import asyncio
        
        class async_generator:
            def __init__(self, stop):
                self.i = 0
                self.stop = stop
        
            async def __aiter__(self):
                return self
        
            async def __anext__(self):
                i = self.i
                self.i += 1
                if self.i <= self.stop:
                    await asyncio.sleep(.1)
                    return i * i
                else:
                    raise StopAsyncIteration
        print('# using async for loop')
        async def main():
            async for i in async_generator(3):
                print(i)
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        
        print('# using __anext__')
        ag = async_generator(3)
        async def call():
            print(await ag.__anext__())
            print(await ag.__anext__())
            print(await ag.__anext__())
            try:
                print(await ag.__anext__())
            except StopAsyncIteration as e:
                print('except by StopAsyncIteration exception')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(call())
        return
        
    def arithmetic_error_test(self, *args, **kwargs):
        """
        The base class for those built-in exceptions that are raised for 
        various arithmetic errors: OverflowError, ZeroDivisionError, 
        FloatingPointError.
        """
        try:   
            a = 10/0
        except ArithmeticError as e:   
                print("except by ArithmeticError exception.",e)
        
        print('\n# ZeroDivisionError')
        # Raised when the second argument of a division or modulo operation is 
        # zero. The associated value is a string indicating the type of the 
        # operands and the operation.
        try:   
            a = 10/0
        except ZeroDivisionError as e:   
                print("except by ZeroDivisionError exception.",e)
                
        print('\n# OverflowError')
        # Raised when the result of an arithmetic operation is too large to be 
        # represented. This cannot occur for integers (which would rather raise
        # MemoryError than give up). However, for historical reasons, 
        # OverflowError is sometimes raised for integers that are outside a 
        # required range. Because of the lack of standardization of floating 
        # point exception handling in C, most floating point operations are not
        # checked.
        try:
            x = 10.5**10000000000000000000000
        except OverflowError as e:
            print('except by OverflowError exception.', e)
            
        print('\n# FloatingPointError')
        # Not currently used.
        return
        
    def assertion_error_test(self, *args, **kwargs):
        """
        Raised when an assert statement fails.
        if you run python with the -O flag, all assertions are stripped from 
        the code.
        """
        try:
            assert 1==2
        except AssertionError as e:
            print('except by AssertionError exception.',e)
        return
        
    def attribute_error_test(self, *args, **kwargs):
        """
        Raised when an attribute reference (see Attribute references) or 
        assignment fails. (When an object does not support attribute references
        or attribute assignments at all, TypeError is raised.)
        """
        class A:
            a = 0
            def __init__(self):
                self.b = 1
        a = A()
        print(a.a, a.b)
        try:
            print(a.c)
        except AttributeError as e:
            print('except by AttributeError exception.',e)
            
        try:
            print(A.b)
        except AttributeError as e:
            print('except by AttributeError exception.',e)
        return
        
    def buffer_error_test(self, *args, **kwargs):
        """
        Raised when a buffer related operation cannot be performed.
        """
        import io
        # Create byte array with string 'Hello'.
        array = io.BytesIO(b'Hello')
        print('array:',array)
        # Create a read-write copy of the bytearray.
        view = array.getbuffer()
        print('view:',view)
        try:
            # Add string ' world!' to existing bytearray.
            array.write(b' world!')
        except BufferError as e:
            print('except by BufferError exception.', e)
        return
        
    def eof_error_test(self, *args, **kwargs):
        """
        Raised when the input() function hits an end-of-file condition (EOF) 
        without reading any data. (N.B.: the io.IOBase.read() and 
        io.IOBase.readline() methods return an empty string when they hit EOF.)
        """
        try:
            file = open('some_file','r')
            print(file.readline())
            print(file.readline())
            print(file.readline())
        except EOFError as e:
            print('except by EOFError exception',e)
        return
        
    def import_error_test(self, *args, **kwargs):
        """
        Raised when the import statement has troubles trying to load a module. 
        Also raised when the “from list” in from ... import has a name that 
        cannot be found.
        The name and path attributes can be set using keyword-only arguments 
        to the constructor. When set they represent the name of the module 
        that was attempted to be imported and the path to any file which 
        triggered the exception, respectively.
        """
        try:
            import abcd
        except ImportError as e:
            print('except by ImportError exception.',e)
        
        print('\n# ModuleNotFoundError')
        # A subclass of ImportError which is raised by import when a module 
        # could not be located. It is also raised when None is found in 
        # sys.modules.
        # New in version 3.6.
        
    def lookup_error_test(self, *args, **kwargs):
        """
        The base class for the exceptions that are raised when a key or index 
        used on a mapping or sequence is invalid: IndexError, KeyError. This 
        can be raised directly by codecs.lookup().
        """
        foo = [1, 2, 3, 4, 4]
        try:
            foo[5]
        except LookupError as e:
            print('except by LookupError exception.',e)
        
        print('\n# IndexError')
        # Raised when a sequence subscript is out of range. (Slice indices are 
        # silently truncated to fall in the allowed range; if an index is not 
        # an integer, TypeError is raised.)
        try:
            foo[5]
        except IndexError as e:
            print('except by IndexError exception.',e)
            
        print('\n# KeyError')
        # Raised when a mapping (dictionary) key is not found in the set of 
        # existing keys.
        d = {'key':'value'}
        try:
            d['wrong-key']
        except KeyError as e:
            print('except by KeyError exception.',e)
        return
        
    def memory_error_test(self, *args, **kwargs):
        """
        Raised when an operation runs out of memory but the situation may 
        still be rescued (by deleting some objects). The associated value is a 
        string indicating what kind of (internal) operation ran out of memory. 
        Note that because of the underlying memory management architecture 
        (C’s malloc() function), the interpreter may not always be able to 
        completely recover from this situation; it nevertheless raises an 
        exception so that a stack traceback can be printed, in case a run-away 
        program was the cause.
        """
        try:
            a = []
            i = "1"
            while True:
                a.append(i)
                i += "1"*10000000000000
        except MemoryError as e:
            print("except by MemoryError exception.",e)
        return
        
    def name_error_test(self, *args, **kwargs):
        """
        Raised when a local or global name is not found. This applies only to 
        unqualified names. The associated value is an error message that 
        includes the name that could not be found.
        """
        try:
            print(a)
        except NameError as e:
            print('except by NameError exception.',e)
        
        print('\n# UnboundLocalError')
        # Raised when a reference is made to a local variable in a function or 
        # method, but no value has been bound to that variable. This is a 
        # subclass of NameError.
        counter = 0
        def increment():
          counter += 1
        try:
            increment()
        except UnboundLocalError as e:
            print('except by UnboundLocalError exception.',e)
        return
        
    def os_error_test(self, *args, **kwargs):
        """
        This exception is raised when a system function returns a 
        system-related error, including I/O failures such as “file not found” 
        or “disk full” (not for illegal argument types or other incidental 
        errors).
        The second form of the constructor sets the corresponding attributes, 
        described below. The attributes default to None if not specified. For 
        backwards compatibility, if three arguments are passed, the args 
        attribute contains only a 2-tuple of the first two constructor 
        arguments.
        The constructor often actually returns a subclass of OSError, as 
        described in OS exceptions below. The particular subclass depends on 
        the final errno value. This behaviour only occurs when constructing 
        OSError directly or via an alias, and is not inherited when 
        subclassing.
        """
        import os
        try:
            os.chdir('somenonexistingdir')
        except OSError as e:
            print('except by OSError exception.', e.errno, e.filename, 
                  e.strerror)
        
        print('\n# BlockingIOError')
        # Raised when an operation would block on an object (e.g. socket) set 
        # for non-blocking operation. Corresponds to errno EAGAIN, EALREADY, 
        # EWOULDBLOCK and EINPROGRESS.
#==============================================================================
#         #server
#         import socket
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.bind(("localhost", 8089))
#         sock.listen(2)
#         try:
#             while True:
#                 conn, addr = sock.accept()
#                 data = conn.recv(1024).decode("ascii")
#                 print(data)
#                 conn.send("hi from server".encode())
#         except Exception as e:
#             print('except by:',e)
#         finally:
#             sock.close()
#==============================================================================
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(("localhost",8089))
            # sock.setblocking(False) raise BlockingIOError exception
            sock.setblocking(False)
            sock.send("hi from client".encode())
            data = sock.recv(1024).decode("ascii")
            print(data)
        except BlockingIOError as e:
            print('except by BlockingIOError exception.',e)
        except Exception as e:
            print('run socket_server.py in a seperate terminal:',
                  e.with_traceback)
        finally:
            sock.close()
        
        print('\n# ChildProcessError')
        # Raised when an operation on a child process failed. Corresponds to 
        # errno ECHILD.
        print('have not found a proper example to implement this exception')
            
        print('\n# ConnectionError')
        # A base class for connection-related issues.
        # Subclasses are BrokenPipeError, ConnectionAbortedError, 
        # ConnectionRefusedError and ConnectionResetError.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
           sock.connect(("localhost",8089))
        except ConnectionError as e:    # This is the correct syntax
           print('except by ConnectionError exception.',e)
        
        print('\n# BrokenPipeError')
        # A subclass of ConnectionError, raised when trying to write on a pipe 
        # while the other end has been closed, or trying to write on a socket 
        # which has been shutdown for writing. Corresponds to errno EPIPE and 
        # ESHUTDOWN.
        try:
            sock.connect_ex(("localhost",8089))
            sock.send("hi from client".encode())
        except BrokenPipeError as e:
            print('except by BrokenPipeError exception.',e)
        finally:
            sock.close()
            
        print('\n# ConnectionAbortedError')
        # A subclass of ConnectionError, raised when a connection attempt is 
        # aborted by the peer. Corresponds to errno ECONNABORTED.
        print('have not found a proper example to implement this exception')
        
        print('\n# ConnectionRefusedError')
        # A subclass of ConnectionError, raised when a connection attempt is 
        # refused by the peer. Corresponds to errno ECONNREFUSED.
        print('have not found a proper example to implement this exception')
        
        print('\n# ConnectionResetError')
        # A subclass of ConnectionError, raised when a connection is reset by 
        # the peer. Corresponds to errno ECONNRESET.
        print('have not found a proper example to implement this exception')
        
        print('\n# FileExistsError')
        # Raised when trying to create a file or directory which already 
        # exists. Corresponds to errno EEXIST.
        print('/'.join(os.path.abspath(__file__).split('/')[:-1]))
        try:
            os.makedirs('new_dir')
        except FileExistsError as e:
            print('except by FileExistsError exception.',e)
            
        print('\n# FileNotFoundError')
        # Raised when a file or directory is requested but doesn’t exist. 
        # Corresponds to errno ENOENT.
        PATH = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        try:
            open(PATH+'/doesnotexist.txt','r')
        except FileNotFoundError as e:
            print('except by FileNotFoundError exception.',e)
            
        print('\n# InterruptedError')
        # Raised when a system call is interrupted by an incoming signal. 
        # Corresponds to errno EINTR.
        # Changed in version 3.5: Python now retries system calls when a 
        # syscall is interrupted by a signal, except if the signal handler 
        # raises an exception (see PEP 475 for the rationale), instead of 
        # raising InterruptedError.
        print('Changed in version 3.5')
        
        print('\n# IsADirectoryError')
        # Raised when a file operation (such as os.remove()) is requested on a 
        # directory. Corresponds to errno EISDIR.
        try:
            os.remove('new_dir')
        except IsADirectoryError as e:
            print('except by IsADirectoryError exception.', e)
            
        print('\n# NotADirectoryError')
        # Raised when a directory operation (such as os.listdir()) is 
        # requested on something which is not a directory. Corresponds to 
        # errno ENOTDIR.
        try:
            os.listdir('demo.txt')
        except NotADirectoryError as e:
            print('except by NotADirectoryError exception.',e)
            
        print('\n# PermissionError')
        # Raised when trying to run an operation without the adequate access 
        # rights - for example filesystem permissions. Corresponds to errno 
        # EACCES and EPERM.
        try:
            os.open(PATH+'/secret_file.txt', os.O_CREAT, 0o000)
        except PermissionError as e:
            print('except by PermissionError exception.', e)
            
        print('\n# ProcessLookupError')
        # Raised when a given process doesn’t exist. Corresponds to errno 
        # ESRCH.
        print('Need to have knowledge in subprocess.')
        
        print('\n# TimeoutError')
        # Raised when a system function timed out at the system level. 
        # Corresponds to errno ETIMEDOUT.
        import signal
        from contextlib import contextmanager
        
        @contextmanager
        def timeout(time):
            # Register a function to raise a TimeoutError on the signal.
            signal.signal(signal.SIGALRM, raise_timeout)
            # Schedule the signal to be sent after ``time``.
            signal.alarm(time)
        
            try:
                yield
            except TimeoutError as e:
                print('except by TimeoutError exception.',e)
            finally:
                # Unregister the signal so it won't be triggered
                # if the timeout is not reached.
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
        
        def raise_timeout(signum, frame):
            raise TimeoutError
        
        def my_func():
            # Add a timeout block.
            with timeout(1):
                print('entering block')
                import time
                time.sleep(10)
                print('This should never get printed because the line before timed out')
                
        my_func()
        return
        
    def reference_error_test(self, *args, **kwargs):
        """
        This exception is raised when a weak reference proxy, created by the 
        weakref.proxy() function, is used to access an attribute of the 
        referent after it has been garbage collected. For more information 
        on weak references, see the weakref module.
        """
        import gc 
        import weakref 
          
        class Foo(object): 
          
            def __init__(self, name): 
                self.name = name 
              
            def __del__(self): 
                print('(Deleting %s)' % self)
          
        obj = Foo('obj') 
        p = weakref.proxy(obj) 
          
        print('BEFORE:', p.name )
        obj = None
        try:
            print('AFTER:', p.name )
        except ReferenceError as e:
            print('except by ReferenceError exception.', e)    
        return
        
    def runtime_error_test(self, *args, **kwargs):
        """
        Raised when an error is detected that doesn’t fall in any of the other 
        categories. The associated value is a string indicating what precisely 
        went wrong. The interpreter does not raise this exception itself very 
        often, but some user code does.
        """
        try:
            raise RuntimeError('This will cause RuntimeError.')
        except RuntimeError as e:
            print('except by RuntimeError exception.', e)
            
        print('\n# NotImplementedError')
        # This exception is derived from RuntimeError. In user defined base 
        # classes, abstract methods should raise this exception when they 
        # require derived classes to override the method, or while the class 
        # is being developed to indicate that the real implementation still 
        # needs to be added.
        # Note:
        # It should not be used to indicate that an operator or method is not 
        # meant to be supported at all – in that case either leave the operator
        # / method undefined or, if a subclass, set it to None.
        # Note:
        # NotImplementedError and NotImplemented are not interchangeable, even 
        # though they have similar names and purposes. See NotImplemented for 
        # details on when to use it.
        import sys
        try:
           class Super(object):
                @property
                def example(self):
                    raise NotImplementedError("Subclasses should implement this!")
           s = Super()
           print(s.example)
        except NotImplementedError as e:
            print('except by NotImplementedError exception.', e)
            
        print('\n# RecursionError')
        # This exception is derived from RuntimeError. It is raised when the 
        # interpreter detects that the maximum recursion depth (see 
        # sys.getrecursionlimit()) is exceeded.
        # New in version 3.5: Previously, a plain RuntimeError was raised.
        def recur_factorial(n):
           """Function to return the factorial
           of a number using recursion"""
           if n == 1:
               return n
           else:
               return n*recur_factorial(n-1)
               
        print('Recursion Limit:',sys.getrecursionlimit())
        try:
            print(recur_factorial(972))
        except RecursionError as e:
            print('except by RecursionError exception.', e)
        return
        
    def syntax_error_test(self, *args, **kwargs):
        """
        Raised when the parser encounters a syntax error. This may occur in an 
        import statement, in a call to the built-in functions exec() or eval(),
        or when reading the initial script or standard input (also 
        interactively).
        Instances of this class have attributes filename, lineno, offset and 
        text for easier access to the details. str() of the exception instance 
        returns only the message.
        """
        try:
            exec('7+')
        except SyntaxError as e:
            print('except by SyntaxError exception.', e.msg,e.text)
            
        print('\n# IndentationError')
        # Base class for syntax errors related to incorrect indentation. This 
        # is a subclass of SyntaxError.
        try:
            exec("""def test2():
                        print('4 space')
                         print('5 space')
                 """)
        except IndentationError as e:
            print('except by IndentationError exception.', e.msg,e.text)
            
        print('\n# TabError')
        # Raised when indentation contains an inconsistent use of tabs and 
        # spaces. This is a subclass of IndentationError.
        try:
            exec("""def test2():
                    \tprint('tab')
                        print('space')
                 """)
        except TabError as e:
            print('except by TabError exception.', e.msg,e.text)
        return
            
    def system_error_test(self, *args, **kwargs):
        """
        Raised when the interpreter finds an internal error, but the situation 
        does not look so serious to cause it to abandon all hope. The 
        associated value is a string indicating what went wrong (in low-level 
        terms).
        You should report this to the author or maintainer of your Python 
        interpreter. Be sure to report the version of the Python interpreter 
        (sys.version; it is also printed at the start of an interactive Python
        session), the exact error message (the exception’s associated value) 
        and if possible the source of the program that triggered the error.
        """
        print('If SystemError occure then nothing mutch can be done about it.')
        return
        
    def type_error_test(self, *args, **kwargs):
        """
        Raised when an operation or function is applied to an object of 
        inappropriate type. The associated value is a string giving details 
        about the type mismatch.
        This exception may be raised by user code to indicate that an 
        attempted operation on an object is not supported, and is not meant to 
        be. If an object is meant to support a given operation but has not yet
        provided an implementation, NotImplementedError is the proper 
        exception to raise.
        Passing arguments of the wrong type (e.g. passing a list when an int is
        expected) should result in a TypeError, but passing arguments with the 
        wrong value (e.g. a number outside expected boundaries) should result 
        in a ValueError.
        """
        try:
            len(5342)
        except TypeError as e:
            print('except by TypeError exception.', e)
        return
        
    def value_error_test(self, *args, **kwargs):
        """
        Raised when an operation or function receives an argument that has the 
        right type but an inappropriate value, and the situation is not 
        described by a more precise exception such as IndexError.
        """
        try:
            int('f')
        except ValueError as e:
            print('except by ValueError exception.', e)
        
        print('\n# UnicodeError')
        # Raised when a Unicode-related encoding or decoding error occurs. It 
        # is a subclass of ValueError.
        # UnicodeError has attributes that describe the encoding or decoding 
        # error. For example, err.object[err.start:err.end] gives the 
        # particular invalid input that the codec failed on.
        print('have not found a proper example to raise UnicodeError')
        
        print('\n# UnicodeDecodeError')
        # Raised when a Unicode-related error occurs during decoding. It is a 
        # subclass of UnicodeError.
        print('have not found a proper example to raise UnicodeDecodeError')
        
        print('\n# UnicodeEncodeError')
        # Raised when a Unicode-related error occurs during encoding. It is a 
        # subclass of UnicodeError.
        print('have not found a proper example to raise UnicodeEncodeError')
        
        print('\n# UnicodeTranslateError')
        # Raised when a Unicode-related error occurs during translating. It is 
        # a subclass of UnicodeError.
        print('have not found a proper example to raise UnicodeTranslateError')
        return
        
    def warning_test(self, *args, **kwargs):
        """
        The following exceptions are used as warning categories; see the 
        Warning Categories documentation for more details.
        """
        pass
        
        
        
        
            
        
    
if __name__ == '__main__':
    bie = BuiltInException()
    print(bie.__doc__)
    
    ##BaseException
    #print('\n# BaseException')
    #print(bie.baseexception_test.__doc__)
    #bie.baseexception_test()
    
    ##SystemExit
    #print('\n# SystemExit')
    #print(bie.system_exit_test.__doc__)
    #bie.system_exit_test()
    
    ##KeyboardInterrupt
    #print('\n# KeyboardInterrupt')
    #print(bie.keyboard_interrupt_test.__doc__)
    #bie.keyboard_interrupt_test()
    
    ##GeneratorExit
    #print('\n# GeneratorExit')
    #print(bie.generator_exit_test.__doc__)
    #bie.generator_exit_test()
    
    ##Exception
    #print('\n# Exception')
    #print(bie.exception_test.__doc__)
    #bie.exception_test()
    
    ##StopIteration
    #print('\n# StopIteration')
    #print(bie.stop_iteration_test.__doc__)
    #bie.stop_iteration_test()
    
    ##StopAsyncIteration
    #print('\n# StopAsyncIteration')
    #print(bie.stop_async_iteration_test.__doc__)
    #bie.stop_async_iteration_test()
    
    ##ArithmeticError
    #print('\n# ArithmeticError')
    #print(bie.arithmetic_error_test.__doc__)
    #bie.arithmetic_error_test()
    
    ##AssertionError
    #print('\n# AssertionError')
    #print(bie.assertion_error_test.__doc__)
    #bie.assertion_error_test()
    
    ##AttributeError
    #print('\n# AttributeError')
    #print(bie.attribute_error_test.__doc__)
    #bie.attribute_error_test()
    
    ##BufferError
    #print('\n# BufferError')
    #print(bie.buffer_error_test.__doc__)
    #bie.buffer_error_test()
    
    ##EOFError
    #print('\n# EOFError')
    #print(bie.eof_error_test.__doc__)
    #bie.eof_error_test()
    
    ##ImportError
    #print('\n# ImportError')
    #print(bie.import_error_test.__doc__)
    #bie.import_error_test()
    
    ##LookupError
    #print('\n# LookupError')
    #print(bie.lookup_error_test.__doc__)
    #bie.lookup_error_test()
    
    ##MemoryError
    #print('\n# MemoryError')
    #print(bie.memory_error_test.__doc__)
    #bie.memory_error_test()
    
    ##NameError
    #print('\n# NameError')
    #print(bie.name_error_test.__doc__)
    #bie.name_error_test()
    
    ##OSError([arg])
    ##OSError(errno, strerror[, filename[, winerror[, filename2]]])
    #print('\n# OSError([arg])\n# OSError(errno, strerror[, filename[, winerror[, filename2]]])')
    #print(bie.os_error_test.__doc__)
    #bie.os_error_test()
    
    ##ReferenceError
    #print('\n# ReferenceError')
    #print(bie.reference_error_test.__doc__)
    #bie.reference_error_test()
    
    ##RuntimeError
    #print('\n# RuntimeError')
    #print(bie.runtime_error_test.__doc__)
    #bie.runtime_error_test()
    
    ##SyntaxError
    #print('\n# SyntaxError')
    #print(bie.syntax_error_test.__doc__)
    #bie.syntax_error_test()
    
    ##SystemError
    #print('\n# SystemError')
    #print(bie.system_error_test.__doc__)
    #bie.system_error_test()
    
    ##TypeError
    #print('\n# TypeError')
    #print(bie.type_error_test.__doc__)
    #bie.type_error_test()
    
    ##ValueError
    #print('\n# ValueError')
    #print(bie.value_error_test.__doc__)
    #bie.value_error_test()
    
    ##Warning
    #print('\n# Warning')
    #print(bie.warning_test.__doc__)
    #bie.warning_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    