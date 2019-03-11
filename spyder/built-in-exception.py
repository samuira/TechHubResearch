# -*- coding: utf-8 -*-

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
        pass
    
if __name__ == '__main__':
    bie = BuiltInException()
    
    # BaseException
    print('\n# BaseException')
    #bie.baseexception_test()
    
    # SystemExit
    print('\n# SystemExit')
    #bie.system_exit_test()
    
    # KeyboardInterrupt
    print('\n# KeyboardInterrupt')
    #bie.keyboard_interrupt_test()
    
    # GeneratorExit
    print('\n# GeneratorExit')
    #bie.generator_exit_test()
    
    # Exception
    print('\n# Exception')
    #bie.exception_test()
    
    # StopIteration
    print('\n# StopIteration')
    #bie.stop_iteration_test()
    
    # StopAsyncIteration
    print('\n# StopAsyncIteration')
    bie.stop_async_iteration_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    