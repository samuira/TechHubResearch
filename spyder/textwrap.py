# -*- coding: utf-8 -*-
"""
Created on Thu July 4 20:02:00 2019

@author: Rajesh Samui
"""
import textwrap


class TextWrap:
    """
    The textwrap module provides some convenience functions, as well as 
    TextWrapper, the class that does all the work. If you’re just wrapping or 
    filling one or two text strings, the convenience functions should be good 
    enough; otherwise, you should use an instance of TextWrapper for 
    efficiency.
    
    wrap(), fill() and shorten() work by creating a TextWrapper instance and 
    calling a single method on it. That instance is not reused, so for 
    applications that process many text strings using wrap() and/or fill(), it 
    may be more efficient to create your own TextWrapper object.

    Text is preferably wrapped on whitespaces and right after the hyphens in 
    hyphenated words; only then will long words be broken if necessary, unless 
    TextWrapper.break_long_words is set to false.
    """
    def __init__(self):
        pass
    
    def textwrap_wrap_test(self):
        """
        Wraps the single paragraph in text (a string) so every line is at most 
        width characters long. Returns a list of output lines, without final 
        newlines.

        Optional keyword arguments correspond to the instance attributes of 
        TextWrapper, documented below. width defaults to 70.
        
        See the TextWrapper.wrap() method for additional details on how wrap() 
        behaves.
        """
        value = """This function wraps the input paragraph such that each line 
in the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""
        print('value =', value)
        # Wrap this text. 
        word_list = textwrap.wrap(value, 20) 
        print('word_list:', word_list)
        # Print each line. 
        for element in word_list: 
            print('length ->', len(element), ':', element)
        return
    
    def textwrap_fill_test(self):
        """
        Wraps the single paragraph in text, and returns a single string 
        containing the wrapped paragraph. fill() is shorthand for 
        "\\n".join(wrap(text, ...))
        """
        value = """This function returns the answer as STRING and not LIST."""
        print('value =', value)
        string = textwrap.fill(value, 20)
        print ('string:', string, sep='\n')
        return
    
    def textwrap_shorten_test(self):
        """
        Collapse and truncate the given text to fit in the given width.

        First the whitespace in text is collapsed (all whitespace is replaced 
        by single spaces). If the result fits in the width, it is returned. 
        Otherwise, enough words are dropped from the end so that the remaining 
        words plus the placeholder fit within width:
        """
        print('textwrap.shorten("hello  world!", width=12):',
                                textwrap.shorten("Hello  world!", width=12))
        print('textwrap.shorten("Hello  world!", width=11):', 
              textwrap.shorten("Hello  world!", width=11))
        print('textwrap.shorten("Hello world", width=10, placeholder="..."):',
              textwrap.shorten("Hello world", width=10, placeholder="..."))
        print('''
        Optional keyword arguments correspond to the instance attributes of 
        TextWrapper, documented below. Note that the whitespace is collapsed 
        before the text is passed to the TextWrapper fill() function, so 
        changing the value of tabsize, expand_tabs, drop_whitespace, and 
        replace_whitespace will have no effect.

        New in version 3.4.
        ''')
        
    def textwrap_dedent_test(self):
        """
        Remove any common leading whitespace from every line in text.

        This can be used to make triple-quoted strings line up with the left 
        edge of the display, while still presenting them in the source code in 
        indented form.
        
        Note that tabs and spaces are both treated as whitespace, but they are 
        not equal: the lines "  hello" and "\\thello" are considered to have no
        common leading whitespace.
        
        Lines containing only whitespace are ignored in the input and 
        normalized to a single newline character in the output.
        """
        s = '''\
        hello
          world
        '''
        print('repr(s):',repr(s))          # prints '    hello\n      world\n    '
        print('repr(textwrap.dedent(s)):', repr(textwrap.dedent(s)))  # prints 'hello\n  world\n'
        return
    
    def textwrap_indent_test(self):
        """
        Add prefix to the beginning of selected lines in text.
        
        Lines are separated by calling text.splitlines(True).
        
        By default, prefix is added to all lines that do not consist solely of 
        whitespace (including any line endings).
        """
        string = 'hello\n\n \nworld'
        print('string =', string, sep='\n')
        print("textwrap.indent(string, '  '):", textwrap.indent(string, '  '), 
              sep='\n')
        
        print('''
        The optional predicate argument can be used to control which lines are 
        indented. For example, it is easy to add prefix to even empty and 
        whitespace-only lines:
        New in version 3.3.
        ''')
        print("textwrap.indent(string, '+ ', lambda line: True):",
              textwrap.indent(string, '+ ', lambda line: True), sep='\n')
        return
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    tw = TextWrap()
    print(tw.__doc__)
    
#    print('\n# textwrap.wrap(text, width=70, **kwargs)')
#    print(tw.textwrap_wrap_test.__doc__)
#    tw.textwrap_wrap_test()

#    print('\n# textwrap.fill(text, width=70, **kwargs)')
#    print(tw.textwrap_fill_test.__doc__)
#    tw.textwrap_fill_test()
    
#    print('\n# textwrap.shorten(text, width, **kwargs)')
#    print(tw.textwrap_shorten_test.__doc__)
#    tw.textwrap_shorten_test()
    
#    print('\n# textwrap.dedent(text)')
#    print(tw.textwrap_dedent_test.__doc__)
#    tw.textwrap_dedent_test()
    
    print('\n# textwrap.indent(text, prefix, predicate=None)')
    print(tw.textwrap_indent_test.__doc__)
    tw.textwrap_indent_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    