# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 14:31:24 2019

@author: Rajesh Samui
"""

import re
import string

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
        print(pattern)
        print(pattern.search("dog"))     # Match at index 0
        print(pattern.search("dog", 1))  # No match; search doesn't include the "d"
    
    
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
    
    reo.__doc__ = """
    Regular Expression Objects:-
    Compiled regular expression objects support the following methods and 
    attributes:"""
    print(reo.__doc__)
        
    print("\n# Pattern.search(string[, pos[, endpos]])")
    print(reo.pattern_search_test.__doc__)
    reo.pattern_search_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    