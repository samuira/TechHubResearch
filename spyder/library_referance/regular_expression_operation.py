# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 14:31:24 2019

@author: Rajesh Samui
"""

import re
import string
import random
import collections

class RegularExpressionOperation:
    """
    Regular expressions use the backslash character ('\') to indicate special 
    forms or to allow special characters to be used without invoking their 
    special meaning. This collides with Python’s usage of the same character 
    for the same purpose in string literals; for example, to match a literal 
    backslash, one might have to write '\\\\' as the pattern string, because 
    the regular expression must be \\, and each backslash must be expressed as 
    \\ inside a regular Python string literal.
    """
    def __init__(self):
        pass
    
    def regular_expression_syntax_test(self):
        """
        Regular expressions can be concatenated to form new regular 
        expressions; if A and B are both regular expressions, then AB is also 
        a regular expression. In general, if a string p matches A and another 
        string q matches B, the string pq will match AB. This holds unless A 
        or B contain low precedence operations; boundary conditions between A 
        and B; or have numbered group references. Thus, complex expressions can
        easily be constructed from simpler primitive expressions like the ones 
        described here. For details of the theory and implementation of regular
        expressions, consult the Friedl book [Frie09], or almost any textbook 
        about compiler construction.
        Regular expressions can contain both special and ordinary characters. 
        Most ordinary characters, like 'A', 'a', or '0', are the simplest 
        regular expressions; they simply match themselves. You can concatenate 
        ordinary characters, so last matches the string 'last'. (In the rest of
        this section, we’ll write RE’s in this special style, usually without 
        quotes, and strings to be matched 'in single quotes'.)
        Some characters, like '|' or '(', are special. Special characters 
        either stand for classes of ordinary characters, or affect how the 
        regular expressions around them are interpreted.
        Repetition qualifiers (*, +, ?, {m,n}, etc) cannot be directly nested. 
        This avoids ambiguity with the non-greedy modifier suffix ?, and with 
        other modifiers in other implementations. To apply a second repetition 
        to an inner repetition, parentheses may be used. For example, the 
        expression (?:a{6})* matches any multiple of six 'a' characters.
        """
        print('The special characters are:')
        print('\n# .')
        """
        (Dot.) In the default mode, this matches any character except a 
        newline. If the DOTALL flag has been specified, this matches any 
        character including a newline.
        """
        
        print('\n# ^')
        """
        (Caret.) Matches the start of the string, and in MULTILINE mode also 
        matches immediately after each newline.
        """
        
        print('\n# $')
        """
        Matches the end of the string or just before the newline at the end of 
        the string, and in MULTILINE mode also matches before a newline. foo 
        matches both ‘foo’ and ‘foobar’, while the regular expression foo$ 
        matches only ‘foo’. More interestingly, searching for foo.$ in 
        'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; 
        searching for a single $ in 'foo\n' will find two (empty) matches: 
            one just before the newline, and one at the end of the string.
        """
        
        print('\n# *')
        """
        Causes the resulting RE to match 0 or more repetitions of the 
        preceding RE, as many repetitions as are possible. ab* will match 
        ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
        """
        
        print('\n# +')
        """
        Causes the resulting RE to match 1 or more repetitions of the 
        preceding RE. ab+ will match ‘a’ followed by any non-zero number of 
        ‘b’s; it will not match just ‘a’.
        """
        
        print('\n# ?')
        """
        Causes the resulting RE to match 0 or 1 repetitions of the preceding 
        RE. ab? will match either ‘a’ or ‘ab’.
        """
        
        print('\n# *?, +?, ??')
        """
        The '*', '+', and '?' qualifiers are all greedy; they match as much 
        text as possible. Sometimes this behaviour isn’t desired; if the RE 
        <.*> is matched against '<a> b <c>', it will match the entire string, 
        and not just '<a>'. Adding ? after the qualifier makes it perform the 
        match in non-greedy or minimal fashion; as few characters as possible 
        will be matched. Using the RE <.*?> will match only '<a>'.
        """
        
        print('\n# {m}')
        """
        Specifies that exactly m copies of the previous RE should be matched; 
        fewer matches cause the entire RE not to match. For example, a{6} will 
        match exactly six 'a' characters, but not five.
        """
        
        print('\n# {m,n}')
        """
        Causes the resulting RE to match from m to n repetitions of the 
        preceding RE, attempting to match as many repetitions as possible. 
        For example, a{3,5} will match from 3 to 5 'a' characters. Omitting m 
        specifies a lower bound of zero, and omitting n specifies an infinite 
        upper bound. As an example, a{4,}b will match 'aaaab' or a thousand 'a'
        characters followed by a 'b', but not 'aaab'. The comma may not be 
        omitted or the modifier would be confused with the previously 
        described form.
        """
        
        print('\n# {m,n}?')
        """
        Causes the resulting RE to match from m to n repetitions of the 
        preceding RE, attempting to match as few repetitions as possible. This 
        is the non-greedy version of the previous qualifier. For example, on 
        the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, 
        while a{3,5}? will only match 3 characters.
        """
        
        print('\n# \\')
        """
        Either escapes special characters (permitting you to match characters 
        like '*', '?', and so forth), or signals a special sequence; special 
        sequences are discussed below.
        If you’re not using a raw string to express the pattern, remember that 
        Python also uses the backslash as an escape sequence in string 
        literals; if the escape sequence isn’t recognized by Python’s parser, 
        the backslash and subsequent character are included in the resulting 
        string. However, if Python would recognize the resulting sequence, the 
        backslash should be repeated twice. This is complicated and hard to 
        understand, so it’s highly recommended that you use raw strings for all
        but the simplest expressions.
        """
        
        print('\n# []')
        """
        Used to indicate a set of characters. In a set:
        Characters can be listed individually, e.g. [amk] will match 'a', 'm', 
        or 'k'.
        Ranges of characters can be indicated by giving two characters and 
        separating them by a '-', for example [a-z] will match any lowercase 
        ASCII letter, [0-5][0-9] will match all the two-digits numbers from 00 
        to 59, and [0-9A-Fa-f] will match any hexadecimal digit. If - is 
        escaped (e.g. [a\-z]) or if it’s placed as the first or last character 
        (e.g. [-a] or [a-]), it will match a literal '-'.
        Special characters lose their special meaning inside sets. For example,
        [(+*)] will match any of the literal characters '(', '+', '*', or ')'.    
        Character classes such as \w or \S (defined below) are also accepted 
        inside a set, although the characters they match depends on whether 
        ASCII or LOCALE mode is in force.
        Characters that are not within a range can be matched by complementing 
        the set. If the first character of the set is '^', all the characters 
        that are not in the set will be matched. For example, [^5] will match 
        any character except '5', and [^^] will match any character except '^'.
        ^ has no special meaning if it’s not the first character in the set.
        To match a literal ']' inside a set, precede it with a backslash, or 
        place it at the beginning of the set. For example, both [()[\]{}] and 
        []()[{}] will both match a parenthesis.   
        Support of nested sets and set operations as in Unicode Technical 
        Standard #18 might be added in the future. This would change the 
        syntax, so to facilitate this change a FutureWarning will be raised in 
        ambiguous cases for the time being. That includes sets starting with a 
        literal '[' or containing literal character sequences '--', '&&', '~~',
        and '||'. To avoid a warning escape them with a backslash.
        """
        
        print('\n# |')
        """
        A|B, where A and B can be arbitrary REs, creates a regular expression 
        that will match either A or B. An arbitrary number of REs can be 
        separated by the '|' in this way. This can be used inside groups (see 
        below) as well. As the target string is scanned, REs separated by '|' 
        are tried from left to right. When one pattern completely matches, 
        that branch is accepted. This means that once A matches, B will not be 
        tested further, even if it would produce a longer overall match. In 
        other words, the '|' operator is never greedy. To match a literal '|', 
        use \|, or enclose it inside a character class, as in [|].
        """
        
        print('\n# (...)')
        """
        Matches whatever regular expression is inside the parentheses, and 
        indicates the start and end of a group; the contents of a group can be 
        retrieved after a match has been performed, and can be matched later 
        in the string with the \number special sequence, described below. To 
        match the literals '(' or ')', use \( or \), or enclose them inside a 
        character class: [(], [)].
        """
        
        print('\n# (?...)')
        """
        This is an extension notation (a '?' following a '(' is not meaningful 
        otherwise). The first character after the '?' determines what the 
        meaning and further syntax of the construct is. Extensions usually do 
        not create a new group; (?P<name>...) is the only exception to this 
        rule. Following are the currently supported extensions.
        """
        
        print('\n# (?aiLmsux)')
        """
        (One or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x'.) 
        The group matches the empty string; the letters set the corresponding 
        flags: re.A (ASCII-only matching), re.I (ignore case), re.L (locale 
        dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode 
        matching), and re.X (verbose), for the entire regular expression. (The 
        flags are described in Module Contents.) This is useful if you wish to 
        include the flags as part of the regular expression, instead of passing
        a flag argument to the re.compile() function. Flags should be used 
        first in the expression string.
        """
        
        print('\n# (?:...)')
        """
        A non-capturing version of regular parentheses. Matches whatever 
        regular expression is inside the parentheses, but the substring 
        matched by the group cannot be retrieved after performing a match or 
        referenced later in the pattern.
        """
        
        print('\n# (?aiLmsux-imsx:...)')
        """
        (Zero or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x', 
        optionally followed by '-' followed by one or more letters from the 'i'
        , 'm', 's', 'x'.) The letters set or remove the corresponding flags: 
            re.A (ASCII-only matching), re.I (ignore case), re.L (locale 
            dependent), re.M (multi-line), re.S (dot matches all), re.U 
            (Unicode matching), and re.X (verbose), for the part of the 
            expression. (The flags are described in Module Contents.)
        The letters 'a', 'L' and 'u' are mutually exclusive when used as 
        inline flags, so they can’t be combined or follow '-'. Instead, when 
        one of them appears in an inline group, it overrides the matching mode 
        in the enclosing group. In Unicode patterns (?a:...) switches to 
        ASCII-only matching, and (?u:...) switches to Unicode matching 
        (default). In byte pattern (?L:...) switches to locale depending 
        matching, and (?a:...) switches to ASCII-only matching (default). This 
        override is only in effect for the narrow inline group, and the 
        original matching mode is restored outside of the group.
        New in version 3.6.
        Changed in version 3.7: The letters 'a', 'L' and 'u' also can be used 
        in a group.
        """
        
        print('\n# (?P<name>...)')
        """
        Similar to regular parentheses, but the substring matched by the group 
        is accessible via the symbolic group name name. Group names must be 
        valid Python identifiers, and each group name must be defined only 
        once within a regular expression. A symbolic group is also a numbered 
        group, just as if the group were not named.
        Named groups can be referenced in three contexts. If the pattern is 
        (?P<quote>['"]).*?(?P=quote) (i.e. matching a string quoted with either
        single or double quotes):
            
        Context of reference to group “quote” 	           Ways to reference it
        
        in the same pattern itself                           -> (?P=quote) (as shown)
                                                             -> \1
        when processing match object m                       -> m.group('quote')
                                                             -> m.end('quote') (etc.)
        in a string passed to the repl argument of re.sub()  -> \g<quote>
                                                             -> \g<1>
                                                             -> \1
        """
        
        print('\n# (?P=name)')
        '''
        A backreference to a named group; it matches whatever text was matched 
        by the earlier group named name.
        '''
        
        print('\n# (?#...)')
        '''
        A comment; the contents of the parentheses are simply ignored.
        '''
        
        print('\n# (?=...)')
        '''
        Matches if ... matches next, but doesn’t consume any of the string. 
        This is called a lookahead assertion. For example, Isaac (?=Asimov) 
        will match 'Isaac ' only if it’s followed by 'Asimov'.
        '''
        
        print('\n# (?!...)')
        '''
        Matches if ... doesn’t match next. This is a negative lookahead 
        assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if 
        it’s not followed by 'Asimov'.
        '''
        
        print('\n# (?<=...)')
        '''
        Matches if the current position in the string is preceded by a match 
        for ... that ends at the current position. This is called a positive 
        lookbehind assertion. (?<=abc)def will find a match in 'abcdef', since 
        the lookbehind will back up 3 characters and check if the contained 
        pattern matches. The contained pattern must only match strings of some 
        fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} 
        are not. Note that patterns which start with positive lookbehind 
        assertions will not match at the beginning of the string being 
        searched; you will most likely want to use the search() function rather
        than the match() function:
        '''
        m = re.search('(?<=abc)def', 'abcdef')
        print('m.group(0):',m.group(0))
        
        m = re.search(r'(?<=-)\w+', 'spam-egg')
        print('m.group(0):',m.group(0))
        
        print('\n# (?<!...)')
        '''
        Matches if the current position in the string is not preceded by a 
        match for .... This is called a negative lookbehind assertion. Similar 
        to positive lookbehind assertions, the contained pattern must only 
        match strings of some fixed length. Patterns which start with negative 
        lookbehind assertions may match at the beginning of the string being 
        searched.
        '''
        
        print('\n# (?(id/name)yes-pattern|no-pattern)')
        '''
        Will try to match with yes-pattern if the group with given id or name 
        exists, and with no-pattern if it doesn’t. no-pattern is optional and 
        can be omitted. For example, (<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$) is a poor
        email matching pattern, which will match with '<user@host.com>' as well
        as 'user@host.com', but not with '<user@host.com' nor 'user@host.com>'.
        '''
        
        print('\n# \\number')
        '''
        Matches the contents of the group of the same number. Groups are 
        numbered starting from 1. For example, (.+) \1 matches 'the the' or 
        '55 55', but not 'thethe' (note the space after the group). This 
        special sequence can only be used to match one of the first 99 groups. 
        If the first digit of number is 0, or number is 3 octal digits long, it
        will not be interpreted as a group match, but as the character with 
        octal value number. Inside the '[' and ']' of a character class, all 
        numeric escapes are treated as characters.
        '''
        
        print('\n# \\A')
        '''
        Matches only at the start of the string.
        '''
        
        print('\n# \\b')
        '''
        Matches the empty string, but only at the beginning or end of a word. A
        word is defined as a sequence of word characters. Note that formally, 
        \b is defined as the boundary between a \w and a \W character (or vice 
        versa), or between \w and the beginning/end of the string. This means 
        that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 
        'foobar' or 'foo3'.
        '''
        
        print('\n# \\B')
        '''
        Matches the empty string, but only when it is not at the beginning or 
        end of a word. This means that r'py\B' matches 'python', 'py3', 'py2', 
        but not 'py', 'py.', or 'py!'. \B is just the opposite of \b, so word 
        characters in Unicode patterns are Unicode alphanumerics or the 
        underscore, although this can be changed by using the ASCII flag. Word 
        boundaries are determined by the current locale if the LOCALE flag is 
        used.
        '''
        
        print('\n# \\d')
        '''
        For Unicode (str) patterns:
            Matches any Unicode decimal digit (that is, any character in 
            Unicode character category [Nd]). This includes [0-9], and also 
            many other digit characters. If the ASCII flag is used only [0-9] 
            is matched.
        For 8-bit (bytes) patterns:
            Matches any decimal digit; this is equivalent to [0-9].
        '''
        
        print('\n# \\D')
        '''
        Matches any character which is not a decimal digit. This is the 
        opposite of \d. If the ASCII flag is used this becomes the equivalent 
        of [^0-9].
        '''
        
        print('\n# \\s')
        ''' 
        For Unicode (str) patterns:
            Matches Unicode whitespace characters (which includes [ \t\n\r\f\v]
            , and also many other characters, for example the non-breaking 
            spaces mandated by typography rules in many languages). If the 
            ASCII flag is used, only [ \t\n\r\f\v] is matched.
        For 8-bit (bytes) patterns:
            Matches characters considered whitespace in the ASCII character set
            ; this is equivalent to [ \t\n\r\f\v].
        '''
        
        print('\n# \\S')
        '''
        Matches any character which is not a whitespace character. This is the 
        opposite of \s. If the ASCII flag is used this becomes the equivalent 
        of [^ \t\n\r\f\v].
        '''
        
        print('\n# \\w')
        '''
        For Unicode (str) patterns:
            Matches Unicode word characters; this includes most characters that
            can be part of a word in any language, as well as numbers and the 
            underscore. If the ASCII flag is used, only [a-zA-Z0-9_] is 
            matched.
        For 8-bit (bytes) patterns:
            Matches characters considered alphanumeric in the ASCII character 
            set; this is equivalent to [a-zA-Z0-9_]. If the LOCALE flag is used
            , matches characters considered alphanumeric in the current locale 
            and the underscore.
        '''
        
        print('\n# \\W')
        '''
        Matches any character which is not a word character. This is the 
        opposite of \w. If the ASCII flag is used this becomes the equivalent 
        of [^a-zA-Z0-9_]. If the LOCALE flag is used, matches characters 
        considered alphanumeric in the current locale and the underscore.
        '''
        
        print('\n# \\Z')
        '''
        Matches only at the end of the string.
        '''
        return
        
    def module_content_test(self):
        """
        The module defines several functions, constants, and an exception. Some
        of the functions are simplified versions of the full featured methods 
        for compiled regular expressions. Most non-trivial applications always 
        use the compiled form.
        Changed in version 3.6: Flag constants are now instances of RegexFlag, 
        which is a subclass of enum.IntFlag.
        """
        print('\n# re.compile(pattern, flags=0)')
        '''
        Compile a regular expression pattern into a regular expression object, 
        which can be used for matching using its match(), search() and other 
        methods, described below.
        The expression’s behaviour can be modified by specifying a flags value.
        Values can be any of the following variables, combined using bitwise OR
        (the | operator).
        
        The sequence
        prog = re.compile(pattern)
        result = prog.match(string)
        is equivalent to
        result = re.match(pattern, string)
    
        but using re.compile() and saving the resulting regular expression 
        object for reuse is more efficient when the expression will be used 
        several times in a single program.
    
        Note:
            The compiled versions of the most recent patterns passed to 
            re.compile() and the module-level matching functions are cached, 
            so programs that use only a few regular expressions at a time 
            needn’t worry about compiling regular expressions.
        '''
        phone_check = re.compile(r"\+[0-9]+\-[0-9]+")
        print('phone_check =',phone_check)
        phone = '+91-9647521448 +91-745634536'
        print('phone =',phone)
        print('phone_check.search(phone):', phone_check.search(phone))
        print('phone_check.match(phone):', phone_check.match(phone))
        print('phone_check.findall(phone):', phone_check.findall(phone))
        
        print('\n# re.A\n# re.ASCII')
        '''
        Make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only matching 
        instead of full Unicode matching. This is only meaningful for Unicode 
        patterns, and is ignored for byte patterns. Corresponds to the inline 
        flag (?a).
        Note that for backward compatibility, the re.U flag still exists (as 
        well as its synonym re.UNICODE and its embedded counterpart (?u)), but 
        these are redundant in Python 3 since matches are Unicode by default 
        for strings (and Unicode matching isn’t allowed for bytes).
        '''
        phone_check = re.compile(r"\+[0-9]+\-[0-9]+", re.ASCII)
        phone = '+91-9647521448 +91-745634536'
        print('phone_check.search(phone):', phone_check.search(phone))
        print('phone_check.match(phone):', phone_check.match(phone))
        print('phone_check.findall(phone):', phone_check.findall(phone))
        
        print('\n# re.DEBUG')
        '''
        Display debug information about compiled expression. No corresponding 
        inline flag.
        '''
        re.compile('.*', re.DEBUG)
        re.compile("a+b*\s\w?", 0x80)
        print('\nre.DEBUG = 0x80\n')
        re.compile("a+b*\s\w?", re.DEBUG)
        
        print('\n# re.I\n# re.IGNORECASE')
        '''
        Perform case-insensitive matching; expressions like [A-Z] will also 
        match lowercase letters. Full Unicode matching (such as Ü matching ü) 
        also works unless the re.ASCII flag is used to disable non-ASCII 
        matches. The current locale does not change the effect of this flag 
        unless the re.LOCALE flag is also used. Corresponds to the inline flag 
        (?i).
        Note that when the Unicode patterns [a-z] or [A-Z] are used in 
        combination with the IGNORECASE flag, they will match the 52 ASCII 
        letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital 
        letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless i), 
        ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign). 
        If the ASCII flag is used, only letters ‘a’ to ‘z’ and ‘A’ to ‘Z’ are 
        matched.
        '''
        print(re.search('test', 'TeSt', re.IGNORECASE))
        print(re.match('test', 'TeSt', re.IGNORECASE))
        print(re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE))
        
        print('\n#  re.L\n# re.LOCALE')
        '''
        Make \w, \W, \b, \B and case-insensitive matching dependent on the 
        current locale. This flag can be used only with bytes patterns. The use
        of this flag is discouraged as the locale mechanism is very unreliable,
        it only handles one “culture” at a time, and it only works with 8-bit 
        locales. Unicode matching is already enabled by default in Python 3 for
        Unicode (str) patterns, and it is able to handle different 
        locales/languages. Corresponds to the inline flag (?L).
        Changed in version 3.6: re.LOCALE can be used only with bytes patterns 
        and is not compatible with re.ASCII.
        Changed in version 3.7: Compiled regular expression objects with the 
        re.LOCALE flag no longer depend on the locale at compile time. Only the
        locale at matching time affects the result of matching.
        '''
        print('Have not found any example of the usage of re.LOCALE')
        
        print('\n# re.M\n# re.MULTILINE')
        '''
        When specified, the pattern character '^' matches at the beginning of 
        the string and at the beginning of each line (immediately following 
        each newline); and the pattern character '$' matches at the end of the 
        string and at the end of each line (immediately preceding each newline). 
        By default, '^' matches only at the beginning of the string, and '$' 
        only at the end of the string and immediately before the newline (if 
        any) at the end of the string. Corresponds to the inline flag (?m).
        '''
        xx = "guru99\ncareerguru99\nselenium"
        k1 = re.findall(r"^\w", xx)
        k2 = re.findall(r"^\w", xx, re.MULTILINE)
        print(k1)
        print(k2)
        
        print('\n# re.S\n# re.DOTALL')
        '''
        Make the '.' special character match any character at all, including a 
        newline; without this flag, '.' will match anything except a newline. 
        Corresponds to the inline flag (?s).
        '''
        print(re.findall(r'.','I am\nR'))
        print(re.findall(r'.','I am\nR',re.S))
        
        print('\n# re.X\n# re.VERBOSE')
        '''
        This flag allows you to write regular expressions that look nicer and 
        are more readable by allowing you to visually separate logical sections
        of the pattern and add comments. Whitespace within the pattern is 
        ignored, except when in a character class, or when preceded by an 
        unescaped backslash, or within tokens like *?, (?: or (?P<...>. When a 
        line contains a # that is not in a character class and is not preceded 
        by an unescaped backslash, all characters from the leftmost such # 
        through the end of the line are ignored.
        Corresponds to the inline flag (?x).
        This means that the two following regular expression objects that match
        a decimal number are functionally equal:
        '''
        a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
        b = re.compile(r"\d+\.\d*")
        print(re.findall(a,'3.44 555 54. .54'))
        print(re.findall(b,'3.44 555 54. .54'))        
        return
    
    def re_search_test(self):
        """
        Scan through string looking for the first location where the regular 
        expression pattern produces a match, and return a corresponding match 
        object. Return None if no position in the string matches the pattern; 
        note that this is different from finding a zero-length match at some 
        point in the string.
        """
        string = "Python is fun Python"
        
        # check if 'Python' is at the beginning
        match = re.search('\APython', string)
        print(match)
        if match:
            print("pattern found inside the string")
        else:
            print("pattern not found") 
        return
    
    def re_match_test(self):
        """
        If zero or more characters at the beginning of string match the regular
        expression pattern, return a corresponding match object. Return None if
        the string does not match the pattern; note that this is different from
        a zero-length match.
        Note that even in MULTILINE mode, re.match() will only match at the 
        beginning of the string and not at the beginning of each line.
        If you want to locate a match anywhere in string, use search() instead 
        (see also search() vs. match()).
        """
        pattern = '^a...s$'
        test_string = 'abyss'
        result_m = re.match(pattern, test_string)
        result_s = re.search(pattern, test_string)
        print(result_m)
        print(result_s)
        if result_m:
            print("Search successful.")
        else:
            print("Search unsuccessful.")
            
        # re.match vs re.search
        print(re.match("c", "abcdef"))      # No match
        print(re.search("c", "abcdef"))     # Match
        
        print(re.match("c", "abcdef"))      # No match
        print(re.search("^c", "abcdef"))    # No match
        print(re.search("^a", "abcdef"))    # Match
        
        print(re.match('X', 'A\nB\nX', re.MULTILINE))       # No match
        print(re.search('^X', 'A\nB\nX', re.MULTILINE))     # Match
        return
    
    def re_fullmatch_test(self):
        """
        If the whole string matches the regular expression pattern, return a 
        corresponding match object. Return None if the string does not match 
        the pattern; note that this is different from a zero-length match.

        New in version 3.4.
        """
        print(re.search(r'^a|ab$', 'ab'))
        print(re.match(r'^a|ab$', 'ab'))
        print(re.fullmatch(r'a|ab', 'ab'))
        
        
        text = 'This is some text -- with punctuation.'
        pattern = 'is'
        
        print('Text       :', text)
        print('Pattern    :', pattern)
        
        m = re.search(pattern, text)
        print('Search     :', m)
        m = re.match(pattern, text)
        print('match      :', m)
        s = re.fullmatch(pattern, text)
        print('Full match :', s)
        
    def re_split_test(self):
        """
        Split string by the occurrences of pattern. If capturing parentheses 
        are used in pattern, then the text of all groups in the pattern are 
        also returned as part of the resulting list. If maxsplit is nonzero, at
        most maxsplit splits occur, and the remainder of the string is returned
        as the final element of the list.
        """
        print("re.split(r'\W+', 'Words, words, words.'):",
              re.split(r'\W+', 'Words, words, words.'))
        print("re.split(r'(\W+)', 'Words, words, words.'):",
              re.split(r'(\W+)', 'Words, words, words.'))
        print("re.split(r'\W+', 'Words, words, words.', 1):",
              re.split(r'\W+', 'Words, words, words.', 1))
        print("re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE):",
              re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
        print()
        
        # If there are capturing groups in the separator and it matches at the 
        # start of the string, the result will start with an empty string. The 
        # same holds for the end of the string:
        
        print("re.split(r'(\W+)', '...words, words...'):",
              re.split(r'(\W+)', '...words, words...'))
        # That way, separator components are always found at the same relative 
        # indices within the result list.
        print()
        # Empty matches for the pattern split the string only when not adjacent
        # to a previous empty match.
        print("re.split(r'\W', 'Words, words, words.'):",
              re.split(r'\W', 'Words, words, words.'))
        print("re.split(r'\W*', '...words...'):",
              re.split(r'\W*', '...words...'))
        print("re.split(r'(\W*)', '...words...'):",
              re.split(r'(\W*)', '...words...'))
        return
    
    def re_findall_test(self):
        """
        Return all non-overlapping matches of pattern in string, as a list of 
        strings. The string is scanned left-to-right, and matches are returned 
        in the order found. If one or more groups are present in the pattern, 
        return a list of groups; this will be a list of tuples if the pattern 
        has more than one group. Empty matches are included in the result.
        Changed in version 3.7: Non-empty matches can now start just after a 
        previous empty match.
        """
        ## Suppose we have a text with many email addresses
        s = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
        print(s)
        ## Here re.findall() returns a list of all the found email strings
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', s) ## ['alice@google.com', 'bob@abc.com']
        print(emails)
        tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', s)
        print(tuples)
        return
    
    def re_finditer_test(self):
        """
        Return an iterator yielding match objects over all non-overlapping 
        matches for the RE pattern in string. The string is scanned 
        left-to-right, and matches are returned in the order found. Empty 
        matches are included in the result.
        Changed in version 3.7: Non-empty matches can now start just after a 
        previous empty match.
        You can use re.finditer to iterate over all matches in a string. This 
        gives you (in comparison to re.findall extra information, such as 
        information about the match location in the string (indexes):
        """
        text = 'You can try to find an ant in this string'
        pattern = 'an?\w'   # find 'an' either with or without a following word 
                            # character
        result = re.finditer(pattern, text)
        print(result)
        for match in result:
            # Start index of match (integer)
            sStart = match.start()
            # Final index of match (integer)
            sEnd = match.end()
            # Complete match (string)
            sGroup = match.group()
            # Print match
            print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))
    
    def re_sub_test(self):
        """
        Return the string obtained by replacing the leftmost non-overlapping 
        occurrences of pattern in string by the replacement repl. If the 
        pattern isn’t found, string is returned unchanged. repl can be a 
        string or a function; if it is a string, any backslash escapes in it 
        are processed. That is, \\n is converted to a single newline character, 
        \\r is converted to a carriage return, and so forth. Unknown escapes of 
        ASCII letters are reserved for future use and treated as errors. Other 
        unknown escapes such as \& are left alone. Backreferences, such as \\6, 
        are replaced with the substring matched by group 6 in the pattern.
        """
        result = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
               r'static PyObject*\npy_\1(void)\n{','def myfunc():')
        print(result)
        
        print("""
        If repl is a function, it is called for every non-overlapping 
        occurrence of pattern. The function takes a single match object 
        argument, and returns the replacement string. 
        """)
        def dashrepl(matchobj):
            if matchobj.group(0) == '-': return ' '
            else: return '-'
            
        print("re.sub('-{1,2}', dashrepl, 'pro----gram-files'):",
                      re.sub('-{1,2}', dashrepl, 'pro----gram-files'))
        print("re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE):",
              re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
    
        print("""
        The pattern may be a string or a pattern object.
        
        The optional argument count is the maximum number of pattern 
        occurrences to be replaced; count must be a non-negative integer. If 
        omitted or zero, all occurrences will be replaced. Empty matches for 
        the pattern are replaced only when not adjacent to a previous empty 
        match, so sub('x*', '-', 'abxd') returns '-a-b--d-'.
        
        In string-type repl arguments, in addition to the character escapes and
        backreferences described above, \g<name> will use the substring matched
        by the group named name, as defined by the (?P<name>...) syntax. 
        \g<number> uses the corresponding group number; \g<2> is therefore 
        equivalent to \2, but isn’t ambiguous in a replacement such as \g<2>0. 
        \20 would be interpreted as a reference to group 20, not a reference to
        group 2 followed by the literal character '0'. The backreference \g<0> 
        substitutes in the entire substring matched by the RE.
        
        Changed in version 3.1: Added the optional flags argument.
        
        Changed in version 3.5: Unmatched groups are replaced with an empty 
        string.
        
        Changed in version 3.6: Unknown escapes in pattern consisting of '\' 
        and an ASCII letter now are errors.
        
        Changed in version 3.7: Unknown escapes in repl consisting of '\' and 
        an ASCII letter now are errors.
        
        Changed in version 3.7: Empty matches for the pattern are replaced when
        adjacent to a previous non-empty match.
        """)
        print("re.sub('x*', '-', 'abxd'):", re.sub('x*', '-', 'abxd'))
        return
    
    def re_subn_test(self):
        """
        Perform the same operation as sub(), but return a tuple (new_string, 
        number_of_subs_made).

        Changed in version 3.1: Added the optional flags argument.
        Changed in version 3.5: Unmatched groups are replaced with an empty 
        string.
        """
        print("re.subn('x*', '-', 'abxd'):", re.subn('x*', '-', 'abxd'))
        result = re.subn(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
               r'static PyObject*\npy_\1(void)\n{','def myfunc():')
        print(result)
        def dashrepl(matchobj):
            if matchobj.group(0) == '-': return ' '
            else: return '-'
            
        print("re.subn('-{1,2}', dashrepl, 'pro----gram-files'):",
                      re.subn('-{1,2}', dashrepl, 'pro----gram-files'))
        print("re.subn(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE):",
              re.subn(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
        return
    
    def re_escape_test(self):
        """
        Escape special characters in pattern. This is useful if you want to 
        match an arbitrary literal string that may have regular expression 
        metacharacters in it. 
        """
        print("re.escape('python.exe'):", re.escape('python.exe'))
        legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
        print(re.escape(legal_chars))
        print('[%s]+' % re.escape(legal_chars))
        operators = ['+', '-', '*', '/', '**']
        print('\n'.join(map(re.escape, sorted(operators, reverse=True))))
        
        print("""
        This functions must not be used for the replacement string in sub() and
        subn(), only backslashes should be escaped.
        """)
        digits_re = r'\d+'
        sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
        print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
        print("""
        Changed in version 3.3: The '_' character is no longer escaped.
        Changed in version 3.7: Only characters that can have special meaning 
        in a regular expression are escaped.
        """)
        return
    
    def re_purge_test(self):
        """
        Clear the regular expression cache.
        Most code will not need to worry about purging the re module cache. 
        It brings very little memory benefit, and can actually hurt performance
        if you purged it.
        
        The cache is used to store compiled regular expression objects when you
        use the top-level re.* functions directly rather than use 
        re.compile(pattern). For example, if you used 
        re.search(r'<some pattern>', string_value) in a loop, then the re 
        module would compile '<some pattern>' only once and store it in the 
        cache, avoiding having to re-compile the pattern each time.
        
        How many such objects are cached and how the cache is managed is an 
        implementation detail, really, but regular expression objects are 
        light-weight objects, taking up at most a few hundred bytes, and Python
        won't store more than a few hundred of these (Python 3.7 stores up to 
        512).
        
        The cache is also automatically managed, so purging is not normally 
        needed at all. Use it if you specifically need to account for regular 
        expression compilation time in a repeated time trial test involving 
        re.* functions, or are testing the caching functionality itself. The 
        only locations in the Python standard library that call re.purge() are 
        in tests (specifically in the test_re unittests for the re module and 
        the reference leak test in the regression test suite).
        
        If your code is creating a lot of regular expression objects that you 
        intent to keep using, it is better to use re.compile() and keep your 
        own references to those compiled expression objects.
        """
        pass
    
    def exception_re_error_test(self):
        """
        Exception raised when a string passed to one of the functions here is 
        not a valid regular expression (for example, it might contain unmatched
        parentheses) or when some other error occurs during compilation or 
        matching. It is never an error if a string contains no match for a 
        pattern. The error instance has the following additional attributes:

        msg:
            The unformatted error message.
    
        pattern:
            The regular expression pattern.
    
        pos:
            The index in pattern where compilation failed (may be None).
    
        lineno:
            The line corresponding to pos (may be None).

        colno:
            The column corresponding to pos (may be None).
    
        Changed in version 3.5: Added additional attributes.
        """
        pass
    
    def pattern_search_test(self):
        """
        Scan through string looking for the first location where this regular 
        expression produces a match, and return a corresponding match object. 
        Return None if no position in the string matches the pattern; note that
        this is different from finding a zero-length match at some point in the
        string.

        The optional second parameter pos gives an index in the string where 
        the search is to start; it defaults to 0. This is not completely 
        equivalent to slicing the string; the '^' pattern character matches at 
        the real beginning of the string and at positions just after a newline,
        but not necessarily at the index where the search is to start.
        
        The optional parameter endpos limits how far the string will be 
        searched; it will be as if the string is endpos characters long, so 
        only the characters from pos to endpos - 1 will be searched for a 
        match. If endpos is less than pos, no match will be found; otherwise, 
        if rx is a compiled regular expression object, rx.search(string, 0, 50)
        is equivalent to rx.search(string[:50], 0).
        """
        pattern = re.compile("d")
        print("pattern =",pattern)
        print('pattern.search("dog"):',pattern.search("dog")) # Match at index 0
        print('pattern.search("dog", 1):', pattern.search("dog", 1))  # No match; search doesn't include the "d"
        return
    
    def pattern_match_test(self):
        """
        If zero or more characters at the beginning of string match this 
        regular expression, return a corresponding match object. Return None if
        the string does not match the pattern; note that this is different from
        a zero-length match.

        The optional pos and endpos parameters have the same meaning as for the
        search() method.
        """
        pattern = re.compile("o")
        print('pattern =', pattern)
        print('pattern.match("dog"):', pattern.match("dog"))    # No match as "o" is not at the start of "dog".
        print('pattern.match("dog", 1):', pattern.match("dog", 1))     # Match as "o" is the 2nd character of "dog".
        
        print('''
        If you want to locate a match anywhere in string, use search() instead 
        (see also search() vs. match()).
        ''')
        return
    
    def pattern_fullmatch_test(self):
        """
        If the whole string matches this regular expression, return a 
        corresponding match object. Return None if the string does not match 
        the pattern; note that this is different from a zero-length match.

        The optional pos and endpos parameters have the same meaning as for the
        search() method.
        New in version 3.4.
        """
        pattern = re.compile("o[gh]")
        print('pattern =', pattern)
        print('pattern.fullmatch("dog"):', pattern.fullmatch("dog"))      # No match as "o" is not at the start of "dog".
        print('pattern.fullmatch("ogre"):', pattern.fullmatch("ogre"))     # No match as not the full string matches.
        print('pattern.fullmatch("doggie", 1, 3):', 
              pattern.fullmatch("doggie", 1, 3))   # Matches within given limits.
    
    def pattern_split_test(self):
        """
        Identical to the split() function, using the compiled pattern.
        """
        pattern = re.compile('\W+')
        print('pattern =', pattern)
        print("pattern.split('Words, words, words.'):",
              pattern.split('Words, words, words.'))
        return
    
    def pattern_findall_test(self):
        """
        Similar to the findall() function, using the compiled pattern, but also
        accepts optional pos and endpos parameters that limit the search region
        like for search().
        """
        ## Suppose we have a text with many email addresses
        s = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
        print('s =', s)
        pattern = re.compile('[\w\.-]+@[\w\.-]+')
        print('pattern =', pattern)
        ## Here re.findall() returns a list of all the found email strings
        print('pattern.findall(s):', pattern.findall(s)) ## ['alice@google.com', 'bob@abc.com']
        pattern = re.compile('([\w\.-]+)@([\w\.-]+)')
        print('pattern =', pattern)
        print('pattern.findall(s):', pattern.findall(s))
        return
    
    def pattern_finditer_test(self):
        """
        Similar to the finditer() function, using the compiled pattern, but 
        also accepts optional pos and endpos parameters that limit the search 
        region like for search().
        """
        text = 'You can try to find an ant in this string'
        print('text =', text)
        pattern = re.compile('an?\w')   # find 'an' either with or without a following word 
        print('pattern =', pattern)
        result = pattern.finditer(text)
        print('pattern.finditer(text):', result)
        for match in result:
            # Start index of match (integer)
            sStart = match.start()
            # Final index of match (integer)
            sEnd = match.end()
            # Complete match (string)
            sGroup = match.group()
            # Print match
            print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))
        return
    
    def pattern_sub_test(self):
        """
        Identical to the sub() function, using the compiled pattern.
        """
        pattern = re.compile('def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):')
        print('pattern =', pattern)
        result = pattern.sub(r'static PyObject*\npy_\1(void)\n{',
                             'def myfunc():')
        print('result:',result, sep='\n')
        return
    
    def pattern_subn_test(self):
        """
        Identical to the subn() function, using the compiled pattern.
        """
        pattern = re.compile('def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):')
        print('pattern =', pattern)
        result = pattern.subn(r'static PyObject*\npy_\1(void)\n{',
                             'def myfunc():')
        print('result:',result, sep='\n')
        return
    
    def pattern_extras_test(self):
        """
        Pattern.flags:
            The regex matching flags. This is a combination of the flags given 
            to compile(), any (?...) inline flags in the pattern, and implicit 
            flags such as UNICODE if the pattern is a Unicode string.
        """
        pattern = re.compile('(?P<name>[^\W\d_]+)|(?P<number>\d+)')
        print('pattern =', pattern)
        print('pattern.flags:', pattern.flags)
        
        print('''
        Pattern.groups:
            The number of capturing groups in the pattern.
        ''')
        print('pattern.groups',pattern.groups)
        
        print('''
        Pattern.groupindex:
            A dictionary mapping any symbolic group names defined by (?P<id>) 
            to group numbers. The dictionary is empty if no symbolic groups 
            were used in the pattern.
        ''')
        print('pattern.groupindex:', pattern.groupindex)
        '''
        Pattern.pattern:
            The pattern string from which the pattern object was compiled.
        '''
        print('pattern.pattern:', pattern.pattern)
        '''
        Changed in version 3.7: Added support of copy.copy() and 
        copy.deepcopy(). Compiled regular expression objects are considered 
        atomic.
        '''
        return
    
    def match_objects_test(self):
        """
        Match objects always have a boolean value of True. Since match() and 
        search() return None when there is no match, you can test whether there
        was a match with a simple if statement:
        """
        pattern = re.compile('(?P<name>[^\W\d_]+)|(?P<number>\d+)')
        string = 'Compiled regular expression objects are considered atomic.'
        print('pattern = '+str(pattern), 'string = '+string, sep='\n')
        match = re.search(pattern, string)
        if match:
            print('match = '+str(match))
            
        print('\n# Match.expand(template)')
        print('''
        Return the string obtained by doing backslash substitution on the 
        template string template, as done by the sub() method. Escapes such as 
        \\n are converted to the appropriate characters, and numeric 
        backreferences (\\1, \\2) and named backreferences (\g<1>, \g<name>) 
        are replaced by the contents of the corresponding group.
    
        Changed in version 3.5: Unmatched groups are replaced with an empty 
        string.
        ''')
        xx = re.compile(r"(\d\d\d\d)")
        print('xx =', xx)
        yy = xx.search("in the year 1999")
        print('yy:', yy)
        print('yy.expand(r"Year: \\1"):',yy.expand(r"Year: \1"))   # Year: 1999
        
        print('\n# Match.group([group1, ...])')
        print('''
        Returns one or more subgroups of the match. If there is a single 
        argument, the result is a single string; if there are multiple 
        arguments, the result is a tuple with one item per argument. Without 
        arguments, group1 defaults to zero (the whole match is returned). If a 
        groupN argument is zero, the corresponding return value is the entire 
        matching string; if it is in the inclusive range [1..99], it is the 
        string matching the corresponding parenthesized group. If a group 
        number is negative or larger than the number of groups defined in the 
        pattern, an IndexError exception is raised. If a group is contained in 
        a part of the pattern that did not match, the corresponding result is 
        None. If a group is contained in a part of the pattern that matched 
        multiple times, the last match is returned.
        ''')
        m = re.match(r"(\w+) (\w+), (\w+)", "Isaac Newton, physicist scientist")
        print('m =', m)
        print('m.group(0):', m.group(0))   # The entire match
        print('m.group(1):', m.group(1))   # The first parenthesized subgroup.
        print('m.group(2):', m.group(2))   # The second parenthesized subgroup.
        print('m.group(1, 2):', m.group(1, 2, 3))  # Multiple arguments give us a tuple.
        
        print('''
        If the regular expression uses the (?P<name>...) syntax, the groupN 
        arguments may also be strings identifying groups by their group name. 
        If a string argument is not used as a group name in the pattern, an 
        IndexError exception is raised.
        ''')
        pattern = re.compile("(?P<first_name>\w+) (?P<last_name>\w+)")
        print('pattern =', pattern)
        string = "Malcolm Reynolds"
        print('string =', string)
        match = pattern.match(string)
        print('match =', match)
        print("match.group('first_name'):", match.group('first_name'))
        print("match.group('last_name'):", match.group('last_name'))
        
        # Named groups can also be referred to by their index.
        print('match.group(1):', match.group(1))
        print('match.group(2):', match.group(2))
        
        # If a group matches multiple times, only the last match is accessible.
        pattern = re.compile("(..)+")
        print('pattern =', pattern)
        string = "a1b2c3"
        print('string =', string)
        match = pattern.match(string)  # Matches 3 times.
        print('match:', match)
        print('match.group(1):', match.group(1))
        
        print('\n# Match.__getitem__(g)')
        print('''
        This is identical to m.group(g). This allows easier access to an 
        individual group from a match.
        New in version 3.6.
        ''')
        pattern = re.compile("(\w+) (\w+)")
        print('pattern =', pattern)
        string = "Isaac Newton, physicist"
        print('string =', string)
        match = pattern.match(string)
        print('match:', match)
        # print('match[0]:', match[0])   # The entire match
        # print('match[1]:', match[1])   # The first parenthesized subgroup.
        # print('match[2]:', match[2])   # The second parenthesized subgroup.
        
        print('\n# Match.groups(default=None)')
        print('''
        Return a tuple containing all the subgroups of the match, from 1 up to 
        however many groups are in the pattern. The default argument is used 
        for groups that did not participate in the match; it defaults to None.
        ''')
        pattern = re.compile(r"(\d+)\.(\d+)")
        print('pattern =', pattern)
        string = "24.1632"
        print('string =', string)
        match = pattern.match(string)
        print('match:', match)
        print('match.groups():', match.groups())
        
        print('''
        If we make the decimal place and everything after it optional, not all 
        groups might participate in the match. These groups will default to 
        None unless the default argument is given.
        ''')
        pattern = re.compile(r"(\d+)\.?(\d+)?")
        print('pattern =', pattern)
        string = "24"
        print('string =', string)
        match = pattern.match(string)
        print('match:', match)
        print('match.groups():', match.groups()) # Second group defaults to None.
        print('match.groups("0"):', match.groups("0")) # Now, the second group defaults to '0'.
        
        print('\n# Match.groupdict(default=None)')
        print('''
        Return a dictionary containing all the named subgroups of the match, 
        keyed by the subgroup name. The default argument is used for groups 
        that did not participate in the match; it defaults to None.
        ''')
        pattern = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)")
        print('pattern =', pattern)
        string = "Malcolm Reynolds"
        print('string =', string)
        match = pattern.match(string)
        print('match:', match)
        print('match.groupdict():', match.groupdict())
        
        print('\n# Match.start([group])\n# Match.end([group])')
        print('''
        Return the indices of the start and end of the substring matched by 
        group; group defaults to zero (meaning the whole matched substring). 
        Return -1 if group exists but did not contribute to the match. For a 
        match object m, and a group g that did contribute to the match, the 
        substring matched by group g (equivalent to m.group(g)) is
        m.string[m.start(g):m.end(g)]
        
        Note that m.start(group) will equal m.end(group) if group matched a 
        null string. For example, after m = re.search('b(c?)', 'cba'), 
        m.start(0) is 1, m.end(0) is 2, m.start(1) and m.end(1) are both 2, 
        and m.start(2) raises an IndexError exception.
        An example that will remove remove_this from email addresses.
        ''')
        email = "tony@tiremove_thisger.net"
        print('email =', email)
        match = re.search("remove_this", email)
        print('match:', match)
        print('email[:match.start()] + email[match.end():]:',
              email[:match.start()] + email[match.end():])
        
        print('\n# Match.span([group])')
        print('''
        For a match m, return the 2-tuple (m.start(group), m.end(group)). Note 
        that if group did not contribute to the match, this is (-1, -1). group 
        defaults to zero, the entire match.
        ''')
        statement = r'new (car)|old (car)'
        print('statement =', statement)
        text = 'I bought a new car and got rid of the old car'
        print('text =', text)
        match = re.search(statement, text)
        print('match:', match)
        print('match.span():', match.span())
        for index, match in enumerate(re.finditer(statement, text)):
            print(index,'match.span():', match.span())
            
        # 1 is referring to the first group, the default is zero - which means 
        # the whole match.
        for index, match in enumerate(re.finditer(statement, text)):
            print(index,'match.span(0):', match.span(0))
            print(index,'match.span(1):', match.span(1))
            print(index,'match.span(2):', match.span(2))
        
        print('\n# Match.pos')
        print('''
        The value of pos which was passed to the search() or match() method of 
        a regex object. This is the index into the string at which the RE 
        engine started looking for a match.
        ''')
        pattern = re.compile('new (?P<new>car)|old (?P<old>car)')
        print('pattern =', pattern)
        text = 'I bought a new car and got rid of the old car'
        print('text =', text)
        match = pattern.search(text, 12, 45)
        print('match:', match)
        print('match.pos:', match.pos)
        
        print('\n# Match.endpos')
        print('''
        The value of endpos which was passed to the search() or match() method 
        of a regex object. This is the index into the string beyond which the 
        RE engine will not go.
        ''')
        print('match.endpos:', match.endpos)
        
        print('\n# Match.lastindex')
        print('''
        The integer index of the last matched capturing group, or None if no 
        group was matched at all. For example, the expressions (a)b, ((a)(b)), 
        and ((ab)) will have lastindex == 1 if applied to the string 'ab', 
        while the expression (a)(b) will have lastindex == 2, if applied to the
        same string.
        ''')
        print('match.lastindex:', match.lastindex)
           
        print('\n# Match.lastgroup')
        print('''
        The name of the last matched capturing group, or None if the group 
        didn’t have a name, or if no group was matched at all.
        ''')
        print('match.lastgroup:', match.lastgroup)
        
        print('\n# Match.re')
        '''
        The regular expression object whose match() or search() method produced
        this match instance.
        '''
        print('match.re:', match.re)
        
        print('\n#  Match.string')
        print('''
        The string passed to match() or search().
        ''')
        print('match.string:', match.string)
        
    def regular_expression_examples(self):
        """
        Checking for a Pair:
            In this example, we’ll use the following helper function to display
            match objects a little more gracefully.
        """
        def displaymatch(match):
            if match is None:
                return None
            return '<Match: %r, groups=%r>' % (match.group(), match.groups())
        
        pattern = re.compile('new (?P<new>car)|old (?P<old>car)')
        print('pattern =', pattern)
        text = 'I bought a new car and got rid of the old car'
        print('text =', text)
        match_itr = pattern.finditer(text)
        print('match_itr:', match_itr)
        print('displaymatch(match):', 
              [displaymatch(match) for match in match_itr])
        
        print('''
        Suppose you are writing a poker program where a player’s hand is 
        represented as a 5-character string with each character representing a 
        card, “a” for ace, “k” for king, “q” for queen, “j” for jack, “t” for 
        10, and “2” through “9” representing the card with that value.
        To see if a given string is a valid hand, one could do the following:
        ''')
        valid = re.compile(r"^[a2-9tjqk]{5}$")
        print('valid =', valid)
        print('displaymatch(valid.match("akt5q")):',
              displaymatch(valid.match("akt5q")))  # Valid.
        print('displaymatch(valid.match("akt5e")):',
              displaymatch(valid.match("akt5e")))  # Invalid.
        print('displaymatch(valid.match("akt")):',
              displaymatch(valid.match("akt")))    # Invalid.
        print('displaymatch(valid.match("727ak")):',
              displaymatch(valid.match("727ak")))  # Valid.
        
        print('''
        That last hand, "727ak", contained a pair, or two of the same valued 
        cards. To match this with a regular expression, one could use 
        backreferences as such:
        ''')
        pair = re.compile(r".*(.).*\1")
        print('pair =', pair)
        print('displaymatch(pair.match("717ak")):',
              displaymatch(pair.match("717ak")))     # Pair of 7s.
        print('displaymatch(pair.match("718ak")):', 
              displaymatch(pair.match("718ak")))     # No pair
        print('displaymatch(pair.match("354aa")):', 
              displaymatch(pair.match("354aa")))     # Pair of aces.
        
        print('''
        To find out what card the pair consists of, one could use the group() 
        method of the match object in the following manner:
        ''')
        print('pair.match("717ak").group(1):', pair.match("717ak").group(1))
        try:
            pair.match("718ak").group(1)
        except AttributeError as e:
            print('AttributeError:', e)
            
        print('\n# Simulating scanf()')
        print('''
        scanf() Token                   Regular Expression
        --------------------------------------------------
        %c                              .
        %5c                             .{5}
        %d                              [-+]?\d+
        %e, %E, %f, %g                  [-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?
        %i                              [-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)
        %o                              [-+]?[0-7]+
        %s                              \S+
        %u                              \d+
        %x, %X                          [-+]?(0[xX])?[\dA-Fa-f]+
        ''')
        
        print('\n# search() vs. match()')
        print('''
        Python offers two different primitive operations based on regular 
        expressions: re.match() checks for a match only at the beginning of the
        string, while re.search() checks for a match anywhere in the string 
        (this is what Perl does by default).
        ''')
        print('re.match("c", "abcdef"):', re.match("c", "abcdef"))   # No match
        print('re.search("c", "abcdef"):', re.search("c", "abcdef"))    # Match
        
        print('''
        Regular expressions beginning with '^' can be used with search() to 
        restrict the match at the beginning of the string:
        ''')
        print('re.match("c", "abcdef"):', re.match("c", "abcdef"))   # No match
        print('re.search("^c", "abcdef"):', re.search("^c", "abcdef"))# No match
        print('re.search("^a", "abcdef"):', re.search("^a", "abcdef"))  # Match
        
        print('''
        Note however that in MULTILINE mode match() only matches at the 
        beginning of the string, whereas using search() with a regular 
        expression beginning with '^' will match at the beginning of each line.
        ''')
        print("re.match('X', 'A\\nB\\nX', re.MULTILINE):", 
              re.match('X', 'A\nB\nX', re.MULTILINE))  # No match
        print("re.search('^X', 'A\\nB\\nX', re.MULTILINE):", 
              re.search('^X', 'A\nB\nX', re.MULTILINE))  # Match
        
        print('\n# Making a Phonebook')
        '''
        split() splits a string into a list delimited by the passed pattern. 
        The method is invaluable for converting textual data into data 
        structures that can be easily read and modified by Python as 
        demonstrated in the following example that creates a phonebook.

        First, here is the input. Normally it may come from a file, here we are
        using triple-quoted string syntax:
        '''
        text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
        entries = re.split("\n+", text)
        print('re.split("\\n+", text):', entries, end='\n\n')
        print('[re.split(":? ", entry, 3) for entry in entries]:',
              [re.split(":? ", entry, 3) for entry in entries], end='\n\n')
        print('[re.split(":? |\.", entry, 3) for entry in entries]:',
              [re.split(":? |\.", entry, 5) for entry in entries])
        
        print('\n# Text Munging')
        print('''
        sub() replaces every occurrence of a pattern with a string or the 
        result of a function. This example demonstrates using sub() with a 
        function to “munge” text, or randomize the order of all the characters 
        in each word of a sentence except for the first and last characters:
        ''')
        def repl(m):
            inner_word = list(m.group(2))
            print(inner_word)
            random.shuffle(inner_word)
            print('random.shuffle:', inner_word)
            return m.group(1) + "".join(inner_word) + m.group(3)
        text = "Professor Abdolmalek, please report your absences promptly."
        print('text =', text)
        print('re.sub(r"(\w)(\w+)(\w)", repl, text):',
              re.sub(r"(\w)(\w+)(\w)", repl, text))
        
        print('\n# Finding all Adverbs')
        print('''
        findall() matches all occurrences of a pattern, not just the first one 
        as search() does. For example, if a writer wanted to find all of the 
        adverbs in some text, they might use findall() in the following manner:
        ''')
        text = "He was carefully disguised but captured quickly by police."
        print('text =', text)
        print('re.findall(r"\w+ly", text):', re.findall(r"\w+ly", text))
        
        print('\n# Finding all Adverbs and their Positions')
        print('''
        If one wants more information about all matches of a pattern than the 
        matched text, finditer() is useful as it provides match objects instead
        of strings. Continuing with the previous example, if a writer wanted to
        find all of the adverbs and their positions in some text, they would 
        use finditer() in the following manner:
        ''')
        [print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0))) 
        for m in re.finditer(r"\w+ly", text)]
        
        print('\n# Raw String Notation')
        print('''
        Raw string notation (r"text") keeps regular expressions sane. Without 
        it, every backslash ('\') in a regular expression would have to be 
        prefixed with another one to escape it. For example, the two following 
        lines of code are functionally identical:
        ''')
        print('re.match(r"\W(.)\\1\W", " ff "):', 
              re.match(r"\W(.)\1\W", " ff "))
        print('re.match("\\W(.)\\1\\W", " ff "):', 
              re.match("\\W(.)\\1\\W", " ff "))
        
        print('\n# Writing a Tokenizer')
        print('''
        A tokenizer or scanner analyzes a string to categorize groups of 
        characters. This is a useful first step in writing a compiler or 
        interpreter.
        The text categories are specified with regular expressions. The 
        technique is to combine those into a single master regular expression 
        and to loop over successive matches:
        ''')
        Token = collections.namedtuple('Token', ['type', 'value', 'line', 
                                                 'column'])
        
        def tokenize(code):
            keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
            token_specification = [
                ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
                ('ASSIGN',   r':='),           # Assignment operator
                ('END',      r';'),            # Statement terminator
                ('ID',       r'[A-Za-z]+'),    # Identifiers
                ('OP',       r'[+\-*/]'),      # Arithmetic operators
                ('NEWLINE',  r'\n'),           # Line endings
                ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
                ('MISMATCH', r'.'),            # Any other character
            ]
            tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in 
                                 token_specification)
            line_num = 1
            line_start = 0
            for mo in re.finditer(tok_regex, code):
                kind = mo.lastgroup
                value = mo.group()
                column = mo.start() - line_start
                if kind == 'NUMBER':
                    value = float(value) if '.' in value else int(value)
                elif kind == 'ID' and value in keywords:
                    kind = value
                elif kind == 'NEWLINE':
                    line_start = mo.end()
                    line_num += 1
                    continue
                elif kind == 'SKIP':
                    continue
                elif kind == 'MISMATCH':
                    raise RuntimeError(value +' unexpected on line '+line_num)
                yield Token(kind, value, line_num, column)
        
        statements = '''
            IF quantity THEN
                total := total + price * quantity;
                tax := price * 0.05;
            ENDIF;
        '''
        
        for token in tokenize(statements):
            print(token)
        
        
        
            
    
    
    
    
    
if __name__ == '__main__':
    reo = RegularExpressionOperation()
    print(reo.__doc__)
    
#    print('\n# Regular Expression Syntax')
#    print(reo.regular_expression_syntax_test.__doc__)
#    reo.regular_expression_syntax_test()
    
#    print('\n# Module Contents')
#    print(reo.module_content_test.__doc__)
#    reo.module_content_test()
    
#    print('\n# re.search(pattern, string, flags=0)')
#    print(reo.re_search_test.__doc__)
#    reo.re_search_test()
    
#    print('\n# re.match(pattern, string, flags=0)')
#    print(reo.re_match_test.__doc__)
#    reo.re_match_test()
    
#    print("\n# re.fullmatch(pattern, string, flags=0)")
#    print(reo.re_fullmatch_test.__doc__)
#    reo.re_fullmatch_test()
    
#    print("\n# re.split(pattern, string, maxsplit=0, flags=0)")
#    print(reo.re_split_test.__doc__)
#    reo.re_split_test()
    
#    print("\n# re.findall(pattern, string, flags=0)")
#    print(reo.re_findall_test.__doc__)
#    reo.re_findall_test()
    
#    print("\n# re.finditer(pattern, string, flags=0)")
#    print(reo.re_finditer_test.__doc__)
#    reo.re_finditer_test()
    
#    print("\n# re.sub(pattern, repl, string, count=0, flags=0)")
#    print(reo.re_sub_test.__doc__)
#    reo.re_sub_test()
    
#    print("\n# re.subn(pattern, repl, string, count=0, flags=0)")
#    print(reo.re_subn_test.__doc__)
#    reo.re_subn_test()
    
#    print("\n# re.escape(pattern)")
#    print(reo.re_escape_test.__doc__)
#    reo.re_escape_test()
    
#    print("\n# re.purge()")
#    print(reo.re_purge_test.__doc__)
#    reo.re_purge_test()
    
#    print("\n# exception re.error(msg, pattern=None, pos=None)")
#    print(reo.exception_re_error_test.__doc__)
#    reo.exception_re_error_test()
    
#    reo.__doc__ = """
#    Regular Expression Objects:-
#    Compiled regular expression objects support the following methods and 
#    attributes:"""
#    print(reo.__doc__)
        
#    print("\n# Pattern.search(string[, pos[, endpos]])")
#    print(reo.pattern_search_test.__doc__)
#    reo.pattern_search_test()
    
#    print('\n# Pattern.match(string[, pos[, endpos]])')
#    print(reo.pattern_match_test.__doc__)
#    reo.pattern_match_test()
    
#    print('\n# Pattern.fullmatch(string[, pos[, endpos]])')
#    print(reo.pattern_fullmatch_test.__doc__)
#    reo.pattern_fullmatch_test()
    
#    print('\n# Pattern.split(string, maxsplit=0)')
#    print(reo.pattern_split_test.__doc__)
#    reo.pattern_split_test()
    
#    print('\n# Pattern.findall(string[, pos[, endpos]])')
#    print(reo.pattern_findall_test.__doc__)
#    reo.pattern_findall_test()
    
#    print('\n# Pattern.finditer(string[, pos[, endpos]])')
#    print(reo.pattern_finditer_test.__doc__)
#    reo.pattern_finditer_test()
    
#    print('\n# Pattern.sub(repl, string, count=0)')
#    print(reo.pattern_sub_test.__doc__)
#    reo.pattern_sub_test()
    
#    print('\n# Pattern.subn(repl, string, count=0)')
#    print(reo.pattern_subn_test.__doc__)
#    reo.pattern_subn_test()
    
#    print('\n# Extra Patterns')
#    print(reo.pattern_extras_test.__doc__)
#    reo.pattern_extras_test()

#    print('\n# Match Objects')
#    print(reo.match_objects_test.__doc__)
#    reo.match_objects_test()
    
    print('\n# Regular Expression Examples')
    print(reo.regular_expression_examples.__doc__)
    reo.regular_expression_examples()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    