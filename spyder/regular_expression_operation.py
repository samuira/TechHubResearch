# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 14:31:24 2019

@author: Rajesh Samui
"""

import re

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
        print(re.search('test', 'TeSt', re.IGNORECASE))
        print(re.match('test', 'TeSt', re.IGNORECASE))
        print(re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE))
        
        
        
        
        
        
        
        
        
        
        
        
    
if __name__ == '__main__':
    reo = RegularExpressionOperation()
    print(reo.__doc__)
    
#    print('\n# Regular Expression Syntax')
#    print(reo.regular_expression_syntax_test.__doc__)
#    reo.regular_expression_syntax_test()
    
    print('\n# Module Contents')
    print(reo.module_content_test.__doc__)
    reo.module_content_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    