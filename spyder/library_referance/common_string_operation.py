# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 14:31:24 2019

@author: Rajesh Samui
"""

import string

class CommonStringOperation:
    """
    Common String Operations:
    """
    def __init__(self):
        pass
    
    def string_constant_test(self):
        """
        The constants defined in this module are:
        """
        print('\n# string.ascii_letters')
        # The concatenation of the ascii_lowercase and ascii_uppercase 
        # constants described below. This value is not locale-dependent.
        print(string.ascii_letters)
        
        print('\n# string.ascii_lowercase')
        # The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not
        # locale-dependent and will not change.
        print(string.ascii_lowercase)
        
        print('\n# string.ascii_uppercase')
        # The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not
        # locale-dependent and will not change.
        print(string.ascii_uppercase)
        
        print('\n# string.digits')
        # The string '0123456789'.
        print(string.digits)
        
        print('\n# string.hexdigits')
        # The string '0123456789abcdefABCDEF'.
        print(string.hexdigits)
        
        print('\n# string.octdigits')
        # The string '01234567'.
        print(string.octdigits)
        
        print('\n# string.punctuation')
        # String of ASCII characters which are considered punctuation 
        # characters in the C locale.
        print(string.punctuation)
    
        print('\n# string.printable')
        # String of ASCII characters which are considered printable. This is a 
        # combination of digits, ascii_letters, punctuation, and whitespace.
        print(string.printable)
        
        print('\n# string.whitespace')
        # A string containing all ASCII characters that are considered 
        # whitespace. This includes the characters space, tab, linefeed, 
        # return, formfeed, and vertical tab.
        print('start',string.whitespace,'end')
        return
        
    def custom_string_formatting_test(self):
        """
        The built-in string class provides the ability to do complex variable 
        substitutions and value formatting via the format() method described 
        in PEP 3101. The Formatter class in the string module allows you to 
        create and customize your own string formatting behaviors using the 
        same implementation as the built-in format() method.
        """
        print('\n# string.Formatter')
        print('\n# format(format_string, *args, **kwargs)')
        """
        The primary API method. It takes a format string and an arbitrary 
        set of positional and keyword arguments. It is just a wrapper that 
        calls vformat().
        Changed in version 3.7: A format string argument is now 
        positional-only.
        """
        from string import Formatter
        formatter = Formatter()
        print("formatter.format('{website}', website='JournalDev'):",
                                formatter.format('{website}', 
                                                 website='JournalDev'))
        print("formatter.format('{} {website}', 'Welcome to', website='JournalDev'):",
                                formatter.format('{} {website}', 'Welcome to', 
                                                 website='JournalDev'))
        # format() behaves in similar manner
        print("'{} {website}'.format('Welcome to', website='JournalDev'):",
        '{} {website}'.format('Welcome to', website='JournalDev'))
        
        print('\n# vformat(format_string, args, kwargs)')
        """
        This function does the actual work of formatting. It is exposed as a 
        separate function for cases where you want to pass in a predefined 
        dictionary of arguments, rather than unpacking and repacking the 
        dictionary as individual arguments using the *args and **kwargs 
        syntax. vformat() does the work of breaking up the format string 
        into character data and replacement fields. It calls the various 
        methods described below.
        """
        print("formatter.vformat('{website}',(), {'website':'JournalDev'}):",
                                 formatter.vformat('{website}',(), 
                                                   {'website':'JournalDev'}))
        print(
            """
            formatter.vformat('{} {website}', ('Welcome to',), 
            {'website':'JournalDev'}):
            """,formatter.vformat('{} {website}', ('Welcome to',), 
                                  {'website':'JournalDev'}))
                
        print('\n# parse(format_string)')
        """
        Loop over the format_string and return an iterable of tuples 
        (literal_text, field_name, format_spec, conversion). This is used by 
        vformat() to break the string into either literal text, or replacement 
        fields.
        The values in the tuple conceptually represent a span of literal text 
        followed by a single replacement field. If there is no literal text 
        (which can happen if two replacement fields occur consecutively), then 
        literal_text will be a zero-length string. If there is no replacement 
        field, then the values of field_name, format_spec and conversion will 
        be None.
        """
        s = 'please do {k1!s:.3} something or {k2!a:4} anything extraordinay {k3!r}'
        print(s)
        for p in formatter.parse(s):
            print(p)
            
        print('\n#  get_field(field_name, args, kwargs)')
        """
        Given field_name as returned by parse() (see above), convert it to an 
        object to be formatted. Returns a tuple (obj, used_key). The default 
        version takes strings of the form defined in PEP 3101, such as 
        “0[name]” or “label.title”. args and kwargs are as passed in to 
        vformat(). The return value used_key has the same meaning as the key 
        parameter to get_value().
        """
        print('Unable to understand how to use this function()')
        
        print('\n# get_value(key, args, kwargs)')
        """
        Retrieve a given field value. The key argument will be either an 
        integer or a string. If it is an integer, it represents the index of 
        the positional argument in args; if it is a string, then it represents 
        a named argument in kwargs.
        The args parameter is set to the list of positional arguments to 
        vformat(), and the kwargs parameter is set to the dictionary of 
        keyword arguments.
        For compound field names, these functions are only called for the first
        component of the field name; Subsequent components are handled through 
        normal attribute and indexing operations.
        So for example, the field expression ‘0.name’ would cause get_value() 
        to be called with a key argument of 0. The name attribute will be 
        looked up after get_value() returns by calling the built-in getattr() 
        function.
        If the index or keyword refers to an item that does not exist, then an 
        IndexError or KeyError should be raised.
        """
        print('Unable to understand how to use this function()')
        
        print('\n# check_unused_args(used_args, args, kwargs)')
        """
        Implement checking for unused arguments if desired. The arguments to 
        this function is the set of all argument keys that were actually 
        referred to in the format string (integers for positional arguments, 
        and strings for named arguments), and a reference to the args and 
        kwargs that was passed to vformat. The set of unused args can be 
        calculated from these parameters. check_unused_args() is assumed to 
        raise an exception if the check fails.
        """
        print('Unable to understand how to use this function()')
        
        print('\n# format_field(value, format_spec)')
        """
        format_field() simply calls the global format() built-in. The method 
        is provided so that subclasses can override it.
        """
        print('Unable to understand how to use this function()')
    
        print('\n# convert_field(value, conversion)')
        """
        Converts the value (returned by get_field()) given a conversion type 
        (as in the tuple returned by the parse() method). The default version 
        understands ‘s’ (str), ‘r’ (repr) and ‘a’ (ascii) conversion types.
        """
        print('Unable to understand how to use this function()')
        return
        
    def format_string_syntax_test(self):
        """
        Format strings contain “replacement fields” surrounded by curly braces 
        {}. Anything that is not contained in braces is considered literal text
        , which is copied unchanged to the output. If you need to include a 
        brace character in the literal text, it can be escaped by doubling: {{ 
        and }}.
        The grammar for a replacement field is as follows:
        replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
        field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
        arg_name          ::=  [identifier | digit+]
        attribute_name    ::=  identifier
        element_index     ::=  digit+ | index_string
        index_string      ::=  <any source character except "]"> +
        conversion        ::=  "r" | "s" | "a"
        format_spec       ::=  <described in the next section>
        """
        # References first positional argument
        print('"First, thou shalt count to {0}".format(5):',
        "First, thou shalt count to {0}".format(5))
        
        # Implicitly references the first positional argument
        print('"Bring me a {}".format(5):',"Bring me a {}".format(5))
        
        # Same as "From {0} to {1}"
        print('"From {} to {}".format(5,7):',"From {} to {}".format(5,7))
        
        # References keyword argument 'name'
        print('"My quest is {name}".format(name="about to begin."):',
        "My quest is {name}".format(name="about to begin."))
        
        class A:
            weight = 60
        a = A()
        # 'weight' attribute of first positional arg
        print('"Weight in tons {0.weight}".format(a):',
        "Weight in tons {0.weight}".format(a))
        
        ar = [3,4]
        # First element of keyword argument 'players'.
        print('"Units destroyed: {players[0]}".format(players=ar):',
        "Units destroyed: {players[0]}".format(players=ar))
        
        """
        The conversion field causes a type coercion before formatting. Normally
        , the job of formatting a value is done by the __format__() method of 
        the value itself. However, in some cases it is desirable to force a 
        type to be formatted as a string, overriding its own definition of 
        formatting. By converting the value to a string before calling 
        __format__(), the normal formatting logic is bypassed.
        Three conversion flags are currently supported: '!s' which calls str() 
        on the value, '!r' which calls repr() and '!a' which calls ascii().
        """
        # Calls str() on the argument first
        print('"Harold\'s a clever {0!s}".format(5):',
        "Harold's a clever {0!s}".format(5))
        
        class Person:
            name = 'Adam'
        
            def __repr__(self):
                return repr(self.name)
        
        print('repr(Person()):',repr(Person()))
        # Calls repr() on the argument first
        print('"Bring out the holy {name!r}".format(name=Person()):',
        "Bring out the holy {name!r}".format(name=Person()))
        
        # Calls ascii() on the argument first
        print(ascii('Pythön is interesting'))
        print("More {!a}".format('Pythön is interesting'))
        
        """
        The format_spec field contains a specification of how the value should 
        be presented, including such details as field width, alignment, 
        padding, decimal precision and so on. Each value type can define its 
        own “formatting mini-language” or interpretation of the format_spec.
        """
        return
        
    def format_specification_mini_language_test(self):
        """
        A general convention is that an empty format string ("") produces the 
        same result as if you had called str() on the value. A non-empty 
        format string typically modifies the result.
        The general form of a standard format specifier is:
        format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
        fill            ::=  <any character>
        align           ::=  "<" | ">" | "=" | "^"
        sign            ::=  "+" | "-" | " "
        width           ::=  digit+
        grouping_option ::=  "_" | ","
        precision       ::=  digit+
        type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
        
        If a valid align value is specified, it can be preceded by a fill 
        character that can be any character and defaults to a space if omitted.
        The meaning of the various alignment options is as follows:
        Option 	Meaning
        '<' 	     Forces the field to be left-aligned within the available space (this is the default for most objects).
        '>' 	     Forces the field to be right-aligned within the available space (this is the default for numbers).
        '=' 	     Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types. It becomes the default when ‘0’ immediately precedes the field width.
        '^' 	     Forces the field to be centered within the available space.
        
        Note that unless a minimum field width is defined, the field width will
        always be the same size as the data to fill it, so that the alignment 
        option has no meaning in this case.
        
        The sign option is only valid for number types, and can be one of the 
        following:
        Option     Meaning
        '+' 	    indicates that a sign should be used for both positive as well as negative numbers.
        '-' 	    indicates that a sign should be used only for negative numbers (this is the default behavior).
        space 	    indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.
        
        The '#' option causes the “alternate form” to be used for the 
        conversion. The alternate form is defined differently for different 
        types. This option is only valid for integer, float, complex and 
        Decimal types. For integers, when binary, octal, or hexadecimal output 
        is used, this option adds the prefix respective '0b', '0o', or '0x' to 
        the output value. For floats, complex and Decimal the alternate form 
        causes the result of the conversion to always contain a decimal-point 
        character, even if no digits follow it. Normally, a decimal-point 
        character appears in the result of these conversions only if a digit 
        follows it. In addition, for 'g' and 'G' conversions, trailing zeros 
        are not removed from the result.
        The ',' option signals the use of a comma for a thousands separator. 
        For a locale aware separator, use the 'n' integer presentation type 
        instead.
        Changed in version 3.1: Added the ',' option (see also PEP 378).
        The '_' option signals the use of an underscore for a thousands 
        separator for floating point presentation types and for integer 
        presentation type 'd'. For integer presentation types 'b', 'o', 'x', 
        and 'X', underscores will be inserted every 4 digits. For other 
        presentation types, specifying this option is an error.
        Changed in version 3.6: Added the '_' option (see also PEP 515).
        width is a decimal integer defining the minimum field width. If not 
        specified, then the field width will be determined by the content.
        When no explicit alignment is given, preceding the width field by a 
        zero ('0') character enables sign-aware zero-padding for numeric types.
        This is equivalent to a fill character of '0' with an alignment type of
        '='.
        The precision is a decimal number indicating how many digits should be 
        displayed after the decimal point for a floating point value formatted 
        with 'f' and 'F', or before and after the decimal point for a floating 
        point value formatted with 'g' or 'G'. For non-number types the field 
        indicates the maximum field size - in other words, how many characters 
        will be used from the field content. The precision is not allowed for 
        integer values.
        The available string presentation types are:
        Type 	Meaning
        's' 	String format. This is the default type for strings and may be omitted.
        None 	The same as 's'.
        
        The available integer presentation types are:
        Type 	Meaning
        'b' 	Binary format. Outputs the number in base 2.
        'c' 	Character. Converts the integer to the corresponding unicode character before printing.
        'd' 	Decimal Integer. Outputs the number in base 10.
        'o' 	Octal format. Outputs the number in base 8.
        'x' 	Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9.
        'X' 	Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9.
        'n' 	Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.
        None 	The same as 'd'.
        
        In addition to the above presentation types, integers can be formatted 
        with the floating point presentation types listed below (except 'n' 
        and None). When doing so, float() is used to convert the integer to a 
        floating point number before formatting.
        The available presentation types for floating point and decimal values 
        are:
        Type 	Meaning
        'e' 	Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. The default precision is 6.
        'E' 	Exponent notation. Same as 'e' except it uses an upper case ‘E’ as the separator character.
        'f' 	Fixed-point notation. Displays the number as a fixed-point number. The default precision is 6.
        'F' 	Fixed-point notation. Same as 'f', but converts nan to NAN and inf to INF.
        'g' 	
    
               General format. For a given precision p >= 1, this rounds the 
               number to p significant digits and then formats the result in 
               either fixed-point format or in scientific notation, depending 
               on its magnitude.
    
               The precise rules are as follows: suppose that the result 
               formatted with presentation type 'e' and precision p-1 would 
               have exponent exp. Then if -4 <= exp < p, the number is 
               formatted with presentation type 'f' and precision p-1-exp. 
               Otherwise, the number is formatted with presentation type 'e' 
               and precision p-1. In both cases insignificant trailing zeros 
               are removed from the significand, and the decimal point is also 
               removed if there are no remaining digits following it.
    
               Positive and negative infinity, positive and negative zero, and 
               nans, are formatted as inf, -inf, 0, -0 and nan respectively, 
               regardless of the precision.
    
               A precision of 0 is treated as equivalent to a precision of 1. 
               The default precision is 6.
        'G' 	General format. Same as 'g' except switches to 'E' if the number gets too large. The representations of infinity and NaN are uppercased, too.
        'n' 	Number. This is the same as 'g', except that it uses the current locale setting to insert the appropriate number separator characters.
        '%' 	Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.
        None 	Similar to 'g', except that fixed-point notation, when used, has at least one digit past the decimal point. The default precision is as high as needed to represent the particular value. The overall effect is to match the output of str() as altered by the other format modifiers.
        """
        pass
    
    def format_example_test(self):
        """
        In most of the cases the syntax is similar to the old %-formatting, 
        with the addition of the {} and with : used instead of %. For example, 
        '%03.2f' can be translated to '{:03.2f}'.
        """
        # Accessing arguments by position:
        print("\n'{0}, {1}, {2}'.format('a', 'b', 'c'):",
        '{0}, {1}, {2}'.format('a', 'b', 'c'))
        # 3.1+ only
        print("'{}, {}, {}'.format('a', 'b', 'c'):",
        '{}, {}, {}'.format('a', 'b', 'c'))  
        print("'{2}, {1}, {0}'.format('a', 'b', 'c'):",
        '{2}, {1}, {0}'.format('a', 'b', 'c'))
        # unpacking argument sequence
        print("'{2}, {1}, {0}'.format(*'abc'):",'{2}, {1}, {0}'.format(*'abc'))
        print("'{0}{1}{0}'.format('abra', 'cad'):",
        '{0}{1}{0}'.format('abra', 'cad'))
        
        # Accessing arguments by name:
        print("\n'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'):",
        'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
        coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
        print("coord =",coord)
        print("'Coordinates: {latitude}, {longitude}'.format(**coord):",
        'Coordinates: {latitude}, {longitude}'.format(**coord))
        
        # Accessing arguments’ attributes:
        c = 3-5j
        print('\nc =',c)
        print("'The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c):",
        'The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c))
        class Point:
            def __init__(self, x, y):
                self.x, self.y = x, y
            def __str__(self):
                return 'Point({self.x}, {self.y})'.format(self=self)
                
        print("str(Point(4, 2)):",str(Point(4, 2)))
        
        # Accessing arguments’ items:
        coord = (3, 5)
        print('\ncoord =',coord)
        print("'X: {0[0]};  Y: {0[1]}'.format(coord):",
                    'X: {0[0]};  Y: {0[1]}'.format(coord))
        
        # Replacing %s and %r:
        print('\n"repr() shows quotes: {!r}; str() doesn\'t: {!s}".format("test1", "test2"):',
              "repr() shows quotes: {!r}; str() doesn\'t: {!s}".format("test1", "test2"))
        
        # Aligning the text and specifying a width:
        print("\n'*{:<30}#'.format('left aligned'):",
        '*{:<30}#'.format('left aligned'))
        print("'*{:>30}#'.format('right aligned'):",
        '*{:>30}#'.format('right aligned'))
        print("'*{:^30}#'.format('centered'):",
        '*{:^30}#'.format('centered'))
        # use '-' as a fill char
        print("'*{:^30}#'.format('centered'):",
        '*{:-^30}#'.format('centered'))
        
        # Replacing %+f, %-f, and % f and specifying a sign:
        # show it always
        print("\n'{:+f}; {:+f}'.format(3.14, -3.14):",
        '{:+f}; {:+f}'.format(3.14, -3.14))
        # show a space for positive numbers
        print("'{: f}; {: f}'.format(3.14, -3.14):",
        '{: f}; {: f}'.format(3.14, -3.14))
        # show only the minus -- same as '{:f}; {:f}'
        print("'{:-f}; {:-f}'.format(3.14, -3.14):",
        '{:-f}; {:-f}'.format(3.14, -3.14))
        
        # Replacing %x and %o and converting the value to different bases:
        # format also supports binary numbers
        print('\n"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42):'
              ,"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
        # with 0x, 0o, or 0b as prefix:
        print('"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42):',
              "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
        
        # Using the comma as a thousands separator:
        print("\n'{:,}'.format(1234567890):",'{:,}'.format(1234567890))
        
        # Expressing a percentage:
        points = 19
        total = 22
        print("\n'Correct answers: {:.2%}'.format(points/total):",
              'Correct answers: {:.2%}'.format(points/total))
        
        # Using type-specific formatting:
        import datetime
        d = datetime.datetime(2010, 7, 4, 12, 15, 58)
        print('\nd =',d)
        print("'{:%Y-%m-%d %H:%M:%S}'.format(d):",
        '{:%Y-%m-%d %H:%M:%S}'.format(d))
        
        # Nesting arguments and more complex examples:
        print()
        for align, text in zip('<^>', ['left', 'center', 'right']):
            print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
        octets = [192, 168, 0, 1]
        print('octets =',octets)
        print("'{:02X}{:02X}{:02X}{:02X}'.format(*octets):",
        '{:02X}{:02X}{:02X}{:02X}'.format(*octets))
        # Changed in version 3.6: Added the '_' option (see also PEP 515).
        # print('int(_, 16):',int(_, 16)) 
        width = 5
        for num in range(5,12): 
            for base in 'dXob':
                print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
            print()
            
    def template_string_test(self):
        """
        Template strings support $-based substitutions, using the following 
        rules:
            - $$ is an escape; it is replaced with a single $.
            - $identifier names a substitution placeholder matching a mapping 
              key of "identifier". By default, "identifier" is restricted to 
              any case-insensitive ASCII alphanumeric string (including 
              underscores) that starts with an underscore or ASCII letter. The 
              first non-identifier character after the $ character terminates 
              this placeholder specification.
            - ${identifier} is equivalent to $identifier. It is required when 
              valid identifier characters follow the placeholder but are not 
              part of the placeholder, such as "${noun}ification".

        """
        print('\n# string.Template(template)')
        # The constructor takes a single argument which is the template string.
        
        print('\n# substitute(mapping, **kwds)')
        """
        Performs the template substitution, returning a new string. mapping is 
        any dictionary-like object with keys that match the placeholders in 
        the template. Alternatively, you can provide keyword arguments, where 
        the keywords are the placeholders. When both mapping and kwds are given
        and there are duplicates, the placeholders from kwds take precedence.
        """
        
        print('\n# safe_substitute(mapping, **kwds)')
        """
        Like substitute(), except that if placeholders are missing from mapping
        and kwds, instead of raising a KeyError exception, the original 
        placeholder will appear in the resulting string intact. Also, unlike 
        with substitute(), any other appearances of the $ will simply return $ 
        instead of raising ValueError.
        While other exceptions may still occur, this method is called “safe” 
        because it always tries to return a usable string instead of raising 
        an exception. In another sense, safe_substitute() may be anything other
        than safe, since it will silently ignore malformed templates containing
        dangling delimiters, unmatched braces, or placeholders that are not 
        valid Python identifiers.
        """
        
        print('\n# template')
        """
        This is the object passed to the constructor’s template argument. In 
        general, you shouldn’t change it, but read-only access is not enforced.
        """
        from string import Template
        s = Template('$who likes $what')
        print("s =Template('$who likes $what'):", s)
        print("s.substitute(who='tim', what='kung pao'):",
              s.substitute(who='tim', what='kung pao'))
        d = dict(who='tim')
        try:
            Template('Give $who $100').substitute(d)
        except ValueError as e:
            print('except by ValueError exception.',e)
        try:
            Template('$who likes $what').substitute(d)
        except KeyError as e:
            print('except by KeyError exception.',e)
            
        print("Template('$who likes $what').safe_substitute(d):",
              Template('$who likes $what').safe_substitute(d))
        print("Template('Give $who $100').safe_substitute(d):",
              Template('Give $who $100').safe_substitute(d))
        
        print('\n# string.capwords(s, sep=None)')
        """
        Split the argument into words using str.split(), capitalize each word 
        using str.capitalize(), and join the capitalized words using 
        str.join(). If the optional second argument sep is absent or None, runs
        of whitespace characters are replaced by a single space and leading and
        trailing whitespace are removed, otherwise sep is used to split and 
        join the words.
        """
        s='The man who is swimming against the stream knows the strength of it.'
        print('s =',s)
        print('string.capwords(s):',string.capwords(s))
        return
        
    
if __name__ == '__main__':
    cso = CommonStringOperation()
    print(cso.__doc__)

#    print('\n# String constants')
#    print(cso.string_constant_test.__doc__)
#    cso.string_constant_test()
    
#    print('\n# Custom String Formatting')
#    print(cso.custom_string_formatting_test.__doc__)
#    cso.custom_string_formatting_test()

#    print('\n# Format String Syntax')
#    print(cso.format_string_syntax_test.__doc__)
#    cso.format_string_syntax_test()

#    print('\n# Format Specification Mini-Language')
#    print(cso.format_specification_mini_language_test.__doc__)
#    cso.format_specification_mini_language_test()

#    print('\n# Format examples')
#    print(cso.format_example_test.__doc__)
#    cso.format_example_test()

#    print('\n# Template strings')
#    print(cso.template_string_test.__doc__)
#    cso.template_string_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
